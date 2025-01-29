import json
with open('lista_pokemon.json', 'r') as prueba:
    pokemons = json.load(prueba)

print(pokemons["sobre_raices"]["Bulbasaur"])