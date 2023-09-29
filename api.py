import json
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder


class PetFriends:
    """Библиотека методов для тестирования API платформы PetFriends."""

    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru/"

    def get_api_key(self, email: str, password: str) -> json:
        """Метод выполняет запрос к API сервера и возвращает статус запроса, а также результат в формате
        JSON с уникальным ключом пользователя, найденного по указанным email и password."""

        headers = {'email': email, 'password': password}
        res = requests.get(self.base_url + 'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result