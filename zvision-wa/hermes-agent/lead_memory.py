"""Lead state machine + JSON persistence — port of memory.ts + handler.ts state logic."""
from __future__ import annotations

import json
import logging
import os
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from typing import Literal, Optional

logger = logging.getLogger(__name__)

LeadState = Literal[
    "VITOR_ACTIVE",
    "ANA_ACTIVE",
    "SCHEDULING",       # collecting email + presenting slots + confirming booking
    "QUALIFIED",
    "NOT_QUALIFIED",
    "HUMAN_HANDOFF",
]

_DATA_DIR = Path(os.getenv("HERMES_HOME", "/opt/data")) / "leads"
MAX_MESSAGES = 40
CONTEXT_WINDOW = 20
REENGAGEMENT_DAYS = 7
HANDOFF_REOPEN_DAYS = 7

_WANTS_HUMAN = [
    "quero falar com humano",
    "falar com atendente",
    "falar com pessoa",
    "falar com o miguel",
    "falar com alguém",
    "atendente humano",
    "pessoa real",
    "quero falar com alguém",
    "me passa pro miguel",
    "fala com o dono",
]

_NEGATION_WORDS = ("não", "nao", "nunca", "jamais")


class Lead:
    """Mirrors TypeScript Lead interface exactly for JSON compatibility."""

    __slots__ = (
        "id", "name", "state", "pain", "summary",
        "message_count", "messages", "handoff_sent",
        "created_at", "updated_at", "last_seen_at",
        # calendar scheduling
        "email", "booking_id", "meeting_at",
        "scheduling_step", "slots_cache",
    )

    def __init__(
        self,
        id: str,
        name: str,
        state: LeadState,
        pain: Optional[str] = None,
        summary: Optional[str] = None,
        message_count: int = 0,
        messages: Optional[list[dict]] = None,
        handoff_sent: bool = False,
        created_at: Optional[str] = None,
        updated_at: Optional[str] = None,
        last_seen_at: Optional[str] = None,
        email: str = "",
        booking_id: str = "",
        meeting_at: str = "",
        scheduling_step: str = "",
        slots_cache: Optional[list] = None,
    ) -> None:
        self.id = id
        self.name = name
        self.state: LeadState = state
        self.pain = pain
        self.summary = summary
        self.message_count = message_count
        self.messages: list[dict] = messages if messages is not None else []
        self.handoff_sent = handoff_sent
        now = _now()
        self.created_at = created_at or now
        self.updated_at = updated_at or now
        self.last_seen_at = last_seen_at
        self.email = email
        self.booking_id = booking_id
        self.meeting_at = meeting_at
        self.scheduling_step = scheduling_step
        self.slots_cache: list = slots_cache if slots_cache is not None else []

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "state": self.state,
            "pain": self.pain,
            "summary": self.summary,
            "messageCount": self.message_count,
            "messages": self.messages,
            "handoffSent": self.handoff_sent,
            "createdAt": self.created_at,
            "updatedAt": _now(),
            "lastSeenAt": self.last_seen_at,
            "email": self.email,
            "bookingId": self.booking_id,
            "meetingAt": self.meeting_at,
            "schedulingStep": self.scheduling_step,
            "slotsCache": self.slots_cache,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "Lead":
        return cls(
            id=d["id"],
            name=d["name"],
            state=d["state"],
            pain=d.get("pain"),
            summary=d.get("summary"),
            message_count=d.get("messageCount", 0),
            messages=d.get("messages", []),
            handoff_sent=d.get("handoffSent", False),
            created_at=d.get("createdAt"),
            updated_at=d.get("updatedAt"),
            last_seen_at=d.get("lastSeenAt"),
            email=d.get("email", ""),
            booking_id=d.get("bookingId", ""),
            meeting_at=d.get("meetingAt", ""),
            scheduling_step=d.get("schedulingStep", ""),
            slots_cache=d.get("slotsCache", []),
        )

    def context_messages(self) -> list[dict]:
        return self.messages[-CONTEXT_WINDOW:]


class LeadStore:
    def __init__(self) -> None:
        _DATA_DIR.mkdir(parents=True, exist_ok=True)

    def _path(self, phone: str) -> Path:
        safe = "".join(c if c.isalnum() else "_" for c in phone)
        return _DATA_DIR / f"{safe}.json"

    def get(self, phone: str) -> Optional[Lead]:
        p = self._path(phone)
        if not p.exists():
            return None
        try:
            return Lead.from_dict(json.loads(p.read_text()))
        except Exception as exc:
            logger.error("[lead_store] Corrupt file %s: %s", p, exc)
            return None

    def save(self, lead: Lead) -> None:
        # Enforce message cap before writing (M4)
        if len(lead.messages) > MAX_MESSAGES:
            lead.messages = lead.messages[-MAX_MESSAGES:]

        target = self._path(lead.id)
        # Atomic write: write to .tmp then rename (M3)
        tmp = target.with_suffix(".tmp")
        try:
            tmp.write_text(json.dumps(lead.to_dict(), ensure_ascii=False, indent=2))
            tmp.replace(target)
        except Exception:
            tmp.unlink(missing_ok=True)
            raise

    def create(self, phone: str, name: str, state: LeadState) -> Lead:
        lead = Lead(id=phone, name=name, state=state)
        self.save(lead)
        return lead


