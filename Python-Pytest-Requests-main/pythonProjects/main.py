import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'fb38190bae6856e0c2f757ca339893c8'
HEADER = { 'Content-Type' : 'application/json',  'trainer_token' : TOKEN}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_newname = {
    "pokemon_id": "125655",
    "name": "Lila"
}

body_pokeball = {
    "pokemon_id": "125655"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

response_newname = requests.patch(url = f'{URL}/pokemons', headers = HEADER, json = body_newname)
print(response_newname.text)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)



