from Pokemon import Pokemon
import random
from lista_pokemon import sobre_planta, sobre_fuego, sobre_agua

class Sobre:
    tipo_sobre: str

    def __init__(self, tipo_sobre: str) -> None:
        self.tipo_sobre = tipo_sobre

    def abrir_sobre(self):
        sobre = []
        resultado = ""
        for i in range(5):
            match self.tipo_sobre:
                case "fuego":
                    clave_fuego = random.choice(list(sobre_fuego.keys()))
                    valor_fuego = sobre_fuego[clave_fuego]
                    poke = Pokemon(clave_fuego, "fuego", valor_fuego)
                    sobre.append(poke)

                case "agua":
                    clave_agua = random.choice(list(sobre_agua.keys()))
                    valor_agua = sobre_agua[clave_agua]
                    poke = Pokemon(clave_agua, "agua", valor_agua)
                    sobre.append(poke)

                case "planta":
                    clave_planta = random.choice(list(sobre_planta.keys()))
                    valor_planta = sobre_planta[clave_planta]
                    poke = Pokemon(clave_planta, "planta", valor_planta)
                    sobre.append(poke)


        for carta in sobre: # Convierto la lista de cartas en un string
            resultado += str(carta) + "\n"

        return f"{resultado}"
    

p1 = Sobre("agua")
print(p1.abrir_sobre())