import random
from lista_pokemon import sobre_planta, sobre_fuego, sobre_agua

class Pokemon:
    nombre: str
    tipo: str
    rareza: str

    def __init__(self, nombre, tipo, rareza):
        self.nombre = nombre
        self.tipo = tipo
        self.rareza = rareza
    
    def carta_pokemon(self):
        return f"**************\n* {self.nombre} *\n**************"

    def __str__(self) -> str:
        return f"\nNombre: {self.nombre}\nTipo: {self.tipo}\nRareza: {self.rareza}\n"
    

clave_fuego = random.choice(list(sobre_fuego.keys()))
valor_fuego = sobre_fuego[clave_fuego]

clave_planta = random.choice(list(sobre_planta.keys()))
valor_planta = sobre_planta[clave_planta]

clave_agua = random.choice(list(sobre_agua.keys()))
valor_agua = sobre_agua[clave_agua]

# Saco un Pokémon aleatorio de mi lista de Pokémons para cada tipo de sobre
pokemon_fuego = Pokemon(clave_fuego, "fuego", valor_fuego)
pokemon_planta = Pokemon(clave_planta, "planta", valor_planta)
pokemon_agua = Pokemon(clave_agua, "agua", valor_agua)

print(pokemon_planta)
print(pokemon_fuego)
print(pokemon_agua)

#print(pokemon_fuego.carta_pokemon())
#print(pokemon_planta.carta_pokemon())
#prueba_cartapkmn = f"******\n{pokemon_planta.nombre}\n******"
#print(prueba_cartapkmn)