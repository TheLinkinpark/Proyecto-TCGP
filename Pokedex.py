import json
import os
from tabulate import tabulate

class Pokedex:
    
    def inciar_pokedex(self):          
        with open('pokedex.json', 'r', encoding="utf-8") as pokedex:

            try:
                return json.load(pokedex) # Intenta cargar el archivo, si no puede, devuelve un diccionario vacío
            except json.JSONDecodeError:
                return {}
            
    def cantidad_cartas(self): # Cuento la cantidad de cartas en la Pokédex
        pokedex = self.inciar_pokedex()
        return len(pokedex)


    def enseñar_pokedex(self):
        pokedex = self.inciar_pokedex()
        tabla = []

        for nombre, datos in pokedex.items(): # Voy añadiendo los datos de cada carta a la tabla
            tabla.append([nombre, datos["rareza"], datos["tipo"], datos["num_pokedex"]])

        os.system('cls' if os.name == 'nt' else 'clear')
        print(tabulate(tabla, headers=["Nombre", "Rareza", "Tipo", "N° Pokédex"], tablefmt="fancy_grid"))
        
    def guardar_pokedex(self, pokedex: dict):
        # Ordeno el contenido del archivo por número de Pokédex
        pokedex_ordenada = dict(sorted(pokedex.items(), key=lambda item: item[1]["num_pokedex"]))
        
        with open('pokedex.json', "w", encoding="utf-8") as poke_guardar: # Guardo el archivo con los datos ordenados
            json.dump(pokedex_ordenada, poke_guardar, indent=4, ensure_ascii=False)
        
    def anhadir_carta(self, sobre: list):
        pokedex = self.inciar_pokedex()
        
        for carta in sobre: # Para cada carta en el sobre, se añade a la Pokédex
            nombre = carta.nombre
            if nombre in pokedex:
                pokedex[nombre]["cantidad"] += 1  # Si la carta obtenida ya está en la Pokédex, se añade 1 a la cantidad
            else:                                 # Utilizo este sistema para no tener datos repetidos en pokedex.json
                pokedex[nombre] = {
                    "nombre": carta.nombre,
                    "tipo": carta.tipo,
                    "rareza": carta.rareza,
                    "num_pokedex": carta.num_pokedex,
                    "cantidad": 1  # Si es la primera vez que se obtiene la carta, se añade con cantidad 1
                }

        self.guardar_pokedex(pokedex)
