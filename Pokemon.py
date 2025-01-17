class Pokemon:
    nombre: str
    tipo: str
    rareza: str

    def __init__(self, nombre, tipo, rareza):
        self.nombre = nombre
        self.tipo = tipo
        self.rareza = rareza

    def __str__(self) -> str:
        return f"Nombre:\n\t{self.nombre}\nTipo:\n\t{self.tipo}\nRareza:\n\t{self.rareza}"
    

pokemon1 = Pokemon("Charizard", "fuego", "***")

print(pokemon1)