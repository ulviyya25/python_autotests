"""
создать покемона

"""



# import requests

URL = 'https://api.pokemonbattle.me:9104'

HEADERS = {
    'Content-Type': 'application/json',
    'trainer_token': '275dd88fc1ef33b3a8aae5fda7a556cd'
}

body = {
    "name": "Pups",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

# response = requests.post(url=f'{URL}/pokemons', json=body, headers=HEADERS)

# Выводим статус код и текст ответа
# print(response.status_code)
# print(response.text)

"""
изменить имя покемона

"""


# import requests

URL = 'https://api.pokemonbattle.me:9104'


HEADERS = {
    'Content-Type': 'application/json',
    'trainer_token': '275dd88fc1ef33b3a8aae5fda7a556cd'
}

body = {
    "pokemon_id": "28323",
    "name": "Gjkjlfds",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

# response = requests.put(url=f'{URL}/pokemons', json=body, headers=HEADERS)

# Выводим статус код и текст ответа
# print(response.status_code)
# print(response.text)
"""
добавить в покебол

"""
import requests

URL = 'https://api.pokemonbattle.me:9104'


HEADERS = {
    'Content-Type': 'application/json',
    'trainer_token': '275dd88fc1ef33b3a8aae5fda7a556cd'
}

body = {
    "pokemon_id": "28323"
}

response = requests.post(url=f'{URL}/trainers/add_pokeball', json=body, headers=HEADERS)

# Выводим статус код и текст ответа
print(response.status_code)
print(response.text)

