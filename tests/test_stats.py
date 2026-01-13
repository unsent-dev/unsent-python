import requests_mock

def test_stats_get(client):
    with requests_mock.Mocker() as m:
        m.get("https://api.unsent.dev/v1/stats", json={"data": "stats"}, status_code=200)
        
        response, error = client.stats.get()
        
        assert error is None
        assert response == {"data": "stats"}

def test_stats_get_with_params(client):
    with requests_mock.Mocker() as m:
        m.get("https://api.unsent.dev/v1/stats?startDate=2023-01-01", json={"data": "stats"}, status_code=200)
        
        response, error = client.stats.get(start_date="2023-01-01")
        
        assert error is None
