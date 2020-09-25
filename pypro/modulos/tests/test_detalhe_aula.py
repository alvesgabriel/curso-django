import pytest
from django.urls import reverse
from model_bakery import baker

from pypro.django_assertions import assert_contains
from pypro.modulos.models import Modulo, Aula


@pytest.fixture
def modulo(db):
    return baker.make(Modulo)


@pytest.fixture
def aula(modulo):
    return baker.make(Aula, modulo=modulo)


@pytest.fixture
def resp(client, aula):
    return client.get(reverse("modulos:aula", kwargs={"slug": aula.slug}))


def test_titulo(resp, aula):
    assert_contains(resp, aula.titulo)


def test_vimeo(resp, aula):
    assert_contains(resp, aula.vimeo_id)
