import json

class Pokedex:
    
    def mostrar_pokedex(self):
        with open('pokedex.json', "r", encoding="utf-8") as pokedex:
            return json.load(pokedex)
        
    def guardar_pokedex(pokedex):
         # Ordenar por número de Pokédex y volver a convertir a diccionario
        pokedex_ordenada = dict(sorted(pokedex.items(), key=lambda item: item[1]["num_pokedex"]))
        with open('pokedex.json', "w", encoding="utf-8") as poke_guardar:
            json.dump(pokedex, poke_guardar, indent=4, ensure_ascii=False)
        
    def anhadir_carta(self, sobre):
        """Añade nuevas cartas a la Pokédex, sumando cantidad si ya existen."""
        pokedex = self.mostrar_pokedex()
        print(type(pokedex), pokedex)
        # for nombre, datos in sobre.items():
        #     if nombre in pokedex:
        #         pokedex[nombre]["cantidad"] += 1  # Aumentar cantidad si ya existe
        #     else:
        #         pokedex[nombre] = datos
        #         pokedex[nombre]["cantidad"] = 1  # Nueva entrada con cantidad inicial 1

        self.guardar_pokedex(pokedex)


if __name__ == "__main__":
    p = Pokedex()
    print(p.mostrar_pokedex())

    