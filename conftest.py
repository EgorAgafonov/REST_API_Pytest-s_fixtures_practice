import pytest
import requests
from datetime import *
import json
from settings import *


@pytest.fixture()
def get_api_key(base_url="https://petfriends.skillfactory.ru/", email=valid_email, password=valid_password) -> json:
    """Метод для авторизации на платформе PetFriends и получения auth-key-ключа для отправки запросов. Одновременно
    является и тестируемой функцией (каждый раз при вызове), и setup-фикстурой pytest для передачи в качестве аргумента
    в тестируемые функции (каждый запрос требует отправлять в заголовке auth_key). Функция возвращает строковое значение
    auth-key."""

    headers = {'email': email, 'password': password}
    res = requests.get(base_url + 'api/key', headers=headers)
    status = res.status_code
    result = ""
    try:
        result = res.json()
    except json.decoder.JSONDecodeError:
        result = res.text

    assert status == 200
    assert 'key' in result

    return result['key']


@pytest.fixture(scope='class')
def greeting():
    print('\nТестирование в классе начинается.')
    yield
    print(f'\nТестирование в классе окончено.')


@pytest.fixture(scope='function', autouse=True)
def duration_of_test(request):
    start_time = datetime.now()
    print(f'\n1/2 НАЧАЛО\nвыполнения тестовой функции: {start_time} сек.\n')
    yield
    end_time = datetime.now()
    print(f'2/2 ОКОНЧАНИЕ\nвыполнения тестовой функции: {end_time} сек.')
    print(f"    ИТОГО: Продолжительность теста {request.function.__name__}: {end_time - start_time} сек.")


@pytest.fixture(scope='function', autouse=True)
def introspection_of_test(request):
    yield
    print(f'\n- Имя фикстуры: {request.fixturename}.')
    print(f'- Область видимости фикстуры: {request.scope}.')
    print(f'- Имя тестируемой функции: {request.function.__name__}.')
    print(f'- Имя класса тестового набора: {request.cls}.')
    print(f'- Относительный путь к тестовому модулю: {request.module.__name__}.')
    print(f'- Абсолютный путь к тестовому модулю: {request.fspath}.\n')
    if request.cls:
        return f"\n У теста {request.function.__name__} класс есть\n"
    else:
        return f"\n У теста {request.function.__name__} класса нет\n"












