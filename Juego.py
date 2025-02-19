from Pokemon import Pokemon
from Pokedex import Pokedex
from Ruleta import Ruleta
from Sobre import Sobre
from Vista import Vista
from time import sleep
import os

class Juego:
    pokemon: Pokemon
    pokedex: Pokedex
    sobre: Sobre
    ruleta: Ruleta
    vista: Vista

    def __init__(self):
        self.vista = Vista()
        self.pokedex = Pokedex()

    def primer_inicio(self):
        self.vista.bienvenida()
        sleep(1)



        primer_sobre = self.vista.primer_sobre()
        
        while primer_sobre != "s" and primer_sobre != "n":
            primer_sobre = input("Has introducido un valor no correspondido. Vuelve a intentarlo: ")


        if  primer_sobre == "s":

            op_sobre = self.vista.puntos_abrir_sobre(True) # Paso a una variable el sobre elegido por el jugador

            while op_sobre < 1 or op_sobre > 3: # Compruebo que el jugador escoge una opción válida
                op_sobre = int(input("Opción no válida, vuelve a introducirla: "))

            sleep(1)
            match op_sobre:

                case 1:
                    self.sobre = Sobre("llamas")
                
                case 2:
                    self.sobre = Sobre("raíces")

                case 3:
                    self.sobre = Sobre("raíces")


            print("Espera unos segundos, se están generando las cartas...")
            sleep(2)       
            print(self.sobre.abrir_sobre())

            tecla = input("Pulsa cualquier tecla para continuar: ")
        else:
             print("Has desaprovechado esta oportunidad, es una pena...")


    def opcion_sobre(self): # Si el jugador elige abrir un sobre, el método jugar llamará a este método
            
            op_sobre = self.vista.puntos_abrir_sobre(True) # Paso a una variable el sobre elegido por el jugador

            while op_sobre < 1 or op_sobre > 3: # Compruebo que el jugador escoge una opción válida
                op_sobre = int(input("Opción no válida, vuelve a introducirla: "))


            match op_sobre:
                case 1:
                    self.sobre = Sobre("llamas")
                
                case 2:
                    self.sobre = Sobre("raíces")

                case 3:
                    self.sobre = Sobre("marea")
            print("Espera unos segundos, se están generando las cartas...")
            sleep(2)
            print(self.sobre.abrir_sobre())

            tecla = input("Pulsa cualquier tecla para continuar: ")


    def opcion_ruleta(self): # Al igual que opcion_sobre, si el jugador decide jugar a la ruleta, se llamará a este método
        r = Ruleta([50, -10, 20, 5, 0, 100, 10])
        resultado = r.girar_ruleta()
        return resultado


    def jugar(self):
        juego = True
        pts_sobre = 10

        while juego:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.vista.mostrar_menu()
            opcion = int(input("Introduce tu opción: "))

            while opcion < 1 or opcion > 4: # Compruebo que el jugador escoge una opción válida para el menú
                opcion = int(input("Opción no válida, vuelve a introducirla: "))


            match opcion:

                case 1:
                    if pts_sobre >= 10:
                        self.opcion_sobre()                      
                    else:
                        self.vista.puntos_abrir_sobre(False)

                case 2:
                    self.pokedex.enseñar_pokedex()
                    tecla = input("Pulsa cualquier tecla para volver al menú principal: ")

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
