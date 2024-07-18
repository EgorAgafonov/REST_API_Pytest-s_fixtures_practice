import json
import requests
import pytest


class CatFacts:
    """Класс-клиент для отправки запросов к API сервису https://catfact.ninja в рамках тестирования"""

    def __init__(self):
        self.base_url = 'https://catfact.ninja'

    def get_list_of_cats_breeds(self, limit):
        """Метод для получения списка пород кошек. Количество пород в списке определяется пользователем с помощью
        параметра query (аргумент limit)."""

        query = {'limit': limit}
        response = requests.get(self.base_url + '/breeds', params=query)

        status = response.status_code
        result = ""
        try:
            result = response.json()
        except json.decoder.JSONDecodeError:
            result = response.text

        return status, result

