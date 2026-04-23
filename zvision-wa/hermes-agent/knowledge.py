"""PDF Knowledge Base — TF-IDF search, no external vector DB."""
from __future__ import annotations

import asyncio
import hashlib
import json
import logging
import math
import os
import re
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

KNOWLEDGE_DIR = Path(os.getenv("HERMES_HOME", "/opt/data")) / "knowledge"
CHUNK_SIZE = 400
CHUNK_OVERLAP = 80
MAX_CONTEXT_CHUNKS = 4
MIN_SCORE = 0.05

_STOPWORDS = {
    "a", "o", "e", "de", "do", "da", "em", "um", "uma", "que", "se", "no",
    "na", "com", "para", "por", "mas", "ou", "ao", "os", "as", "dos", "das",
    "nos", "nas", "pelo", "pela", "isso", "este", "essa", "mais", "como",
    "foi", "ser", "tem", "seu", "sua", "também", "já", "não", "muito",
}


@dataclass
class Chunk:
    text: str
    source: str
    page: int
    chunk_idx: int
    doc_id: str = field(init=False)

    def __post_init__(self) -> None:
        self.doc_id = f"{self.source}:p{self.page}:c{self.chunk_idx}"


class KnowledgeBase:
    """
    Loads PDFs from KNOWLEDGE_DIR, chunks them, builds TF-IDF index.
    Relevant chunks are injected into the agent's system prompt.
    Cache in index.json invalidated when PDFs change (hash-based).
    """

    def __init__(self) -> None:
        self.chunks: list[Chunk] = []
        self._index: dict[str, dict[str, float]] = {}
        self._loaded = False
        self._cache = Path(os.getenv("HERMES_HOME", "/opt/data")) / "knowledge-cache.json"

    async def load(self) -> None:
        if self._loaded:
            return
        KNOWLEDGE_DIR.mkdir(parents=True, exist_ok=True)

        if await self._try_load_cache():
            self._loaded = True
            logger.info("[knowledge] %d chunks from cache", len(self.chunks))
            return

        pdfs = list(KNOWLEDGE_DIR.glob("*.pdf"))
        if not pdfs:
            logger.info("[knowledge] No PDFs in %s", KNOWLEDGE_DIR)
            self._loaded = True
            return

        logger.info("[knowledge] Parsing %d PDF(s)...", len(pdfs))
        chunks: list[Chunk] = []
        loop = asyncio.get_event_loop()

        for pdf in pdfs:
            try:
                pdf_chunks = await loop.run_in_executor(None, self._parse_pdf, pdf)
                chunks.extend(pdf_chunks)
                logger.info("[knowledge] %s → %d chunks", pdf.name, len(pdf_chunks))
            except Exception as exc:
                logger.error("[knowledge] Failed %s: %s", pdf.name, exc)

        self.chunks = chunks
        self._build_index()
        await self._save_cache()
        self._loaded = True
        logger.info("[knowledge] %d total chunks indexed", len(self.chunks))

    def search(self, query: str, top_k: int = MAX_CONTEXT_CHUNKS) -> list[Chunk]:
        if not self.chunks:
            return []
        q_vec = _tfidf_vec(_tokenize(query))
        scored = [
            (_cosine(q_vec, self._index.get(c.doc_id, {})), c)
            for c in self.chunks
        ]
        scored = [(s, c) for s, c in scored if s >= MIN_SCORE]
        scored.sort(key=lambda x: x[0], reverse=True)
        return [c for _, c in scored[:top_k]]

    def format_context(self, chunks: list[Chunk]) -> str:
        if not chunks:
            return ""
        lines = ["[CONHECIMENTO DE VENDAS RELEVANTE]"]
        for c in chunks:
            lines.append(f"\n— {c.source} (p.{c.page}):")
            lines.append(c.text.strip())
        return "\n".join(lines)

    # ── PDF parsing ──────────────────────────────────────────────────────────

    def _parse_pdf(self, path: Path) -> list[Chunk]:
        from pypdf import PdfReader
        reader = PdfReader(str(path))
        source = path.stem
        pages: list[tuple[int, str]] = []
        for i, page in enumerate(reader.pages, start=1):
            text = _clean_pdf_text(page.extract_text() or "")
            if text.strip():
                pages.append((i, text))
        return _chunk_pages(pages, source)

    def _build_index(self) -> None:
        n = len(self.chunks)
        if n == 0:
            return
        tokenized = [(c.doc_id, _tokenize(c.text)) for c in self.chunks]
        df: dict[str, int] = {}
        for _, tokens in tokenized:
            for t in set(tokens):
                df[t] = df.get(t, 0) + 1
        for doc_id, tokens in tokenized:
            tf = Counter(tokens)
            total = len(tokens) or 1
            self._index[doc_id] = {
                t: (cnt / total) * math.log((n + 1) / (df.get(t, 0) + 1))
                for t, cnt in tf.items()
            }

    # ── Cache ─────────────────────────────────────────────────────────────────

    async def _try_load_cache(self) -> bool:
        if not self._cache.exists():
            return False
        try:
            data = json.loads(self._cache.read_text())
            if data.get("pdf_hash") != self._pdf_hash():
                return False
            self.chunks = [Chunk(**c) for c in data["chunks"]]
            self._index = data["index"]
            return True
        except Exception as exc:
            logger.warning("[knowledge] Cache invalid: %s", exc)
            return False

    async def _save_cache(self) -> None:
        try:
            self._cache.write_text(json.dumps({
                "pdf_hash": self._pdf_hash(),
                "chunks": [
                    {"text": c.text, "source": c.source, "page": c.page, "chunk_idx": c.chunk_idx}
                    for c in self.chunks
                ],
                "index": self._index,
            }, ensure_ascii=False))
        except Exception as exc:
            logger.warning("[knowledge] Cache save failed: %s", exc)

    def _pdf_hash(self) -> str:
        parts = [f"{p.name}:{p.stat().st_size}" for p in sorted(KNOWLEDGE_DIR.glob("*.pdf"))]
        return hashlib.md5("|".join(parts).encode()).hexdigest()


