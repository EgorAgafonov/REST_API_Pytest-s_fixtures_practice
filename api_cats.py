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

    def get_fact_of_cats(self, max_length):
        """Метод для получения случайного факта из жизни кошек. Максимальная длинна строки с фактом ограничена
        параметром query (аргумент max_length)."""

        query = {'max_length': max_length}
        response = requests.get(self.base_url + '/fact', params=query)
        status = response.status_code
        result = ""
        try:
            result = response.json()
        except json.decoder.JSONDecodeError:
            result = response.text

        return status, result

    def get_list_of_facts(self, max_length, limit):
        """Метод для получения случайного факта из жизни кошек. Максимальная длинна строки с фактом ограничена
        параметром query (аргумент max_length)."""

        query = {'max_length': max_length, 'limit': limit}
        response = requests.get(self.base_url + '/facts', params=query)
        status = response.status_code
        result = ""
        try:
            result = response.json()
        except json.decoder.JSONDecodeError:
            result = response.text

        return status, result



