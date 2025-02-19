import json
import os
from tabulate import tabulate
class Pokedex:
    
    def mostrar_pokedex(self):        

        with open('pokedex.json', 'r', encoding="utf-8") as pokedex:     
             poke = json.load(pokedex)

        tabla = []
        for nombre, datos in poke.items():
            tabla.append([nombre, datos["rareza"], datos["tipo"], datos["num_pokedex"]])

        os.system('cls' if os.name == 'nt' else 'clear')
        print(tabulate(tabla, headers=["Nombre", "Rareza", "Tipo", "N° Pokédex"], tablefmt="fancy_grid"))
        
    def guardar_pokedex(self, pokedex):
        # Ordenar por número de Pokédex y volver a convertir a diccionario
        pokedex_ordenada = dict(sorted(pokedex.items(), key=lambda item: item[1]["num_pokedex"]))
        with open('pokedex.json', "w", encoding="utf-8") as poke_guardar:
            json.dump(pokedex_ordenada, poke_guardar, indent=4, ensure_ascii=False)
        
    def anhadir_carta(self, sobre):
        """Añade nuevas cartas a la Pokédex, sumando cantidad si ya existen."""
        pokedex = self.mostrar_pokedex()
        
        for carta in sobre:
            nombre = carta.nombre
            if nombre in pokedex:
                pokedex[nombre]["cantidad"] += 1  # Si la carta obtenida ya está en la Pokédex, se añade 1 a la cantidad
            else:
                pokedex[nombre] = {
                    "nombre": carta.nombre,
                    "tipo": carta.tipo,
                    "rareza": carta.rareza,
                    "num_pokedex": carta.num_pokedex,
                    "cantidad": 1  # Si es la primera vez que se obtiene la carta, se añade con cantidad 1
                }

        self.guardar_pokedex(pokedex)


if __name__ == "__main__":
    cartas = {"Bulbasaur": {
            "nombre": "Bulbasaur",
            "rareza": "*",
            "tipo": "planta",
            "num_pokedex": 1
        },
        "Ivysaur": {
            "nombre": "Ivysaur",
            "rareza": "**",
            "tipo": "planta",
            "num_pokedex": 2
        }}
    print(cartas)
    p = Pokedex()

    print(p.anhadir_carta(cartas))

    