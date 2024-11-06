import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'fb38190bae6856e0c2f757ca339893c8'
HEADER = { 'Content-Type' : 'application/json',  'trainer_token' : TOKEN}
TRAINER_ID = 8455

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainers_id' : TRAINER_ID})
    assert response.status_code == 200