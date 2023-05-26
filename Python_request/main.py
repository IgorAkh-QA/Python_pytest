import requests
#{'id': '4573', 'trainer_name': 'Igor', 'trainer_token': '724ac102e245eec3abae25ffaa0b0fa7'}
##https
#pokemonbattle.me:9104
#header в POST и PUT запросах: 
#Content-Type: application/json
token = '724ac102e245eec3abae25ffaa0b0fa7'

response = requests.post('https://pokemonbattle.me:9104/pokemons', headers = {'Content-Type' : 'application/json',
                                                                              'trainer_token': token},
                                                                              json = { 
                                                                                  "name": "Бугагаш",
                                                                                  "photo": "https://dolnikov.ru/pokemons/albums/001.png"
})                     
response = requests.put('https://pokemonbattle.me:9104/pokemons', headers = {'Content-Type' : 'application/json',
                                                                              'trainer_token': token},
                                                                              json = { 
                                                                                  "pokemon_id": "12125",
    "name": "Бигль",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
})        
print(response.text)