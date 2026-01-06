import requests_mock

def test_list_contact_books(client):
    with requests_mock.Mocker() as m:
        m.get("https://api.unsent.dev/v1/contactBooks", json=[{"id": "b1", "name": "Book 1"}], status_code=200)
        
        response, error = client.contact_books.list()
        
        assert error is None
        assert len(response) == 1
        assert response[0]["id"] == "b1"

def test_create_contact_book(client):
    with requests_mock.Mocker() as m:
        m.post("https://api.unsent.dev/v1/contactBooks", json={"id": "b2"}, status_code=200)
        
        response, error = client.contact_books.create({"name": "Book 2"})
        
        assert error is None
        assert response["id"] == "b2"

def test_delete_contact_book(client):
    with requests_mock.Mocker() as m:
        m.delete("https://api.unsent.dev/v1/contactBooks/b1", json={"success": True}, status_code=200)
        
        response, error = client.contact_books.delete("b1")
        
        assert error is None
        assert response["success"] is True
