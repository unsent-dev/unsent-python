"""Tests for webhooks resource.

Note: These tests are preparatory for the webhooks feature which is currently
under development in the API. They ensure the SDK structure is ready when the
feature becomes available.
"""
import requests_mock

def test_list_webhooks(client):
    with requests_mock.Mocker() as m:
        m.get("https://api.unsent.dev/v1/webhooks", json=[{"id": "wh1", "url": "https://example.com/hook"}], status_code=200)
        
        response, error = client.webhooks.list()
        
        assert error is None
        assert len(response) == 1
        assert response[0]["id"] == "wh1"

def test_create_webhook(client):
    with requests_mock.Mocker() as m:
        m.post("https://api.unsent.dev/v1/webhooks", json={"id": "wh2", "url": "https://new.com/hook"}, status_code=200)
        
        response, error = client.webhooks.create({"url": "https://new.com/hook", "events": ["email.sent"]})
        
        assert error is None
        assert response["id"] == "wh2"

def test_delete_webhook(client):
    with requests_mock.Mocker() as m:
        m.delete("https://api.unsent.dev/v1/webhooks/wh1", json={"success": True}, status_code=200)
        
        response, error = client.webhooks.delete("wh1")
        
        assert error is None
        assert response["success"] is True

def test_test_webhook(client):
    with requests_mock.Mocker() as m:
        m.post("https://api.unsent.dev/v1/webhooks/wh1/test", json={"id": "call1", "status": 200}, status_code=200)
        
        response, error = client.webhooks.test("wh1")
        
        assert error is None
        assert response["id"] == "call1"
        assert response["status"] == 200
