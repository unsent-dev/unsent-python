from unsent.legacy_types import Email
import requests_mock

def test_send_email(client):
    with requests_mock.Mocker() as m:
        m.post("https://api.unsent.dev/v1/emails", json={"emailId": "email_123"}, status_code=200)
        
        response, error = client.emails.send({
            "to": "test@example.com",
            "from": "sender@example.com",
            "subject": "Test Email",
            "text": "Hello World"
        })
        
        assert error is None
        assert response["emailId"] == "email_123"
        assert m.last_request.json()["to"] == "test@example.com"

def test_get_email(client):
    with requests_mock.Mocker() as m:
        m.get("https://api.unsent.dev/v1/emails/email_123", json={"id": "email_123", "subject": "Test"}, status_code=200)
        
        response, error = client.emails.get("email_123")
        
        assert error is None
        assert response["id"] == "email_123"

def test_batch_emails(client):
    with requests_mock.Mocker() as m:
        m.post("https://api.unsent.dev/v1/emails/batch", json={"data": [{"emailId": "1"}, {"emailId": "2"}]}, status_code=200)
        
        response, error = client.emails.batch([
            {"to": "u1@example.com", "from": "s@example.com"},
            {"to": "u2@example.com", "from": "s@example.com"}
        ])
        
        assert error is None
        assert len(response["data"]) == 2

def test_list_emails(client):
    with requests_mock.Mocker() as m:
        m.get("https://api.unsent.dev/v1/emails?page=1&limit=10", json={"data": [{"id": "email_1"}], "count": 1}, status_code=200)
        
        response, error = client.emails.list(page=1, limit=10)
        
        assert error is None
        assert response["count"] == 1
        assert len(response["data"]) == 1

def test_list_emails_with_filters(client):
    with requests_mock.Mocker() as m:
        m.get("https://api.unsent.dev/v1/emails?startDate=2024-01-01&domainId=domain_1", json={"data": [], "count": 0}, status_code=200)
        
        response, error = client.emails.list(start_date="2024-01-01", domain_id="domain_1")
        
        assert error is None
        assert response["count"] == 0

def test_get_complaints(client):
    with requests_mock.Mocker() as m:
        m.get("https://api.unsent.dev/v1/emails/complaints?page=1&limit=20", json={"data": [{"email": "complaint@example.com"}], "count": 1}, status_code=200)
        
        response, error = client.emails.get_complaints(page=1, limit=20)
        
        assert error is None
        assert response["count"] == 1

def test_get_bounces(client):
    with requests_mock.Mocker() as m:
        m.get("https://api.unsent.dev/v1/emails/bounces?page=1&limit=20", json={"data": [{"email": "bounce@example.com"}], "count": 1}, status_code=200)
        
        response, error = client.emails.get_bounces(page=1, limit=20)
        
        assert error is None
        assert response["count"] == 1

def test_get_unsubscribes(client):
    with requests_mock.Mocker() as m:
        m.get("https://api.unsent.dev/v1/emails/unsubscribes", json={"data": [{"email": "unsub@example.com"}], "count": 1}, status_code=200)
        
        response, error = client.emails.get_unsubscribes()
        
        assert error is None
        assert response["count"] == 1

def test_get_events(client):
    with requests_mock.Mocker() as m:
        m.get("https://api.unsent.dev/v1/emails/email_123/events?page=1", json={"data": []}, status_code=200)
        
        response, error = client.emails.get_events("email_123", page=1)
        
        assert error is None
        assert response == {"data": []}
