import requests_mock

def test_list_templates(client):
    with requests_mock.Mocker() as m:
        m.get("https://api.unsent.dev/v1/templates", json=[{"id": "tpl1", "name": "Template 1"}], status_code=200)
        
        response, error = client.templates.list()
        
        assert error is None
        assert len(response) == 1
        assert response[0]["id"] == "tpl1"

def test_create_template(client):
    with requests_mock.Mocker() as m:
        m.post("https://api.unsent.dev/v1/templates", json={"id": "tpl2", "name": "New Template"}, status_code=200)
        
        response, error = client.templates.create({"name": "New Template"})
        
        assert error is None
        assert response["id"] == "tpl2"

def test_get_template(client):
    with requests_mock.Mocker() as m:
        m.get("https://api.unsent.dev/v1/templates/tpl1", json={"id": "tpl1", "name": "Template 1"}, status_code=200)
        
        response, error = client.templates.get("tpl1")
        
        assert error is None
        assert response["id"] == "tpl1"
