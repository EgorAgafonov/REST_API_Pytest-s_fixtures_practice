import pytest
import requests
from datetime import *
from settings import *


@pytest.fixture()
def some_data():
    return 42


@pytest.fixture(autouse=True)
def get_key():
    response = requests.post(url='https://petfriends.skillfactory.ru/login',
                             data={"email": valid_email, "pass": valid_password})
    assert response.status_code == 200, 'Запрос выполнен неуспешно'
    assert 'Cookie' in response.request.headers, 'В запросе не передан ключ авторизации'
    return response.request.headers.get('Cookie')


@pytest.fixture(autouse=True)
def time_delta():
    start_time = datetime.now()
    yield
    end_time = datetime.now()
    print(f"\nВремя прохождения теста: {end_time - start_time}")


