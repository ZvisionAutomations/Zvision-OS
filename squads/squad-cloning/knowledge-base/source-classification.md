# Source Classification — Classes de Disponibilidade de Conteudo

> Classifica targets por volume de conteudo disponivel e define a estrategia
> de captura ideal para cada classe.

---

## 4 Classes

### Classe A — Rico (100h+ de conteudo)

**Perfil:** YouTuber ativo, podcaster, autor de multiplos livros, presenca forte em social media.
**Exemplos:** Gary Halbert, Alex Hormozi, Russell Brunson
**Estrategia:**
1. Whisper API transcreve YouTube/podcasts via Whisper (priorizar conteudo longo-form)
2. Claude Code (1M) processa tudo em 1-2 sessoes
3. Priorizar: conteudo original > entrevistas > lives > social media
4. **Output esperado:** Tier 3 (clone completo)

### Classe B — Moderado (20-100h)

**Perfil:** Alguns videos, 1-2 livros, entrevistas esporadicas, presenca moderada online.
**Exemplos:** Eugene Schwartz, Brad Frost
**Estrategia:**
1. Whisper API transcreve o que tem de video/audio
2. Brave Search busca entrevistas, artigos, palestras
3. Complementar com livros (PDF → extracao de texto)
4. **Output esperado:** Tier 2 ou 3

### Classe C — Escasso (<20h)

**Perfil:** Poucos videos, artigos, citacoes. Mais referenciado por terceiros do que produtor de conteudo.
**Exemplos:** Robert Collier, Parris Lampropoulos
**Estrategia:**
1. Brave Search + Codex rastreiam tudo acessivel
2. Livros como fonte primaria
3. Analise de terceiros que estudam/citam essa pessoa
4. Whisper API captura mencoes em podcasts de outros
5. **Output esperado:** Tier 1 ou 2

### Classe D — Historico (so obras escritas)

**Perfil:** Pre-internet, sem video/audio. Apenas livros, cartas, manuscritos.
**Exemplos:** Claude Hopkins, Joseph Campbell, David Ogilvy
**Estrategia:**
1. Livros/obras como fonte unica (PDF → OCR se necessario)
2. Biografias e analises academicas como fonte secundaria
3. Citacoes compiladas por terceiros
4. **Output esperado:** Tier 1 (KBs ricos baseados em obra escrita)

---

## Criterios de Classificacao

| Criterio | A | B | C | D |
|----------|---|---|---|---|
| Video/audio proprio | 100h+ | 20-100h | <20h | 0h |
| Livros publicados | 3+ | 1-2 | 0-1 | 1+ (historico) |
| Artigos/entrevistas | Muitos | Varios | Poucos | Raros |
| Social media ativa | Sim | Parcial | Minima | Nao |
| Palavras estimadas | 200K+ | 50-200K | 10-50K | 5-50K |

---

## Priorizacao de Fontes

| Prioridade | Tipo de fonte | Razao |
|-----------|--------------|-------|
| 1 (Maxima) | Conteudo longo-form proprio (curso, livro, palestra) | Maior profundidade, pensamento estruturado |
| 2 | Entrevistas/podcasts onde e entrevistado | Respostas espontaneas revelam heuristics reais |
| 3 | Artigos/posts escritos pela pessoa | Pensamento organizado mas editado |
| 4 | Social media threads | Insights rapidos, menos profundos |
| 5 | Mencoes por terceiros | Fonte secundaria, menor confianca |

---

## Scoring de Confiabilidade por Fonte

| Fonte | Reliability Score | Notas |
|-------|------------------|-------|
| Transcricao direta (Whisper) | 0.95 | Pequenos erros possiveis |
| Livro (PDF text extraction) | 0.98 | Texto fiel |
| Livro (OCR) | 0.85 | Erros de OCR possiveis |
| Artigo web (Playwright) | 0.95 | Geralmente fiel |
| Social media post | 0.90 | Contexto pode faltar |
| Citacao por terceiro | 0.70 | Pode estar fora de contexto |
| Biografia/analise academica | 0.75 | Interpretacao do autor |
