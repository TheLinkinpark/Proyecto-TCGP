class Pokemon:
    nombre: str
    tipo: str
    rareza: str
    num_pokedex: int

    def __init__(self, nombre: str, tipo: str, rareza: str, num_pokedex: int) -> None:
        self.nombre = nombre
        self.tipo = tipo
        self.rareza = rareza
        self.num_pokedex = num_pokedex


    def __str__(self) -> str: # Devuelve la carta Pokémon dibujada
        return f'''
┌───────────────────┐
│ {self.nombre.center(17)} │
├───────────────────┤
│ {self.tipo.center(17)} │ 
│ {self.rareza.center(17)} │
│                   │  
│ {str(self.num_pokedex).center(17)} │
└───────────────────┘'''

if __name__ == "__main__":
    p = Pokemon("Bulbasaur", "Tipo: eléctrico", "Rareza: *", 1)
    print(p)
