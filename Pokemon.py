import random

class Pokemon:
    nombre: str
    tipo: str
    rareza: str
    #num_pokedex: int

    def __init__(self, nombre, tipo, rareza):
        self.nombre = nombre
        self.tipo = tipo
        self.rareza = rareza
        #self.num_pokedex = num_pokedex

    def __str__(self) -> str:
        return f"Nombre:\n\t{self.nombre}\nTipo:\n\t{self.tipo}\nRareza:\n\t{self.rareza}\nNúmero Pokédex:\n\t"
    

fuego = {
    "Charmander": "*",
    "Charmeleon": "**",
    "Charizard": "***"
}


clave_aleatoria_fuego = random.choice(list(fuego.keys()))
valor_asociado_fuego = fuego[clave_aleatoria_fuego]



pokemon_fuego = Pokemon(clave_aleatoria_fuego, "fuego", valor_asociado_fuego)
print(pokemon_fuego)

prueba_cartapkmn = f"******\n{pokemon_fuego.nombre}\n******"
print(prueba_cartapkmn)