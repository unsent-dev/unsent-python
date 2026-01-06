import requests_mock

def test_get_settings(client):
    with requests_mock.Mocker() as m:
        m.get("https://api.unsent.dev/v1/settings", json={"teamId": "team1", "plan": "pro"}, status_code=200)
        
        response, error = client.settings.get()
        
        assert error is None
        assert response["teamId"] == "team1"
        assert response["plan"] == "pro"
