import os

class Vista:

    def bienvenida(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 56)
        print("¡Bienvendx al Juego de Cartas Coleccionables de Pokémon!")
        print("=" * 56)
        print('''
En este juego podrás abrir sobres de Pokémon y coleccionar las cartas en tu Pokédex.
Dispones de 3 tipos de sobre para abrir, los cuales son:
    1. Llamas y rugidos
    2. Raíces y rocas
    3. Mareas místicas

En ellos podrás encontrar desde cartas muy comunes hasta cartas rarísimas, incluyendo a los Pokémon legendarios.
Si tienes la suerte de obtener a los 4 Pokémon legendarios que están repartidos entre los 3 sobres, recibirás
una recompensa digna.
    ''')
        
    def primer_sobre(self):
        print('''
Al ser tu primera vez en el juego, has recibido un sobre gratuito para que puedas empezar a conseguir cartas.
Si quieres seguir abrindo sobres, tendrás que conseguir PokéPuntos jugando en la ruleta.
''')
        return input("¿Quieres abrir el sobre? Si dices que no, no podrás volver a obtenerlo (s/n): ")
    

    def mostrar_menu(self):
        print(f'''
==================
  Menú principal
==================          

1. Abrir sobre
2. Ver Pokédex
3. Ruleta PokéPuntos
4. Salir''')

    
    def puntos_abrir_sobre(self, pts_necesarios: bool): # 
        if pts_necesarios:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("¡Vamos a abrir un sobre!")
            sobre1 = [
        "########################################",
        "#**************************************#",
        "#*                                    *#",
        "#*         LLAMAS Y RUGIDOS           *#",
        "#*                                    *#",
        "#*                                    *#",
        "#*              (o^.^)                *#",
        "#*              (>🔥<)                *#",
        "#*                                    *#",
        "#*        ⚡ Pokémons tipo ⚡         *#",
        "#*         fuego y eléctrico          *#",
        "#**************************************#",
        "########################################"
            ]
            sobre2 = [
        "########################################",
        "#**************************************#",
        "#*                                    *#",
        "#*         RAÍCES Y ROCAS             *#",
        "#*                                    *#",
        "#*                                    *#",
        "#*         ⠀🌿⠀(o^.^)🌿               *#",
        "#*         ⠀🌿⠀(>🍃<)🌿               *#",
        "#*                                    *#",
        "#*        🌱 Pokémons tipo 🌱         *#",
        "#*       planta, roca y tierra        *#",
        "#**************************************#",
        "########################################"
            ]
            sobre3 = [
        "########################################",
        "#**************************************#",
        "#*                                    *#",
        "#*         MAREAS MÍSTICAS            *#",
        "#*                                    *#",
        "#*                                    *#",
        "#*          🌊 (o^.^)🔮               *#",
        "#*          🌊 (>💧<)🔮               *#",
        "#*                                    *#",
        "#*        🌊 Pokémons tipo 🌊         *#",
        "#*          agua y psíquico           *#",
        "#**************************************#",
        "########################################"
            ] 
    

            # Imprimir los sobres en paralelo
            for linea1, linea2, linea3 in zip(sobre1, sobre2, sobre3):
                print(f"{linea1}   {linea2}   {linea3}")

            return int(input("Introduce el número del sobre que quieres abrir: "))

        else:
                print("No tienes los puntos suficientes para abrir un sobre. ¡Consigue más puntos!")

    def jugar_ruleta(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("¡Bienvenidx a la Ruleta PokéPuntos!")
        print()
        print('''En esta ruleta podrás conseguir puntos (o perderlos) para abrir sobres.
              
Podrás conseguir 0, 5, 10, 20, 50 o 100 puntos. Sin embargo, también puedes llegar a perder 10 puntos.
Todo dependerá del azar. ¡Buena suerte!''')
        return input("¿Quieres jugar a la ruleta para conseguir puntos? (s/n): ")


if __name__ == "__main__":
    prueba = Vista()
    prueba.puntos_abrir_sobre(True)
