import json
import pytest
import requests
from conftest import get_api_key
from settings import valid_email, valid_password
from requests_toolbelt.multipart.encoder import MultipartEncoder


class PetFriends:
    """Библиотека методов для тестирования API платформы PetFriends."""

    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru/"

    def create_pet_simple(self, auth_key, name: str, animal_type: str, age: float) -> json:
        """Метод отправляет на сервер базовую информацию о добавляемом питомце без фотографии.
        Возвращает код состояния ответа на запрос и данные добавленного питомца в формате JSON."""

        headers = {'auth_key': auth_key}
        data = {'name': name, 'animal_type': animal_type, 'age': age}
        res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
