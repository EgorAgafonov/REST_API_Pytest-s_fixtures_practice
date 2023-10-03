from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password
import os
import requests
import pytest
import json
from conftest import *
import time

pf = PetFriends()


# def test_getAllPets(get_api_key):
#     response = requests.get(url='https://petfriends.skillfactory.ru' + '/api/pets',
#                             headers={'auth_key': get_api_key}, params={'filter': 'my_pets'})
#
#     assert response.status_code == 200, 'Запрос выполнен неуспешно'
#     assert len(response.json().get('pets')) > 0, 'Количество питомцев не соответствует ожиданиям'


def test_create_pet_simple(get_api_key):
    """Позитивный тест проверки размещения пользователем карточки питомца без фотографии. Для обязательной,
    предварительной авторизации пользователя на сайте перед размещением карточки c помощью библиотеки Pytest сначала
    инициализируется функция-фикстура get_api_key. В случае положительной авторизации на сайте (в фикстуре get_api_key
    реализована тестовая проверка на предмет валидации пользователя на сайте) с помощью модуля api.py с классом
    атрибутов и методов PetFriends, выполняется post-запрос на размещение карточки. Валидация теста считается успешной
    в случае если статус ответа сервера равен 200, а передаваемое в запросе кличка питомца содержится в json-ответе
    сервера. Использование фиктусры get_api_key позволяет избежать многострочного кода в тестовом наборе(коллекции),
    делает код более лаконичным."""

    status, result = pf.create_pet_simple(auth_key=get_api_key, name='Richard', animal_type='bobcat', age=1.6)

    assert status == 200, 'Запрос выполнен неуспешно'
    assert result['name'] == 'Richard', 'Запрос неверный, карточка питомца не создана'
