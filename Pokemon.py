import random


class Pokemon:
    nombre: str
    tipo: str
    rareza: str

    def __init__(self, nombre, tipo, rareza):
        self.nombre = nombre
        self.tipo = tipo
        self.rareza = rareza


    def __str__(self) -> str: # Devuelve la carta Pokémon dibujada
        return f"{'\u2500' * 15}\n CARTA POKÉMON\n{'\u2500' * (len(self.nombre) + 4)}\n| {self.nombre} |\n{'\u2500' * (len(self.nombre) + 4)}\n Tipo: {self.tipo}\n Rareza: {self.rareza}\n{'\u2500' * 15}"









    # Saco un Pokémon aleatorio de mi lista de Pokémons para cada tipo de sobre


