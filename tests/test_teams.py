import requests_mock

def test_teams_list(client):
    with requests_mock.Mocker() as m:
        m.get("https://api.unsent.dev/v1/teams", json={"data": []}, status_code=200)
        
        response, error = client.teams.list()
        
        assert error is None
        assert response == {"data": []}

def test_teams_get(client):
    with requests_mock.Mocker() as m:
        m.get("https://api.unsent.dev/v1/team", json={"id": "team1", "name": "My Team"}, status_code=200)
        
        response, error = client.teams.get()
        
        assert error is None
        assert response["id"] == "team1"
        assert response["name"] == "My Team"
