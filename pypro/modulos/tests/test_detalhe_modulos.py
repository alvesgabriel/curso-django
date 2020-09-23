import pytest
from django.urls import reverse
from model_bakery import baker

from pypro.django_assertions import assert_contains
from pypro.modulos.models import Modulo


@pytest.fixture
def modulo(db):
    return baker.make(Modulo)


@pytest.fixture
def resp(client, modulo):
    return client.get(reverse("modulos:detalhe", kwargs={"slug": modulo.slug}))


def test_titulo_modulo(resp, modulo):
    assert_contains(resp, modulo.titulo)


def test_publico_modulo(resp, modulo):
    assert_contains(resp, modulo.publico)


def test_descricao_modulo(resp, modulo):
    assert_contains(resp, modulo.descricao)
