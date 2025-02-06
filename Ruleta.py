import time
import random
import os

class Ruleta:
    valores: list[int]

    def __init__(self, valores):
        self.valores = valores

    def dibujar_ruleta(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # Borra la pantalla cada vez que dibuja la ruleta
        print('─' * 30)
        for i in (self.valores):
            print(f"│{i}│")

if __name__ == "__main__":
    p = Ruleta([50, -10, 5, 20, 5, 0, 100, 5, 10])
    p.dibujar_ruleta()

