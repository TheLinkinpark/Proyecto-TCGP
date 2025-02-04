class Vista:

    def bienvenida(self) -> None:
        print("¡Bienvend@ al Juego de Cartas Coleccionables de Pokémon!")
        print('''En este juego podrás abrir sobres de Pokémon y coleccionar las cartas en tu Pokédex.
              Dispones de 3 tipos de sobre para abrir, los cuales son:
              1. Raíces y rocas
              2. Llamas y rugidos
              3. Mareas místicas
              ''')

    def mostrar_menu(self):
        print('''
            1. Abrir sobre
            2. Ver Pokédex
            3. Conseguir Puntos
            4. Salir''')

    def nombre_jugador(self):
        return input("Introduce tu nombre: ")
    



# def dibujar_sobre_llamas():
#     return [
#         "########################################",
#         "#**************************************#",
#         "#*                                    *#",
#         "#*         LLAMAS Y RUGIDOS          *#",
#         "#*                                    *#",
#         "#*                                   *#",
#         "#*              (o^.^)               *#",
#         "#*              (>🔥<)               *#",
#         "#*                                    *#",
#         "#*        ⚡ Pokémons tipo ⚡       *#",
#         "#*         fuego y eléctrico          *#",
#         "#**************************************#",
#         "########################################"
#     ]

# def dibujar_sobre_raices():
#     return [
#         "########################################",
#         "#**************************************#",
#         "#*                                    *#",
#         "#*         RAÍCES Y ROCAS            *#",
#         "#*                                    *#",
#         "#*                                   *#",
#         "#*         ⠀🌿⠀(o^.^)🌿             *#",
#         "#*         ⠀🌿⠀(>🍃<)🌿             *#",
#         "#*                                    *#",
#         "#*        🌱 Pokémons tipo 🌱        *#",
#         "#*            planta, roca y tierra   *#",
#         "#**************************************#",
#         "########################################"
#     ]

# def dibujar_sobre_marea():
#     return [
#         "########################################",
#         "#**************************************#",
#         "#*                                    *#",
#         "#*         MAREAS MÍSTICAS            *#",
#         "#*                                    *#",
#         "#*                                   *#",
#         "#*          🌊 (o^.^)🔮             *#",
#         "#*          🌊 (>💧<)🔮             *#",
#         "#*                                    *#",
#         "#*        🌊 Pokémons tipo 🌊        *#",
#         "#*            agua y psíquico         *#",
#         "#**************************************#",
#         "########################################"
#     ]

# # Obtener las líneas de cada sobre
# sobre1 = dibujar_sobre_llamas()
# sobre2 = dibujar_sobre_raices()
# sobre3 = dibujar_sobre_marea()

# # Imprimir en paralelo
# for linea1, linea2, linea3 in zip(sobre1, sobre2, sobre3):
#     print(f"{linea1}   {linea2}   {linea3}")
