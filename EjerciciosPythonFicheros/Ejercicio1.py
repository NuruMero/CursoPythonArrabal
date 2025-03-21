# Crea una función comprobar_existencia_archivo que reciba un nombre de archivo y 
# retorne True si el archivo existe, y False en caso contrario.

import os

def comprobar_existencia_archivo(name):
    return os.path.exists(name)

filename = input("Introduce el nombre del archivo: ")
print(f"El archivo existe: {comprobar_existencia_archivo(filename)}")