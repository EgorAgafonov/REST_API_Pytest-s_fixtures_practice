from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password
import os
import requests
import pytest
import json
from conftest import *
import time

pf = PetFriends()




def test_getAllPets(get_api_key):
    response = requests.get(url='https://petfriends.skillfactory.ru' + '/api/pets',
                            headers={'auth_key': get_api_key}, params={'filter': 'my_pets'})

    assert response.status_code == 200, 'Запрос выполнен неуспешно'
    assert len(response.json().get('pets')) > 0, 'Количество питомцев не соответствует ожиданиям'



def test_create_pet_simple(get_api_key):

    status, result = pf.create_pet_simple(name='Charlie', animal_type='persian', age=7)


    assert status == 200, 'Запрос выполнен неуспешно'
    # assert result['name'] == 'Charlie', 'Запрос неверный, карточка питомца не создана'
