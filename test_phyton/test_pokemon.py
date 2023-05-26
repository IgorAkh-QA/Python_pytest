import requests
import pytest
# token = '724ac102e245eec3abae25ffaa0b0fa7'
def test_check_status_code():
  response = requests.get('https://pokemonbattle.me:9104/trainers')
  assert response.status_code == 200
def test_check_trainer_name():
  response = requests.get('https://pokemonbattle.me:9104/trainers', 
                          params = {"trainer_id" : 4573})
  assert response.json()['trainer_name'] == "Igor"
  
  