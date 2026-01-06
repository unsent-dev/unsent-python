from unsent.unsent import unsent

def test_client_init_with_key():
    client = unsent(key="test_key")
    assert client.key == "test_key"
    assert client.url == "https://api.unsent.dev/v1"

def test_client_resources_init(client):
    assert client.emails
    assert client.contacts
    assert client.contact_books
    assert client.domains
    assert client.campaigns
    assert client.templates
    assert client.webhooks
    assert client.analytics
    assert client.suppressions
    assert client.api_keys
    assert client.settings
