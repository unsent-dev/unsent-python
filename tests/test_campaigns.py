import requests_mock

def test_list_campaigns(client):
    with requests_mock.Mocker() as m:
        m.get("https://api.unsent.dev/v1/campaigns", json=[{"id": "cmp1", "name": "Campaign 1"}], status_code=200)
        
        response, error = client.campaigns.list()
        
        assert error is None
        assert len(response) == 1
        assert response[0]["id"] == "cmp1"

def test_create_campaign(client):
    with requests_mock.Mocker() as m:
        m.post("https://api.unsent.dev/v1/campaigns", json={"id": "cmp2", "name": "New Campaign"}, status_code=200)
        
        response, error = client.campaigns.create({
            "name": "New Campaign",
            "from": "sender@example.com",
            "subject": "Hello",
            "contactBookId": "book1"
        })
        
        assert error is None
        assert response["id"] == "cmp2"

def test_schedule_campaign(client):
    with requests_mock.Mocker() as m:
        m.post("https://api.unsent.dev/v1/campaigns/cmp1/schedule", json={"success": True}, status_code=200)
        
        response, error = client.campaigns.schedule("cmp1", {"sendNow": True})
        
        assert error is None
        assert response["success"] is True
