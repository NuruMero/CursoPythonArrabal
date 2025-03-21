# Crea una función leer_archivo que lea y muestre el contenido de un archivo llamado saludo.txt

def leer_archivo():
    with open("saludo.txt", "r") as file:
        print(file.read())

leer_archivo()