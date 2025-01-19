class Vista:

    def bienvenida(self):
        print("Bienvend@ al Juego de Cartas Coleccionables de Pokémon")
        print('''En este juego podrás abrir sobres de Pokémon y coleccionarlas en tu Pokédex.
              Dispones de 3 tipos de sobre para abrir, los cuales son:
              1. Tipo planta
              2. Tipo fuego
              3. Tipo agua
              ''')

    def mostrar_menu(self):
        print('''
            1. Abrir sobre
            2. Ver Pokédex
            3. Salir''')

    def nombre_jugador(self):
        return input("Introduce tu nombre: ")