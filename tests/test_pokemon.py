import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'

TOKEN = '842ebca1ccc9fcbe07a9c22a6238618e'

HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}

TRAINER_ID = '12448'

def test_status_code_trainers():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_respons():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Mutabor'