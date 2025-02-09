from Pokemon import Pokemon
from Ruleta import Ruleta
from Sobre import Sobre
from Vista import Vista
from time import sleep

class Juego:
    pokemon: Pokemon
    sobre: Sobre
    ruleta: Ruleta
    vista: Vista

    def __init__(self):
        self.vista = Vista()


    def jugar(self):
        self.vista.bienvenida()
        sleep(1)

        primer_sobre = self.vista.primer_sobre()
        
        while primer_sobre != "s" and primer_sobre != "n":
            primer_sobre = input("Has introducido un valor no correspondido. Vuelve a intentarlo: ")

        if  primer_sobre == "s":
            sleep(1)
            match self.vista.puntos_abrir_sobre(True):
                case 1:
                    self.sobre = Sobre("llamas")
                
                case 2:
                    self.sobre = Sobre("raíces")

                case 3:
                    self.sobre = Sobre("raíces")
            print(self.sobre.abrir_sobre())
        else:
             print("Has desaprovechado esta oportunidad, es una pena...")

        self.vista.mostrar_menu()