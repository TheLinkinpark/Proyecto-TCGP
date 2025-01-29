import random
import json

class Pokemon:
    nombre: str
    tipo: str
    rareza: str
    num_pokedex: int

    def __init__(self, nombre, tipo, rareza, num_pokedex) -> None:
        self.nombre = nombre
        self.tipo = tipo
        self.rareza = rareza
        self.num_pokedex = num_pokedex


    def __str__(self) -> str: # Devuelve la carta Pokémon dibujada
        return f"{'\u2500' * 15}\n CARTA POKÉMON\n{'\u2500' * (len(self.nombre) + 4)}\n| {self.nombre} |\n{'\u2500' * (len(self.nombre) + 4)}\n Tipo: {self.tipo}\n Rareza: {self.rareza}\n{'\u2500' * 15}"





with open('lista_pokemon.json', 'r') as prueba:
    pokemons = json.load(prueba)


clave_raices = random.choice(list(pokemons["sobre_raices"]))
valor_raices = pokemons["sobre_raices"][clave_raices]


poke = Pokemon(clave_raices, valor_raices["tipo"], valor_raices["rareza"], valor_raices["num_pokedex"])
print(poke)

