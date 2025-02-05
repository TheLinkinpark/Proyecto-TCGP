import time
import random
import os
class Ruleta:
    valores: list[int]

    def __init__(self):
        self.valores = [20, 0, 50, 5, 10, -10, 100, 5]

    def dibujar_ruleta():
        os.system('cls' if os.name == 'nt' else 'clear')  # Borra la pantalla cada vez que dibuja la ruleta
