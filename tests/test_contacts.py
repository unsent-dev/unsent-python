import requests_mock

def test_list_contacts(client):
    with requests_mock.Mocker() as m:
        m.get("https://api.unsent.dev/v1/contactBooks/book1/contacts?page=1&limit=10", json={"data": [{"id": "c1"}], "count": 1}, status_code=200)
        
        response, error = client.contacts.list("book1", page=1, limit=10)
        
        assert error is None
        assert response["count"] == 1

def test_create_contact(client):
    with requests_mock.Mocker() as m:
        m.post("https://api.unsent.dev/v1/contactBooks/book1/contacts", json={"contactId": "c1"}, status_code=200)
        
        response, error = client.contacts.create("book1", {
            "email": "test@example.com",
            "firstName": "Test",
            "lastName": "User"
        })
        
        assert error is None
        assert response["contactId"] == "c1"

def test_get_contact(client):
    with requests_mock.Mocker() as m:
        m.get("https://api.unsent.dev/v1/contactBooks/book1/contacts/c1", json={"id": "c1", "email": "test@example.com"}, status_code=200)
        
        response, error = client.contacts.get("book1", "c1")
        
        assert error is None
        assert response["id"] == "c1"

def test_delete_contact(client):
    with requests_mock.Mocker() as m:
        m.delete("https://api.unsent.dev/v1/contactBooks/book1/contacts/c1", json={"success": True}, status_code=200)
        
        response, error = client.contacts.delete("book1", "c1")
        
        assert error is None
        assert response["success"] is True

