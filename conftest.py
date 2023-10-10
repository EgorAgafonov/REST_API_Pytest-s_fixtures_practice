import sys

import pytest
import requests
from datetime import *
import json
from settings import *


@pytest.fixture(scope='class', autouse=True)
def duration_of_collection(request):
    start_time = datetime.now()
    print(f'\n1/3 START COLLECTION:\nНачало выполнения тестовой коллекции: {start_time} сек.')
    yield
    end_time = datetime.now()
    print(f'2/3 END COLLECTION:\nОкончание выполнения тестовой коллекции: {end_time} сек.')
    print(f"3/3 RESULT: Общая продолжительность всех тестов в коллекции {request.cls}: {end_time - start_time} сек.\n")


@pytest.fixture(scope='class', autouse=True)
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

    print(f'\n--- Запрос api-ключа успешно выполнен, пользователь авторизован. ---')
    return result['key']


@pytest.fixture(scope='function', autouse=True)
def duration_of_test(request):
    start_time = datetime.now()
    print(f'\n1)Начало выполнения тестовой функции: {start_time} сек.')
    yield
    end_time = datetime.now()
    print(f'2)Окончание выполнения тестовой функции: {end_time} сек.')
    print(f"    ВСЕГО продолжительность теста {request.function.__name__}: {end_time - start_time} сек.\n")


@pytest.fixture(scope='function', autouse=True)
def introspection_of_test(request):
    yield
    print(f'\n- Имя теста (тестируемой функции): {request.function.__name__}.')
    print(f'- Имя коллекции (тестового класса): {request.cls}.')
    print(f'- Имя фикстуры: {request.fixturename}.')
    print(f'- Область видимости фикстуры: {request.scope}.')
    print(f'- Относительный путь к тестовому модулю: {request.module.__name__}.')
    print(f'- Абсолютный путь к тестовому модулю: {request.fspath}.')
    if request.cls:
        return f"\n У теста(тестируемой функции) {request.function.__name__} есть коллекция (тестовый класс).\n"
    else:
        return f"\n У теста(тестируемой функции) {request.function.__name__} коллекция (тестовый класс) отсутствует.\n"


min_python_310_required = pytest.mark.skipif(sys.version_info > (3, 9), reason='Тест требует python версии 3.10 или '
                                                                               'выше.')



