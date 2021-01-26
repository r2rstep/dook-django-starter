from django.urls import reverse
import pytest
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from testowy_piec.users.models import BaseUser


@pytest.fixture
def client() -> APIClient:
    yield APIClient()


@pytest.mark.django_db
def test_non_existing_user_cannot_login(client: APIClient):
    assert BaseUser.objects.count() == 0

    url = reverse('api:authentication:login')
    data = {
        'email': 'test@hacksoft.io',
        'password': 'hacksoft'
    }

    response = client.post(url, data)

    # {'detail': ErrorDetail(string='No active account found with the given credentials', code='no_active_account')}

    assert response.status_code == 401


@pytest.mark.django_db(transaction=True)
def test_existing_user_can_login_and_access_apis(client: APIClient, user: BaseUser):
    assert client.login(username=user.email, password='test')
    token = Token.objects.create(user=user)
    client.credentials(HTTP_AUTHORIZATION='JWT ' + token.key)

    url = reverse('api:authentication:me')
    data = {'email': user.email}
    response = client.get(url, data=data)

    assert response.status_code == 200
    """
    1. Create user
    2. Assert login is OK
    3. Call /api/auth/me
    4. Assert valid response
    """
