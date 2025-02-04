import json

with open("lista_pokemon.json", "r") as prueba:
    pokemons = json.load(prueba)



for pokemon in pokemons["sobre_raices"]:
    print(pokemons["sobre_raices"][pokemon]["num_pokedex"])

for pokemon in pokemons["sobre_llamas"]:
    print(pokemons["sobre_llamas"][pokemon]["num_pokedex"])

for pokemon in pokemons["sobre_marea"]:
    print(pokemons["sobre_marea"][pokemon]["num_pokedex"])