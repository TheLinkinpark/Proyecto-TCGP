from Pokemon import Pokemon
from Pokedex import Pokedex
import random
import json
import time

with open('lista_pokemon.json', 'r', encoding="utf-8") as p:
    pokemons = json.load(p)

class Sobre:
    tipo_sobre: str
    pokedex: Pokedex

    def __init__(self, tipo_sobre: str) -> None:
        self.tipo_sobre = tipo_sobre
        self.pokedex = Pokedex()

    def abrir_sobre(self):
        sobre = []
        resultado = ""
        for i in range(5):
            match self.tipo_sobre:
                case "llamas":
                    clave_llamas = random.choice(list(pokemons["sobre_llamas"]))
                    valor_llamas = pokemons["sobre_llamas"][clave_llamas]
                    poke = Pokemon(clave_llamas, valor_llamas["tipo"], valor_llamas["rareza"], valor_llamas["num_pokedex"])

                case "marea":
                    clave_marea = random.choice(list(pokemons["sobre_marea"]))
                    valor_marea = pokemons["sobre_marea"][clave_marea]
                    poke = Pokemon(clave_marea, valor_marea["tipo"], valor_marea["rareza"], valor_marea["num_pokedex"])

                case "raíces":
                    clave_raices = random.choice(list(pokemons["sobre_raices"]))
                    valor_raices = pokemons["sobre_raices"][clave_raices]
                    poke = Pokemon(clave_raices, valor_raices["tipo"], valor_raices["rareza"], valor_raices["num_pokedex"])
             
            sobre.append(poke)
            
            self.pokedex.anhadir_carta(sobre)

        for carta in sobre: # Convierto la lista de cartas en un string
            
            resultado += str(carta) + "\n"

        return f"{resultado}"




if __name__ == "__main__":
    p1 = Sobre("llamas")
    print(p1.abrir_sobre())