"""Google Calendar integration — slot availability, booking, Meet link, event lookup."""
from __future__ import annotations

import json
import logging
import os
import uuid
from datetime import datetime, timedelta, timezone
from typing import Optional

logger = logging.getLogger(__name__)

_SCOPES = ["https://www.googleapis.com/auth/calendar"]
CALENDAR_ID = os.getenv("GOOGLE_CALENDAR_ID", "primary")
_SA_JSON_RAW = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON", "")

SLOT_DURATION_MIN = 30
WORKING_START_H = 9
WORKING_END_H = 18
BRT = timezone(timedelta(hours=-3))  # São Paulo — sem horário de verão desde 2019

_DAYS_PT = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]


def is_enabled() -> bool:
    return bool(_SA_JSON_RAW) and bool(CALENDAR_ID)


def _service():
    if not _SA_JSON_RAW:
        raise RuntimeError("GOOGLE_SERVICE_ACCOUNT_JSON not set")
    from google.oauth2.service_account import Credentials
    from googleapiclient.discovery import build
    info = json.loads(_SA_JSON_RAW)
    creds = Credentials.from_service_account_info(info, scopes=_SCOPES)
    return build("calendar", "v3", credentials=creds, cache_discovery=False)


def get_available_slots(days_ahead: int = 3, max_slots: int = 3) -> list[dict]:
    """
    Returns up to max_slots available windows in the next days_ahead working days.
    Slot dict: {"label": "Quarta 23/04 às 14h", "start_iso": UTC ISO, "end_iso": UTC ISO}
    """
    svc = _service()
    now_brt = datetime.now(BRT)

    # Round up to next full hour
    if now_brt.minute > 0 or now_brt.second > 0:
        next_hour = now_brt.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
    else:
        next_hour = now_brt.replace(minute=0, second=0, microsecond=0)

    # Clamp to working hours
    if next_hour.hour < WORKING_START_H:
        next_hour = next_hour.replace(hour=WORKING_START_H)
    elif next_hour.hour >= WORKING_END_H:
        next_hour = (next_hour + timedelta(days=1)).replace(hour=WORKING_START_H, minute=0, second=0, microsecond=0)

    search_end = now_brt + timedelta(days=days_ahead + 1)

    # Query freebusy
    fb = svc.freebusy().query(body={
        "timeMin": next_hour.astimezone(timezone.utc).isoformat(),
        "timeMax": search_end.astimezone(timezone.utc).isoformat(),
        "items": [{"id": CALENDAR_ID}],
    }).execute()

    busy = fb.get("calendars", {}).get(CALENDAR_ID, {}).get("busy", [])
    busy_intervals: list[tuple[datetime, datetime]] = []
    for b in busy:
        bs = datetime.fromisoformat(b["start"].replace("Z", "+00:00")).astimezone(BRT)
        be = datetime.fromisoformat(b["end"].replace("Z", "+00:00")).astimezone(BRT)
        busy_intervals.append((bs, be))

    def _is_busy(s: datetime, e: datetime) -> bool:
        return any(s < be and e > bs for bs, be in busy_intervals)

    slots: list[dict] = []
    cur = next_hour

    while len(slots) < max_slots and cur < search_end:
        if cur.weekday() >= 5:  # skip weekends
            cur = (cur + timedelta(days=1)).replace(hour=WORKING_START_H, minute=0, second=0, microsecond=0)
            continue
        if cur.hour >= WORKING_END_H:
            cur = (cur + timedelta(days=1)).replace(hour=WORKING_START_H, minute=0, second=0, microsecond=0)
            continue
        if cur.hour < WORKING_START_H:
            cur = cur.replace(hour=WORKING_START_H, minute=0, second=0, microsecond=0)
            continue

        slot_end = cur + timedelta(minutes=SLOT_DURATION_MIN)
        if not _is_busy(cur, slot_end):
            time_str = f"{cur.strftime('%H')}h{cur.strftime('%M')}" if cur.minute else f"{cur.strftime('%H')}h"
            label = f"{_DAYS_PT[cur.weekday()]} {cur.strftime('%d/%m')} às {time_str}"
            slots.append({
                "label": label,
                "start_iso": cur.astimezone(timezone.utc).isoformat(),
                "end_iso": slot_end.astimezone(timezone.utc).isoformat(),
            })

        cur += timedelta(minutes=SLOT_DURATION_MIN)

    return slots