class LeadStateManager:
    def __init__(self) -> None:
        self.store = LeadStore()

    def get_or_create_inbound(self, phone: str, name: str) -> Lead:
        lead = self.store.get(phone)
        if lead is None:
            lead = self.store.create(phone, name, "ANA_ACTIVE")
            logger.info("[lead] New inbound: %s (%s)", name, phone)
        return lead

    def create_outbound(self, phone: str, business_name: str) -> Optional[Lead]:
        if self.store.get(phone):
            logger.info("[lead] %s already exists — skip outbound", phone)
            return None
        return self.store.create(phone, business_name, "VITOR_ACTIVE")

    def check_re_engagement(self, lead: Lead) -> bool:
        if lead.state != "NOT_QUALIFIED" or not lead.updated_at:
            return False
        try:
            updated = datetime.fromisoformat(lead.updated_at.rstrip("Z")).replace(tzinfo=timezone.utc)
            days = (datetime.now(timezone.utc) - updated).days
        except ValueError:
            return False
        if days >= REENGAGEMENT_DAYS:
            lead.state = "ANA_ACTIVE"
            lead.handoff_sent = False
            logger.info("[lead] Re-engagement: %s after %d days", lead.name, days)
            self.store.save(lead)
            return True
        logger.info("[lead] %s ignored — NOT_QUALIFIED for %d days", lead.id, days)
        return False

    def check_handoff_reopen(self, lead: Lead) -> bool:
        """Returns True if the HUMAN_HANDOFF lead should re-engage after cooldown."""
        if lead.state != "HUMAN_HANDOFF" or not lead.updated_at:
            return False
        try:
            updated = datetime.fromisoformat(lead.updated_at.rstrip("Z")).replace(tzinfo=timezone.utc)
            days = (datetime.now(timezone.utc) - updated).days
        except ValueError:
            return False
        if days >= HANDOFF_REOPEN_DAYS:
            lead.state = "ANA_ACTIVE"
            lead.handoff_sent = False
            logger.info("[lead] Handoff reopen: %s after %d days", lead.name, days)
            self.store.save(lead)
            return True
        return False

    def wants_human(self, text: str) -> bool:
        """Detects human handoff intent, ignoring negated phrases (H1)."""
        # Normalize unicode (L4) before matching
        lower = unicodedata.normalize("NFC", text.lower())
        for phrase in _WANTS_HUMAN:
            idx = lower.find(phrase)
            if idx == -1:
                continue
            # Check for negation within 25 chars before the phrase
            window = lower[max(0, idx - 25):idx]
            if any(neg in window for neg in _NEGATION_WORDS):
                continue
            return True
        return False

    def process_state_transition(self, lead: Lead, response: str) -> None:
        lower = response.lower()

        if lead.state == "VITOR_ACTIVE":
            if "deixa eu te conectar com a ana" in lower:
                lead.state = "ANA_ACTIVE"
                logger.info("[state] %s: VITOR_ACTIVE → ANA_ACTIVE", lead.id)
            elif "se mudar de ideia" in lower or "obrigado pelo seu tempo" in lower:
                lead.state = "NOT_QUALIFIED"
                logger.info("[state] %s: VITOR_ACTIVE → NOT_QUALIFIED", lead.id)

        elif lead.state == "ANA_ACTIVE":
            # cal.com fallback kept for manual overrides without Google Calendar
            if "cal.com/zvision-automations" in lower:
                lead.state = "QUALIFIED"
                logger.info("[state] %s: ANA_ACTIVE → QUALIFIED (link)", lead.id)
            elif "obrigada pelo tempo" in lower or "se um dia fizer sentido" in lower:
                lead.state = "NOT_QUALIFIED"
                logger.info("[state] %s: ANA_ACTIVE → NOT_QUALIFIED", lead.id)
            else:
                self._extract_pain(lead)

        elif lead.state == "SCHEDULING":
            pass  # managed deterministically by main.py:_process_scheduling

    def is_handoff_response(self, response: str) -> bool:
        return "deixa eu chamar o miguel diretamente, um segundo" in response.lower()

    def _extract_pain(self, lead: Lead) -> None:
        if lead.pain or len(lead.messages) < 2:
            return
        last_user = next(
            (m["content"] for m in reversed(lead.messages) if m.get("role") == "user"),
            None,
        )
        if last_user and len(last_user) > 10:
            lead.pain = last_user[:300]


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()
