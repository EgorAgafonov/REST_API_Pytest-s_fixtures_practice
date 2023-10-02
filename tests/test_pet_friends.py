from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password
import os
import requests
import pytest
import json
from conftest import *
import time

pf = PetFriends()


def test_getAllPets(get_key):
    response = requests.get(url='https://petfriends.skillfactory.ru/api/pets',
                            headers={"Cookie": get_key}, params={'filter': 'my_pets'})
    assert response.status_code == 200, 'Запрос выполнен неуспешно'
    assert len(response.json().get('pets')) == 0, 'Количество питомцев не соответствует ожиданиям'


def test_create_pet_simple(get_key):
    data = {'name': "Барон", 'animal_type': 'персидская', 'age': '10'}
    response = requests.post(url='https://petfriends.skillfactory.ru/' + '/api/create_pet_simple',
                             headers={'Cookie': get_key}, data=data)
    status = response.status_code
    result = response.text

    assert status == 200
    print(result.find('Барон'))