def create_booking(
    name: str,
    email: str,
    phone: str,
    start_iso: str,  # UTC ISO string
    end_iso: str,    # UTC ISO string
    pain: str = "",
) -> tuple[str, Optional[str]]:
    """
    Creates a Google Calendar event with Google Meet.
    Returns (event_id, meet_link | None).
    """
    from googleapiclient.errors import HttpError

    svc = _service()
    start_dt = datetime.fromisoformat(start_iso.replace("Z", "+00:00"))
    start_brt = start_dt.astimezone(BRT)

    event_body = {
        "summary": f"Briefing Zvision — {name}",
        "description": (
            f"Lead: {name}\n"
            f"WhatsApp: +{phone}\n"
            f"Necessidade: {(pain or 'não informada')[:300]}\n\n"
            "Agendado via HERMES Agent"
        ),
        "start": {"dateTime": start_iso, "timeZone": "UTC"},
        "end": {"dateTime": end_iso, "timeZone": "UTC"},
        "attendees": [{"email": email, "displayName": name}],
        "conferenceData": {
            "createRequest": {
                "requestId": str(uuid.uuid4()),
                "conferenceSolutionKey": {"type": "hangoutsMeet"},
            }
        },
        "extendedProperties": {
            "private": {
                "phone": phone,
                "pain": (pain or "")[:200],
            }
        },
        "reminders": {
            "useDefault": False,
            "overrides": [{"method": "email", "minutes": 60}],
        },
    }

    try:
        created = svc.events().insert(
            calendarId=CALENDAR_ID,
            body=event_body,
            conferenceDataVersion=1,
            sendUpdates="externalOnly",
        ).execute()
    except HttpError as exc:
        logger.error("[calendar] create_booking failed: %s", exc)
        raise

    event_id: str = created["id"]
    meet_link: Optional[str] = None
    for ep in created.get("conferenceData", {}).get("entryPoints", []):
        if ep.get("entryPointType") == "video":
            meet_link = ep.get("uri")
            break

    logger.info("[calendar] Booked event %s for %s", event_id, name[:20])
    return event_id, meet_link


def list_upcoming_events(from_hours: float, to_hours: float) -> list[dict]:
    """
    Returns events starting between from_hours and to_hours from now
    that have a phone number in extendedProperties.private.
    Each event: {"id", "summary", "start_utc", "phone", "pain", "meet_link"}
    """
    svc = _service()
    now = datetime.now(timezone.utc)

    result = svc.events().list(
        calendarId=CALENDAR_ID,
        timeMin=(now + timedelta(hours=from_hours)).isoformat(),
        timeMax=(now + timedelta(hours=to_hours)).isoformat(),
        singleEvents=True,
        orderBy="startTime",
    ).execute()

    events = []
    for item in result.get("items", []):
        private = (item.get("extendedProperties") or {}).get("private", {})
        phone = private.get("phone", "")
        if not phone:
            continue

        start_str = (item.get("start") or {}).get("dateTime", "")
        try:
            start_utc = datetime.fromisoformat(start_str.replace("Z", "+00:00"))
        except ValueError:
            continue

        meet_link: Optional[str] = None
        for ep in (item.get("conferenceData") or {}).get("entryPoints", []):
            if ep.get("entryPointType") == "video":
                meet_link = ep.get("uri")
                break

        events.append({
            "id": item["id"],
            "summary": item.get("summary", ""),
            "start_utc": start_utc,
            "phone": phone,
            "pain": private.get("pain", ""),
            "meet_link": meet_link,
        })

    return events
