"""
Harness — AC1..AC6 para admin lead reset endpoints (spec hermes-admin-reset.md)
Roda com: pytest tests/test_admin_reset.py -v
"""
import json
import os
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
from fastapi.testclient import TestClient

VALID_API_KEY = "test-secret-key"
TEST_PHONE = "5511999990077"


def _build_client(secret: str = VALID_API_KEY):
    with patch("main.WEBHOOK_SECRET", secret):
        import main
        return TestClient(main.app)


def _lead_json(phone: str, state: str = "HUMAN_HANDOFF") -> dict:
    return {
        "id": phone,
        "name": "Test Lead",
        "state": state,
        "messages": [],
        "messageCount": 5,
        "handoffSent": True,
        "pain": "test pain",
        "lastSeenAt": "2026-04-21T12:00:00+00:00",
    }


class TestAdminReset:

    def test_ac1_delete_existing_lead(self):
        """AC1: DELETE /admin/lead/{phone} com apikey válida → lead deletado, 200."""
        with tempfile.TemporaryDirectory() as tmpdir:
            lead_path = Path(tmpdir) / f"{TEST_PHONE}.json"
            lead_path.write_text(json.dumps(_lead_json(TEST_PHONE)))

            with patch("main.WEBHOOK_SECRET", VALID_API_KEY), \
                 patch("main.lead_mgr.store._path", return_value=lead_path):

                import main
                client = TestClient(main.app)
                resp = client.delete(
                    f"/admin/lead/{TEST_PHONE}",
                    headers={"apikey": VALID_API_KEY},
                )

        assert resp.status_code == 200
        data = resp.json()
        assert data["ok"] is True
        assert data["existed"] is True
        assert not lead_path.exists(), "Arquivo do lead deve ter sido deletado"

    def test_ac2_delete_with_invalid_apikey_returns_401(self):
        """AC2: DELETE com apikey errada → 401."""
        with patch("main.WEBHOOK_SECRET", VALID_API_KEY):
            import main
            client = TestClient(main.app)
            resp = client.delete(
                f"/admin/lead/{TEST_PHONE}",
                headers={"apikey": "wrong-key"},
            )

        assert resp.status_code == 401

    def test_ac3_delete_nonexistent_lead(self):
        """AC3: DELETE lead que não existe → 200, existed=False."""
        nonexistent = Path("/tmp/nonexistent_lead_99999.json")

        with patch("main.WEBHOOK_SECRET", VALID_API_KEY), \
             patch("main.lead_mgr.store._path", return_value=nonexistent):

            import main
            client = TestClient(main.app)
            resp = client.delete(
                "/admin/lead/99999999999",
                headers={"apikey": VALID_API_KEY},
            )

        assert resp.status_code == 200
        data = resp.json()
        assert data["ok"] is True
        assert data["existed"] is False

    def test_ac4_get_existing_lead(self):
        """AC4: GET /admin/lead/{phone} com apikey → 200 com estado do lead."""
        from lead_memory import Lead

        mock_lead = MagicMock(spec=Lead)
        mock_lead.to_dict.return_value = {
            "id": TEST_PHONE,
            "name": "Test Lead",
            "state": "ANA_ACTIVE",
            "messageCount": 3,
            "messages": [{"role": "user", "content": "oi"}],
        }

        with patch("main.WEBHOOK_SECRET", VALID_API_KEY), \
             patch("main.lead_mgr.store.get", return_value=mock_lead):

            import main
            client = TestClient(main.app)
            resp = client.get(
                f"/admin/lead/{TEST_PHONE}",
                headers={"apikey": VALID_API_KEY},
            )

        assert resp.status_code == 200
        data = resp.json()
        assert data["state"] == "ANA_ACTIVE"
        assert data["messages"] == [], "Histórico de mensagens nunca deve ser exposto via admin"

    def test_ac5_get_nonexistent_lead_returns_404(self):
        """AC5: GET lead que não existe → 404."""
        with patch("main.WEBHOOK_SECRET", VALID_API_KEY), \
             patch("main.lead_mgr.store.get", return_value=None):

            import main
            client = TestClient(main.app)
            resp = client.get(
                "/admin/lead/99999999999",
                headers={"apikey": VALID_API_KEY},
            )

        assert resp.status_code == 404

    def test_ac6_list_all_leads(self):
        """AC6: GET /admin/leads → lista todos os leads com estado."""
        with tempfile.TemporaryDirectory() as tmpdir:
            data = [
                ("5511111111111", "VITOR_ACTIVE"),
                ("5511222222222", "ANA_ACTIVE"),
            ]
            for phone, state in data:
                (Path(tmpdir) / f"{phone}.json").write_text(
                    json.dumps(_lead_json(phone, state))
                )

            sentinel_path = Path(tmpdir) / "x.json"

            with patch("main.WEBHOOK_SECRET", VALID_API_KEY), \
                 patch("main.lead_mgr.store._path", return_value=sentinel_path):

                import main
                client = TestClient(main.app)
                resp = client.get("/admin/leads", headers={"apikey": VALID_API_KEY})

        assert resp.status_code == 200
        leads = resp.json()
        assert isinstance(leads, list)
        assert len(leads) == 2
        states = {l["state"] for l in leads}
        assert "VITOR_ACTIVE" in states
        assert "ANA_ACTIVE" in states
