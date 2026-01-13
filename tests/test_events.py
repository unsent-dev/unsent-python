import requests_mock

def test_events_list(client):
    with requests_mock.Mocker() as m:
        m.get("https://api.unsent.dev/v1/events", json={"data": []}, status_code=200)
        
        response, error = client.events.list()
        
        assert error is None
        assert response == {"data": []}

def test_events_list_with_params(client):
    with requests_mock.Mocker() as m:
        m.get("https://api.unsent.dev/v1/events?page=1&limit=10", json={"data": []}, status_code=200)
        
        response, error = client.events.list(page=1, limit=10)
        
        assert error is None
