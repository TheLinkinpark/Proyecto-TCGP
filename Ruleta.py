import time
import random
import os

class Ruleta:
    valores: list[int]

    def __init__(self, valores: list[int]):
        self.valores = valores

    def dibujar_ruleta(self, indice_seleccionado: int):
        os.system('cls' if os.name == 'nt' else 'clear')  # Borra la pantalla cada vez que dibuja la ruleta
        print("¡Que gire la ruleta!")
        print(f"\t{'─' * 12}")
        for i, valor in enumerate(self.valores):
            marcador = "<--" if i == indice_seleccionado else "   "
            print(f"\t│{valor:^10}│ {marcador}") # Imprime cada valor de la ruleta con un espaciado para centrarlo 
        print(f"\t{'─' * 12}")

    def girar_ruleta(self):
        indice_seleccionado = 0
        for num in range(random.randint(10, 20)):

            indice_seleccionado = (indice_seleccionado + 1) % len(self.valores)
            self.dibujar_ruleta(indice_seleccionado)
            time.sleep(0.15)
        
        resultado = self.valores[indice_seleccionado]

        if self.valores[indice_seleccionado] < 0:
            print(f"Has perdido {abs(resultado)} puntos...")
        else:
            print(f"¡Has ganado {resultado} puntos!")

        time.sleep(0.6)
        return resultado

if __name__ == "__main__":
    r = Ruleta([50, -10, 20, 5, 0, 100, 10])
    r.girar_ruleta()

