import requests_mock

def test_list_api_keys(client):
    with requests_mock.Mocker() as m:
        m.get("https://api.unsent.dev/v1/api-keys", json=[{"id": "key1", "name": "Key 1"}], status_code=200)
        
        response, error = client.api_keys.list()
        
        assert error is None
        assert len(response) == 1
        assert response[0]["name"] == "Key 1"

def test_create_api_key(client):
    with requests_mock.Mocker() as m:
        m.post("https://api.unsent.dev/v1/api-keys", json={"id": "key2", "name": "Key 2", "key": "un_xxx"}, status_code=200)
        
        response, error = client.api_keys.create({"name": "Key 2"})
        
        assert error is None
        assert response["key"] == "un_xxx"

def test_revoke_api_key(client):
    with requests_mock.Mocker() as m:
        m.delete("https://api.unsent.dev/v1/api-keys/key1", json={"success": True}, status_code=200)
        
        response, error = client.api_keys.revoke("key1")
        
        assert error is None
        assert response["success"] is True
