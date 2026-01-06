import requests_mock

def test_list_domains(client):
    with requests_mock.Mocker() as m:
        m.get("https://api.unsent.dev/v1/domains", json=[{"id": 1, "name": "example.com"}], status_code=200)
        
        response, error = client.domains.list()
        
        assert error is None
        assert len(response) == 1
        assert response[0]["name"] == "example.com"

def test_create_domain(client):
    with requests_mock.Mocker() as m:
        m.post("https://api.unsent.dev/v1/domains", json={"id": 2, "name": "new.com"}, status_code=200)
        
        response, error = client.domains.create({"name": "new.com", "region": "us-east-1"})
        
        assert error is None
        assert response["name"] == "new.com"

def test_verify_domain(client):
    with requests_mock.Mocker() as m:
        m.put("https://api.unsent.dev/v1/domains/1/verify", json={"message": "Verification started"}, status_code=200)
        
        response, error = client.domains.verify(1)
        
        assert error is None
        assert response["message"] == "Verification started"
