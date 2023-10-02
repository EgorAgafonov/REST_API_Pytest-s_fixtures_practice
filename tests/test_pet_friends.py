from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password
import os
import requests
import pytest
from conftest import *
import time

pf = PetFriends()


def test_getAllPets(get_key):
    response = requests.get(url='https://petfriends.skillfactory.ru/api/pets',
                            headers={"Cookie": get_key}, params={'filter': 'my_pets'})
    assert response.status_code == 200, 'Запрос выполнен неуспешно'
    assert len(response.json().get('pets')) == 0, 'Количество питомцев не соответствует ожиданиям'
