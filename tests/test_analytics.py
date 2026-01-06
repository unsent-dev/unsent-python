import requests_mock

def test_get_usage(client):
    with requests_mock.Mocker() as m:
        m.get("https://api.unsent.dev/v1/analytics/usage", json={"sent": 100, "limit": 1000}, status_code=200)
        
        response, error = client.analytics.get_usage()
        
        assert error is None
        assert response["sent"] == 100
        assert response["limit"] == 1000

def test_get_daily_stats(client):
    with requests_mock.Mocker() as m:
        m.get("https://api.unsent.dev/v1/analytics/daily-stats?startDate=2023-01-01&endDate=2023-01-31", json=[{"date": "2023-01-01", "sent": 10}], status_code=200)
        
        response, error = client.analytics.get_daily_stats("2023-01-01", "2023-01-31")
        
        assert error is None
        assert len(response) == 1
        assert response[0]["sent"] == 10

def test_get_domain_reputation(client):
    with requests_mock.Mocker() as m:
        m.get("https://api.unsent.dev/v1/analytics/domain-reputation?domainId=dom1", json={"domain": "example.com", "reputation": "high"}, status_code=200)
        
        response, error = client.analytics.get_domain_reputation("dom1")
        
        assert error is None
        assert response["reputation"] == "high"
