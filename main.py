from Juego import Juego

# Se recomienda aumentar un poco el tamaño de la terminal de VSCode para obtener una mejor experiencia visual.

# Para mostrar la Pokédex, hago uso de la librería tabulate, para que se vea más ordenado.
# Instalación: pip install tabulate

if __name__ == "__main__":
    juego = Juego()

    with open('pokedex.json', 'r') as file:
        contenido = file.read()
        if contenido == '':
            juego.primer_inicio() # Si el archivo está vacío, se entiende que es la primera vez que se juega
            
        juego.jugar() # Si hay contenido en el archivo, ignora el mensaje de bienvenida
                          # y muestra directamente el menú principal
        
    
    