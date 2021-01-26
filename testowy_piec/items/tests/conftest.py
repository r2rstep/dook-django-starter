import pytest

from testowy_piec.items.models import Item
from testowy_piec.items.tests.factories import ItemFactory


@pytest.fixture
def item() -> Item:
    return ItemFactory()
