from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password
import os
import requests
import pytest
import json
from conftest import *
import time

pf = PetFriends()


def test_getAllPets(get_api_key):
    """Позитивный тест проверки запроса размещенных пользователем карточек питомцев. Для обязательной, предварительной
    авторизации пользователя на сайте перед размещением карточки c помощью библиотеки Pytest сначала инициализируется
    функция-фикстура get_api_key. В случае положительной авторизации на сайте (в фикстуре get_api_key реализована
    тестовая проверка на предмет валидации пользователя на сайте) с помощью библиотеки requests, выполняется get-запрос
    на предоставление всех карточек питомцев, созданных пользователем. В параметрах запроса передаётся необходимое
    значение фильтра - 'my_pets'. Валидация теста считается успешной в случае, если статус ответа сервера равен 200, а
    количество полученных карточек питомцев (элементов списка в json-словаре) больше 0. Использование фикстуры
    get_api_key позволяет избежать многострочного кода в тестовом наборе(коллекции), делает код более лаконичным."""

    status, result = pf.get_all_pets(auth_key=get_api_key, filters='my_pets')

    assert status == 200, 'Запрос выполнен неуспешно'
    assert len(result.get('pets')) > 0, 'Количество питомцев не соответствует ожиданиям'


def test_create_pet_simple(get_api_key):
    """Позитивный тест проверки размещения пользователем карточки питомца без фотографии. Используется фикстура
    get_api_key, как и в предыдущем тесте. В случае положительной авторизации на сайте с помощью модуля api.py с классом
    атрибутов и методов PetFriends, выполняется post-запрос на размещение карточки. Валидация теста считается успешной
    в случае если статус ответа сервера равен 200, а передаваемое в запросе кличка питомца содержится в json-ответе
    сервера."""

    status, result = pf.create_pet_simple(auth_key=get_api_key, name='Richard', animal_type='bobcat', age=1.5)

    assert status == 200, 'Запрос выполнен неуспешно'
    assert result['name'] == 'Richard', 'Запрос неверный, карточка питомца не создана'


def test_create_pet_wth_photo(get_api_key, pet_photo='images/cat1.jpg'):
    """Позитивный тест проверки размещения пользователем карточки питомца с фотографией. Используется фикстура
    get_api_key, как и в предыдущем тесте. В случае положительной авторизации на сайте с помощью модуля api.py с классом
    атрибутов и методов PetFriends, выполняется post-запрос на размещение карточки с фото. Валидация теста считается
    успешной в случае, если статус ответа сервера равен 200, а возвращаемое в ответе сервера значение ключа 'pet_photo'
    не пустое (т.е. содержит байтовое представление размещенного фото питомца)."""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    status, result = pf.create_pet_wth_foto(auth_key=get_api_key, name='Tomas', animal_type='british-lazy', age='2',
                                            pet_photo=pet_photo)

    assert status == 200, 'Запрос выполнен неуспешно'
    assert result['pet_photo'] != '', 'Запрос неверный, карточка питомца с фото не создана'


# def test_delete_pet_id(get_api_key):
#     """"""
#     list_of_pets = pf.
#     status = pf.delete_pet(auth_key=get_api_key, pet_id='')


