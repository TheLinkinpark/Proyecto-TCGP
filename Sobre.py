from Pokemon import Pokemon
from Pokedex import Pokedex
import random
import json

with open('lista_pokemon.json', 'r', encoding="utf-8") as p: # Abro el archivo con la lista de pokemons
    pokemons = json.load(p)

class Sobre:
    tipo_sobre: str
    pokedex: Pokedex

    def __init__(self, tipo_sobre: str) -> None:
        self.tipo_sobre = tipo_sobre
        self.pokedex = Pokedex()

    def abrir_sobre(self):
        sobre = [] # Creo una lista vacía para añadir las cartas del sobre
        
        for i in range(5):
            match self.tipo_sobre:
                case "llamas":
                    clave_llamas = random.choice(list(pokemons["sobre_llamas"])) # Escojo el nombre de un pokémon, siendo la clave del diccionario
                    valor_llamas = pokemons["sobre_llamas"][clave_llamas] # Con la clave, obtengo sus datos
                    poke = Pokemon(clave_llamas, valor_llamas["tipo"], valor_llamas["rareza"], valor_llamas["num_pokedex"])

                case "marea":
                    clave_marea = random.choice(list(pokemons["sobre_marea"])) # Hago lo mismo para los 3 tipos de sobre
                    valor_marea = pokemons["sobre_marea"][clave_marea]
                    poke = Pokemon(clave_marea, valor_marea["tipo"], valor_marea["rareza"], valor_marea["num_pokedex"])

                case "raíces":
                    clave_raices = random.choice(list(pokemons["sobre_raices"]))
                    valor_raices = pokemons["sobre_raices"][clave_raices]
                    poke = Pokemon(clave_raices, valor_raices["tipo"], valor_raices["rareza"], valor_raices["num_pokedex"])
             
            sobre.append(poke)

            self.pokedex.anhadir_carta(sobre) # Añado los Pokémon a la Pokédex

            resultado = " ".join([str(carta) for carta in sobre]) # Convierto la lista de cartas en un string y así imprimirlas por pantalla


        return resultado


if __name__ == "__main__":
    p1 = Sobre("llamas")
    print(p1.abrir_sobre())