import pytest
import requests
from datetime import *
import json
from settings import *


@pytest.fixture()
def get_api_key(base_url="https://petfriends.skillfactory.ru/", email=valid_email, password=valid_password) -> json:

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


# @pytest.fixture(autouse=True)
# def time_delta():
#     start_time = datetime.now()
#     yield
#     end_time = datetime.now()
#     print(f"\nВремя прохождения теста: {end_time - start_time}")
