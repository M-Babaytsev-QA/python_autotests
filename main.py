import requests

URL = 'https://api.pokemonbattle.ru/v2'

TOKEN = '842ebca1ccc9fcbe07a9c22a6238618e'

HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}

body_generate = {
    "name" : "Mariarti",
    "photo_id" : -1
}

response_generate = requests.post (url = f'{URL}/pokemons' , headers = HEADER, json = body_generate)

print(response_generate.text)

pokemon_id = response_generate.json()['id']
print(pokemon_id)

body_new_name = {
    "pokemon_id": pokemon_id,
    "name": "Durimar",
    "photo_id": -1
}

response_new_name = requests.put (url = f'{URL}/pokemons' , headers = HEADER, json = body_new_name)
print(response_new_name.text)

body_pokeball = {
    "pokemon_id": pokemon_id
}

response_pokeball = requests.post (url= f'{URL}/trainers/add_pokeball' , headers = HEADER, json = body_pokeball)
print(response_pokeball.text)