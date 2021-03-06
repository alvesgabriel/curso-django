import pytest
from django.urls import reverse
from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client, db):
    return client.get(reverse("base:home"))


def test_home_status(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, "<title>Python Pro - Home</title>")


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("base:home")}">Python Pro</a>')


def test_email_link(resp):
    assert_contains(resp, 'href="mailto:ramalho@python.pro.br"')


def test_home_body(resp):
    assert_contains(resp, "Curso de Python com Luciano Ramalho")
