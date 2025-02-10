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


    def primer_inicio(self):
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


    def opcion_sobre(self): # Si el jugador elige abrir un sobre, el método jugar llamará a este método
            match self.vista.puntos_abrir_sobre(True):
                case 1:
                    self.sobre = Sobre("llamas")
                
                case 2:
                    self.sobre = Sobre("raíces")

                case 3:
                    self.sobre = Sobre("raíces")
            print(self.sobre.abrir_sobre())


    def opcion_ruleta(self): # Al igual que opcion_sobre, si el jugador decide jugar a la ruleta, se llamará a este método
        r = Ruleta([50, -10, 20, 5, 0, 100, 10])
        resultado = r.girar_ruleta()
        return resultado


    def jugar(self):
        juego = True
        pts_sobre = 0

        while juego:
            self.vista.mostrar_menu()
            opcion = int(input("Introduce tu opción: "))

            while opcion < 1 and opcion > 4:
                print("Opción no válida, vuelve a introducirla: ")


            match opcion:

                case 1:
                    if pts_sobre >= 10:
                        self.opcion_sobre()                      
                    else:
                        self.vista.puntos_abrir_sobre(False)

                case 2:
                    print("Pokédex")

                case 3:

                    ruleta = self.vista.jugar_ruleta()
                    while ruleta != "s" and ruleta != "n":
                        ruleta = input("Has introducido un valor no correspondido. Vuelve a intentarlo: ")
                         
                    while ruleta == "s":
                            
                        pts_sobre += self.opcion_ruleta()
                        print(f"Tus puntos de sobre: {pts_sobre}")
                        ruleta = input("¿Quieres volver a jugar a la ruleta PokéPuntos?(s/n) ")
            
                case 4:
                    print("¡Hasta la próxima!")
                    juego = False
