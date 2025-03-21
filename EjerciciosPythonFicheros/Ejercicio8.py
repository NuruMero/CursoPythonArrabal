# Crea una función crear_directorio que cree un directorio llamado mi_directorio 
# si no existe.

import os

def crear_directorio():
    if not os.path.exists("mi_directorio"):
        os.mkdir("mi_directorio")

crear_directorio()