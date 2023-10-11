from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password
import os
import requests
import pytest
import json
from conftest import *
from pytest import *
import time
import sys


#
# pf = PetFriends()
#
#
# class TestClass_PetFriends:
#     """Коллекция авто-тестов для тестирования REST API сервиса платформы PetFriends. """
#
#     def test_create_pet_simple(self, get_api_key):
#         """Позитивный тест проверки размещения пользователем карточки питомца без фотографии. Для обязательной,
#         предварительной авторизации пользователя на сайте перед размещением карточки c помощью библиотеки Pytest
#         сначала инициализируется функция-фикстура get_api_key. В случае положительной авторизации на сайте (в
#         фикстуре get_api_key реализована тестовая проверка на предмет валидации пользователя на сайте),
#         с помощью модуля api.py с классом атрибутов и методов PetFriends выполняется post-запрос на размещение карточки
#         с данными питомца без фото. В случае положительной авторизации на сайте, с помощью модуля api.py с
#         классом атрибутов и методов PetFriends выполняется post-запрос на размещение карточки. Валидация теста
#         считается успешной в случае если статус ответа сервера равен 200, а передаваемое в запросе кличка питомца
#         содержится в json-ответе сервера."""
#
#         status, result = pf.create_pet_simple(auth_key=get_api_key, name='Richard', animal_type='bobcat', age=1.5)
#
#         assert status == 200, 'Запрос выполнен неуспешно'
#         assert result['name'] == 'Richard', 'Запрос неверный, карточка питомца не создана'
#
#     def test_create_pet_wth_photo(self, get_api_key, name='Tomas', animal_type='british-lazy', age='2',
#                                   pet_photo='images/cat2.jpg'):
#         """Позитивный тест проверки размещения пользователем карточки питомца с фотографией. Используется фикстура
#         get_api_key, как и в предыдущем тесте. В случае положительной авторизации на сайте, с помощью модуля api.py с
#         классом атрибутов и методов PetFriends выполняется post-запрос на размещение карточки с фото. Валидация теста
#         считается успешной в случае, если статус ответа сервера равен 200, а возвращаемое в ответе сервера значение
#         ключа 'pet_photo' не пустое (т.е. содержит байтовое представление размещенного фото питомца)."""
#
#         pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
#
#         status, result = pf.create_pet_wth_foto(auth_key=get_api_key, name=name, animal_type=animal_type, age=age,
#                                                 pet_photo=pet_photo)
#
#         assert status == 200, 'Запрос выполнен неуспешно'
#         assert result['pet_photo'] != '', 'Запрос неверный, карточка питомца с фото не создана'
#
#     def test_getAllPets(self, get_api_key):
#         """Позитивный тест проверки запроса размещенных пользователем карточек питомцев. Используется фикстура
#         get_api_key, как и в предыдущем тесте. В случае положительной авторизации на сайте, с помощью модуля api.py с
#         классом атрибутов и методов PetFriends выполняется get-запрос на предоставление всех карточек питомцев,
#         созданных пользователем. В параметрах запроса передаётся необходимое значение фильтра - 'my_pets'. Валидация
#         теста считается успешной в случае, если статус ответа сервера равен 200, а количество полученных карточек
#         питомцев (элементов списка в json-словаре) больше 0. Использование фикстуры get_api_key позволяет избежать
#         многострочного кода в тестовом наборе (коллекции), делает код более лаконичным."""
#
#         status, result = pf.get_all_pets(auth_key=get_api_key, filters='my_pets')
#
#         assert status == 200, 'Запрос выполнен неуспешно'
#         assert len(result.get('pets')) > 0, 'Количество питомцев не соответствует ожиданиям'
#
#     def test_delete_pet_id(self, get_api_key):
#         """Позитивный тест проверки удаления карточки питомца из списка питомцев пользователя. Используется фикстура
#         get_api_key, как и в предыдущем тесте. В случае положительной авторизации на сайте, с помощью модуля api.py с
#         классом атрибутов и методов PetFriends выполняется delete-запрос на удаление карточки питомца по id-номеру.
#         Валидация теста считается успешной в случае, если статус ответа сервера на запрос равен 200, а id-номер
#         удаляемого питомца (его карточка) отсутствует в повторном get-запросе списка всех питомцев пользователя."""
#
#         _, my_pets = pf.get_all_pets(auth_key=get_api_key, filters='my_pets')  # получаем список питомцев пользователя
#
#         if len(my_pets[
#                    'pets']) == 0:  # в случае, если у пользователя отсутствуют размещенные карточки питомцев, инициируем
#             # post-запрос на добавление в профиль пользователя  карточки питомца с фото.
#
#             pf.create_pet_wth_foto(auth_key=get_api_key, name='Charlie', animal_type='siamese', age='2',
#                                    pet_photo='images/cat2.jpg')
#             _, my_pets = pf.get_all_pets(auth_key=get_api_key,
#                                          filters='my_pets')  # повторно запрашиваем список питомцев
#             # пользователя.
#
#         pet_id = my_pets['pets'][0][
#             'id']  # получаем id-номер питомца из списка my_pets для осуществления delete-запроса.
#
#         status = pf.delete_pet(auth_key=get_api_key, pet_id=pet_id)  # удаляем карточку питомца по id-номеру и получаем
#         # статус ответа от сервера.
#
#         _, my_pets = pf.get_all_pets(auth_key=get_api_key, filters='my_pets')  # повторно запрашиваем список питомцев
#         # для проверки отсутствия удаленного питомца
#         # в списке пользователя
#         assert status == 200
#         assert pet_id not in my_pets.values()
#
#     # @pytest.mark.skip(reason='Метод запроса работает некорректно, выполнение теста отложено.')
#     # @pytest.mark.skipif(sys.version_info > (3, 9), reason=f'Тест требует python версии 3.9'
#     #                                                       f'или ниже, выполнение теста отложено.')
#     # @min_python_310_required
#     # @pytest.mark.xfail(sys.platform == 'win32', reason='Возможны сбои в работе и падение теста на платформе win32')
#     @pytest.mark.xfail(raises=UnboundLocalError, reason="В случае отсутствия карточки(чек) питомцев у пользователя"
#                                                         "результат будет равен XFAIL (нечего удалять - "
#                                                         "UnboundLocalError)!")
#     def test_delete_all_pets(self, get_api_key):
#         """Позитивный тест проверки удаления всех карточек питомцев из профиля пользователя. Используется фикстура
#         get_api_key, как и в предыдущем тесте. В случае положительной авторизации на сайте, с помощью модуля api.py с
#         классом атрибутов и методов PetFriends, выполняется delete-запрос на удаление карточки питомца по id-номеру.
#         Валидация теста считается успешной в случае, если статус ответа сервера на delete-запрос равен 200,
#         а возвращаемый сервером ответ на get-запрос с массивом размещенных пользователем питомцев является пустым(
#         ключ 'pets' содержит пустой список словарей)."""
#
#         status, result = pf.delete_all_my_pets(auth_key=get_api_key)
#
#         assert status == 200
#         assert result['pets'] == []


@pytest.mark.api
@pytest.mark.auth
def test_auth_api():
    pass


@pytest.mark.api
@pytest.mark.event
def test_event_api():
    pass


@pytest.mark.ui
@pytest.mark.auth
def test_auth_ui():
    pass


@pytest.mark.ui
@pytest.mark.event
def test_event_ui():
    pass