# ── Helpers ───────────────────────────────────────────────────────────────────

def _clean_pdf_text(text: str) -> str:
    text = re.sub(r"[\x00-\x08\x0b-\x0c\x0e-\x1f\x7f]", "", text)
    text = re.sub(r"-\n", "", text)
    text = re.sub(r"\n(?=[a-z])", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def _chunk_pages(pages: list[tuple[int, str]], source: str) -> list[Chunk]:
    chunks: list[Chunk] = []
    idx = 0
    step = CHUNK_SIZE - CHUNK_OVERLAP
    for page_num, text in pages:
        words = text.split()
        for i in range(0, max(1, len(words) - CHUNK_OVERLAP), step):
            window = words[i: i + CHUNK_SIZE]
            if len(window) < 30:
                continue
            chunks.append(Chunk(text=" ".join(window), source=source, page=page_num, chunk_idx=idx))
            idx += 1
    return chunks


def _tokenize(text: str) -> list[str]:
    text = re.sub(r"[^\w\s]", " ", text.lower())
    return [t for t in text.split() if len(t) > 2 and t not in _STOPWORDS]


def _tfidf_vec(tokens: list[str]) -> dict[str, float]:
    tf = Counter(tokens)
    total = len(tokens) or 1
    return {t: c / total for t, c in tf.items()}


def _cosine(a: dict[str, float], b: dict[str, float]) -> float:
    dot = sum(a.get(t, 0.0) * v for t, v in b.items())
    norm_a = math.sqrt(sum(v * v for v in a.values())) or 1.0
    norm_b = math.sqrt(sum(v * v for v in b.values())) or 1.0
    return dot / (norm_a * norm_b)


_kb: Optional[KnowledgeBase] = None


def get_knowledge_base() -> KnowledgeBase:
    global _kb
    if _kb is None:
        _kb = KnowledgeBase()
    return _kb
