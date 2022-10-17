from urllib import response
import requests
import pytest

def test_statuscode():
    response = requests.get('https://petstore.swagger.io/v2/pet/250')
    assert response.status_code == 200

def test_name_of_pet():
    response = requests.get('https://petstore.swagger.io/v2/pet/250')
    assert response.json()['name'] == 'NeverLatee'