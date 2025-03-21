# Crea una función eliminar_archivo que reciba el nombre de un archivo y lo elimine si existe.

import os

def eliminar_archivo():
    filename = input("Introduce el nombre del archivo a eliminar: ")
    if os.path.exists(filename):
        os.remove(filename)

eliminar_archivo()