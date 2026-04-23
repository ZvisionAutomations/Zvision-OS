"""
Harness — AC1..AC5 para calendar booking sem conferenceData (spec hermes-calendar-fix.md)
Roda com: pytest tests/test_calendar.py -v
"""
from unittest.mock import MagicMock, patch

import pytest


def _mock_service(event_id: str = "evt-123") -> MagicMock:
    """Monta um mock do googleapiclient service."""
    created_event = {
        "id": event_id,
        "conferenceData": {},  # sem Meet link
    }
    events_mock = MagicMock()
    events_mock.insert.return_value.execute.return_value = created_event
    events_mock.list.return_value.execute.return_value = {"items": []}

    freebusy_mock = MagicMock()
    freebusy_mock.query.return_value.execute.return_value = {
        "calendars": {"primary": {"busy": []}}
    }

    svc = MagicMock()
    svc.events.return_value = events_mock
    svc.freebusy.return_value = freebusy_mock
    return svc


class TestCalendarBooking:

    def test_ac1_booking_succeeds_without_conference_data(self):
        """AC1: create_booking não lança exceção com service account Gmail pessoal."""
        mock_svc = _mock_service("evt-001")

        with patch("calendar_client._service", return_value=mock_svc), \
             patch("calendar_client._SA_JSON_RAW", "{}"), \
             patch("calendar_client.CALENDAR_ID", "primary"):

            import calendar_client
            event_id, meet_link = calendar_client.create_booking(
                name="João Silva",
                email="joao@exemplo.com",
                phone="5511999990001",
                start_iso="2026-04-22T12:00:00+00:00",
                end_iso="2026-04-22T12:30:00+00:00",
                pain="Emite NF manualmente",
            )

        assert event_id == "evt-001"

    def test_ac2_meet_link_is_none(self):
        """AC2: meet_link retornado é None quando sem conferenceData."""
        mock_svc = _mock_service("evt-002")

        with patch("calendar_client._service", return_value=mock_svc), \
             patch("calendar_client._SA_JSON_RAW", "{}"), \
             patch("calendar_client.CALENDAR_ID", "primary"):

            import calendar_client
            _, meet_link = calendar_client.create_booking(
                name="Maria",
                email="maria@exemplo.com",
                phone="5511999990002",
                start_iso="2026-04-22T14:00:00+00:00",
                end_iso="2026-04-22T14:30:00+00:00",
            )

        assert meet_link is None

    def test_ac5_event_has_lead_info_in_description(self):
        """AC5: evento criado contém nome, telefone e dor do lead na descrição."""
        captured_body = {}

        def fake_insert(calendarId, body, **kwargs):
            captured_body.update(body)
            result = MagicMock()
            result.execute.return_value = {"id": "evt-003", "conferenceData": {}}
            return result

        mock_svc = MagicMock()
        mock_svc.events.return_value.insert = fake_insert

        with patch("calendar_client._service", return_value=mock_svc), \
             patch("calendar_client._SA_JSON_RAW", "{}"), \
             patch("calendar_client.CALENDAR_ID", "primary"):

            import calendar_client
            calendar_client.create_booking(
                name="Pedro Santos",
                email="pedro@exemplo.com",
                phone="5511999990003",
                start_iso="2026-04-23T09:00:00+00:00",
                end_iso="2026-04-23T09:30:00+00:00",
                pain="Suporte manual todo dia",
            )

        assert "Pedro Santos" in captured_body["description"]
        assert "5511999990003" in captured_body["description"]
        assert "Suporte manual todo dia" in captured_body["description"]
        assert "conferenceData" not in captured_body, "conferenceData não deve existir no body"
