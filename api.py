import json
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder


class PetFriends:
    """Библиотека методов для тестирования API платформы PetFriends."""

    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru/"


    def get_key(self, email: str, password: str) -> json:
        """"""

        response = requests.post(self.base_url + '/api/key',
                                 headers={"email": email, "pass": password})
        assert response.status_code == 200, 'Запрос выполнен неуспешно'
        assert 'Cookie' in response.request.headers, 'В запросе не передан ключ авторизации'
        return response.request.headers.get('Cookie')