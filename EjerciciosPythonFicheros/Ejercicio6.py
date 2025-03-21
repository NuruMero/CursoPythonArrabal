# Crea una función renombrar_archivo que reciba un nombre de archivo antiguo y uno 
# nuevo, y lo renombre.

import os

def renombrar_archivo():
    filename = input("Introduce el nombre del archivo a cambiar: ")
    if (os.path.exists):
        newname = input("Introduce el nuevo nombre: ")
        os.rename(filename, newname)

renombrar_archivo()