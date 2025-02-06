class Vista:

    def bienvenida(self) -> None:
        print("¡Bienvendx al Juego de Cartas Coleccionables de Pokémon!")
        print('''En este juego podrás abrir sobres de Pokémon y coleccionar las cartas en tu Pokédex.
              Dispones de 3 tipos de sobre para abrir, los cuales son:
              1. Llamas y rugidos
              2. Raíces y rocas
              3. Mareas místicas
              ''')

    def mostrar_menu(self):
        print('''
            1. Abrir sobre
            2. Ver Pokédex
            3. Ruleta PokéPuntos
            4. Salir''')

    def nombre_jugador(self):
        return input("Introduce tu nombre: ")
    
    def puntos_abrir_sobre(self, pts_necesarios: bool): # 
        if pts_necesarios:
            print("Tienes los puntos necesarios para abrir un sobre. ¡A por él!")
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
            int(input("Introduce el número del sobre que quieres abrir: "))

        else:
                print("No tienes los puntos suficientes para abrir un sobre. ¡Consigue más puntos!")

    def jugar_ruleta(self):
        print("¡Bienvenidx a la Ruleta PokéPuntos!")
        print('''En esta ruleta podrás conseguir puntos (o perderlos) para abrir sobres.
              Podrás conseguir 0, 5, 10, 20, 50 o 100 puntos. Sin embargo, también puedes llegar a perder 10 puntos.
              Todo dependerá del azar. ¡Buena suerte!''')
        return input("¿Quieres jugar a la ruleta para conseguir puntos? (s/n): ")


if __name__ == "__main__":
    prueba = Vista()
    prueba.puntos_abrir_sobre(True)
