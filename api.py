import json
import pytest
import requests
from conftest import get_api_key
from settings import valid_email, valid_password
from requests_toolbelt.multipart.encoder import MultipartEncoder


class PetFriends:
    """Библиотека методов для тестирования API платформы PetFriends."""

    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru"

    def create_pet_simple(self, auth_key, name: str, animal_type: str, age) -> json:
        """Метод позволяет разместить на сервере базовую информацию о питомце без фотографии.
        Возвращает код состояния ответа на запрос и данные добавленного питомца в формате JSON."""

        headers = {'auth_key': auth_key}
        data = {'name': name, 'animal_type': animal_type, 'age': age}
        response = requests.post(self.base_url + '/api/create_pet_simple', headers=headers, data=data)
        status = response.status_code
        result = ""
        try:
            result = response.json()
        except json.decoder.JSONDecodeError:
            result = response.text
        return status, result

    def create_pet_wth_foto(self, auth_key, name, animal_type, age, pet_photo):
        """Метод позволяет разместить на сервере базовую информацию о питомце, а также его фотографию.
        Возвращает код состояния ответа на запрос и данные добавленного питомца в формате JSON."""

        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })
        headers = {'auth_key': auth_key, 'Content-Type': data.content_type}

        response = requests.post(self.base_url + '/api/pets', headers=headers, data=data)

        status = response.status_code
        result = ""
        try:
            result = response.json()
        except json.decoder.JSONDecodeError:
            result = response.text
        return status, result

    def get_all_pets(self, auth_key, filters: str):
        """"""

        headers = {'auth_key': auth_key}
        filters = {'filter': filters}

        response = requests.get(self.base_url + '/api/pets',
                                headers=headers, params=filters)

        status = response.status_code
        result = ""
        try:
            result = response.json()
        except json.decoder.JSONDecodeError:
            result = response.text
        return status, result

    def delete_pet(self, auth_key, pet_id):
        """Метод позволяет удалить на сервере карточку питомца на основании id-номера. Возвращает код состояния
        ответа."""

        headers = {'auth_key': auth_key}

        response = requests.delete(self.base_url + '/api/pets/' + pet_id, headers=headers)

        status = response.status_code

        return status

    def delete_all_my_pets(self, auth_key):
        """Метод позволяет удалить на сервере все карточки питомцев, размещенные пользователем в его профиле.
        Возвращает код состояния ответа."""

        headers = {'auth_key': auth_key}
        filters = {'filter': 'my_pets'}
        my_pets = requests.get(self.base_url + '/api/pets', headers=headers, params=filters)
        result = my_pets.json()

        while len(result['pets']) > 0:
            delete_pets = requests.delete(self.base_url + '/api/pets/' + result['pets'][0]['id'], headers=headers)
            my_pets = requests.get(self.base_url + '/api/pets', headers=headers, params=filters)
            status = delete_pets.status_code
            result = my_pets.json()

        return status, result
