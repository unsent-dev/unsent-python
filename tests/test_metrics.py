import requests_mock

def test_metrics_get(client):
    with requests_mock.Mocker() as m:
        m.get("https://api.unsent.dev/v1/metrics", json={"data": "metrics"}, status_code=200)
        
        response, error = client.metrics.get()
        
        assert error is None
        assert response == {"data": "metrics"}

def test_metrics_get_with_params(client):
    with requests_mock.Mocker() as m:
        m.get("https://api.unsent.dev/v1/metrics?period=day", json={"data": "metrics"}, status_code=200)
        
        response, error = client.metrics.get(period="day")
        
        assert error is None
