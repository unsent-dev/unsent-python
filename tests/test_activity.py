import requests_mock

def test_activity_list(client):
    with requests_mock.Mocker() as m:
        m.get("https://api.unsent.dev/v1/activity", json={"data": []}, status_code=200)
        
        response, error = client.activity.list()
        
        assert error is None
        assert response == {"data": []}

def test_activity_list_with_params(client):
    with requests_mock.Mocker() as m:
        m.get("https://api.unsent.dev/v1/activity?page=1", json={"data": []}, status_code=200)
        
        response, error = client.activity.list(page=1)
        
        assert error is None
