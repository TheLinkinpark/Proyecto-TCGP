import random
from lista_pokemon import planta, fuego, agua

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
    
    def carta_pokemon(self):
        return f"**************\n* {self.nombre} *\n**************"

    def __str__(self) -> str:
        return f"Nombre:\n\t{self.nombre}\nTipo:\n\t{self.tipo}\nRareza:\n\t{self.rareza}"
    

clave_fuego = random.choice(list(fuego.keys()))
valor_fuego = fuego[clave_fuego]

clave_planta = random.choice(list(planta.keys()))
valor_planta = planta[clave_planta]

clave_agua = random.choice(list(agua.keys()))
valor_agua = agua[clave_agua]

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