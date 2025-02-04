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
        return f"{'\u2500' * 15}\n CARTA POKÉMON\n{'\u2500' * (len(self.nombre) + 4)}\n| {self.nombre} |\n{'\u2500' * (len(self.nombre) + 4)}\n Tipo: {self.tipo}\n Rareza: {self.rareza}\n Pokédex: nº{self.num_pokedex}\n {'\u2500' * 15}"



