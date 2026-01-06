import requests_mock

def test_list_suppressions(client):
    with requests_mock.Mocker() as m:
        m.get("https://api.unsent.dev/v1/suppressions", json=[{"id": "sup1", "email": "bounced@example.com"}], status_code=200)
        
        response, error = client.suppressions.list()
        
        assert error is None
        assert len(response) == 1
        assert response[0]["email"] == "bounced@example.com"

def test_list_suppressions_with_reason(client):
    with requests_mock.Mocker() as m:
        m.get("https://api.unsent.dev/v1/suppressions?reason=HARD_BOUNCE&page=1", json=[{"id": "sup1", "email": "bounced@example.com", "reason": "HARD_BOUNCE"}], status_code=200)
        
        response, error = client.suppressions.list(reason="HARD_BOUNCE", page=1)
        
        assert error is None
        assert len(response) == 1
        assert response[0]["reason"] == "HARD_BOUNCE"

def test_add_suppression(client):
    with requests_mock.Mocker() as m:
        m.post("https://api.unsent.dev/v1/suppressions", json={"id": "sup2", "email": "spam@example.com"}, status_code=200)
        
        response, error = client.suppressions.add({"email": "spam@example.com", "reason": "MANUAL"})
        
        assert error is None
        assert response["email"] == "spam@example.com"

def test_delete_suppression(client):
    with requests_mock.Mocker() as m:
        m.delete("https://api.unsent.dev/v1/suppressions/email/test@example.com", json={"success": True}, status_code=200)
        
        response, error = client.suppressions.delete("test@example.com")
        
        assert error is None
        assert response["success"] is True

