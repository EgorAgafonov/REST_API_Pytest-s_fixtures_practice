import json
import requests
import pytest


class CatFacts:
    """Класс-клиент для отправки запросов к API сервису https://catfact.ninja в рамках тестирования"""

    def __init__(self):
        self.base_url = 'https://catfact.ninja'

    def get_list_of_cats(self, limit: str) -> list:
        """"""
        query = {'limit': limit}
        response = requests.get(self.base_url + '/breeds', params=query)


