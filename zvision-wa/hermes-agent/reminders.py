"""Background task: send WhatsApp reminders 24h and 1h before scheduled meetings."""
from __future__ import annotations

import asyncio
import json
import logging
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from evolution_client import EvolutionClient

logger = logging.getLogger(__name__)

_SENT_FILE = Path(os.getenv("HERMES_HOME", "/opt/data")) / "sent_reminders.json"
_INTERVAL_SECONDS = 30 * 60  # check every 30 minutes
BRT = timezone(timedelta(hours=-3))


def _load_sent() -> set[str]:
    try:
        return set(json.loads(_SENT_FILE.read_text()))
    except Exception:
        return set()


def _save_sent(sent: set[str]) -> None:
    try:
        _SENT_FILE.write_text(json.dumps(sorted(sent), ensure_ascii=False))
    except Exception as exc:
        logger.warning("[reminders] Failed to save: %s", exc)


async def run_reminder_loop(evolution: "EvolutionClient") -> None:
    """Runs forever, checking for upcoming meetings and sending WhatsApp reminders."""
    logger.info("[reminders] Loop started (interval=%ds)", _INTERVAL_SECONDS)
    while True:
        try:
            await _tick(evolution)
        except Exception as exc:
            logger.error("[reminders] Tick error: %s", exc)
        await asyncio.sleep(_INTERVAL_SECONDS)


async def _tick(evolution: "EvolutionClient") -> None:
    import calendar_client

    sent = _load_sent()
    changed = False

    # 24h window: events starting in 23–25h from now
    events_24h = await asyncio.to_thread(calendar_client.list_upcoming_events, 23.0, 25.0)
    for ev in events_24h:
        key = f"{ev['id']}:24h"
        if key in sent:
            continue

        start_brt = ev["start_utc"].astimezone(BRT)
        msg = (
            f"Oi! Lembrando que amanhã às {start_brt.strftime('%H')}h "
            f"é sua call sobre o site de vocês. "
            f"Qualquer dúvida até lá, me chama aqui!"
        )
        try:
            await evolution.send_text(ev["phone"], msg)
            sent.add(key)
            changed = True
            logger.info("[reminders] 24h → %s****", ev["phone"][:5])
        except Exception as exc:
            logger.warning("[reminders] 24h failed %s****: %s", ev["phone"][:4], exc)

    # 1h window: events starting in 50–70 min from now
    events_1h = await asyncio.to_thread(calendar_client.list_upcoming_events, 0.83, 1.17)
    for ev in events_1h:
        key = f"{ev['id']}:1h"
        if key in sent:
            continue

        meet = ev.get("meet_link") or "verifique seu e-mail"
        msg = f"Sua call começa em 1 hora! Link da reunião: {meet}"
        try:
            await evolution.send_text(ev["phone"], msg)
            sent.add(key)
            changed = True
            logger.info("[reminders] 1h → %s****", ev["phone"][:5])
        except Exception as exc:
            logger.warning("[reminders] 1h failed %s****: %s", ev["phone"][:4], exc)

    if changed:
        _save_sent(sent)
