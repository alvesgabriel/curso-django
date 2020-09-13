from django.test import Client


def test_home_status(client: Client):
    resp = client.get("/")
    assert resp.status_code == 200


def test_home_body(client: Client):
    resp = client.get("/")
    assert "Olá Django".encode("utf-8") in resp.content
