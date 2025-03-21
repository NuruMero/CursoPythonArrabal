# Crea una función leer_lineas_archivo que lea el contenido de un archivo llamado 
# notas.txt línea por línea y las imprima.

def leer_lineas_archivo():
    with open("notas.txt", "r") as mendrugo:
        for line in mendrugo:
            print(line.strip())

leer_lineas_archivo()