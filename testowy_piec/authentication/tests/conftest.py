import pytest

from testowy_piec.users.models import BaseUser
from .factories import UserFactory


@pytest.fixture
def user() -> BaseUser:
    return UserFactory()
