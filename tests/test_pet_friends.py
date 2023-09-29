from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password
import os
import pytest
import time

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """Проверяем что запрос API ключа возвращает статус 200 и в результате содержится слово key."""

    status, result = pf.get_api_key(email, password)

    assert status == 200
    assert 'key' in result
