from collections import OrderedDict

from django.urls import reverse
from rest_framework.test import APIClient
import pytest

from .factories import ItemFactory


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


@pytest.mark.django_db(transaction=True)
def test_paginated_list(client):
    items = []
    for _ in range(0, 3):
        items.append(ItemFactory())

    url = reverse('api:items:items')
    expected_first_page_response = OrderedDict({
        'limit': 1,
        'offset': 0,
        'count': len(items),
        'next': f'http://testserver{url}?limit=1&offset=1',
        'previous': None,
        'results': [
            OrderedDict({
                'id': items[0].id,
                'name': items[0].name,
                'prop': items[0].prop,
            })
        ]
    })

    response = client.get(f'{url}?limit=1')
    assert response.status_code == 200
    assert response.data == expected_first_page_response

    response = client.get(response.data['next'])
    expected_next_page_response = OrderedDict({
        'limit': 1,
        'offset': 1,
        'count': len(items),
        'next': f'http://testserver{url}?limit=1&offset=2',
        'previous': f'http://testserver{url}?limit=1',
        'results': [
            OrderedDict({
                'id': items[1].id,
                'name': items[1].name,
                'prop': items[1].prop,
            })
        ]
    })
    assert response.status_code == 200
    assert response.data == expected_next_page_response


@pytest.mark.django_db(transaction=True)
def test_paginated_list(client):
    items = []
    for idx in range(0, 3):
        item = ItemFactory(prop=idx)
        items.append(item)

    url = reverse('api:items:items')
    expected_results = [OrderedDict({'id': items[1].id,
                                     'name': items[1].name,
                                     'prop': items[1].prop,
                                     })]

    response = client.get(f'{url}?prop={items[1].prop}')
    assert response.status_code == 200
    assert response.data['results'] == expected_results
