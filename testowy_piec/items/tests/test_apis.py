from django.urls import reverse
from rest_framework.test import APIClient
import pytest


@pytest.fixture
def client() -> APIClient:
    yield APIClient()


@pytest.mark.django_db(transaction=True)
def test_post(client):
    url = reverse('api:items:items')
    data = {
        'name': 'Test Test',
        'prop': 666
    }

    response = client.post(f'{url}', data)

    assert response.status_code == 201
