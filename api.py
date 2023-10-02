import json

import pytest
import requests
from settings import valid_email, valid_password
from requests_toolbelt.multipart.encoder import MultipartEncoder


class PetFriends:
    """Библиотека методов для тестирования API платформы PetFriends."""

    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru/"

    def get_key(self):
        # переменные email и password нужно заменить своими учетными данными
        response = requests.post(url='https://petfriends.skillfactory.ru/login',
                                 data={"email": valid_email, "pass": valid_password})
        assert response.status_code == 200, 'Запрос выполнен неуспешно'
        assert 'Cookie' in response.request.headers, 'В запросе не передан ключ авторизации'
        return response.request.headers.get('Cookie')