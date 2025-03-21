# Crea una función añadir_a_archivo que reciba un texto y lo añada al final de un archivo 
# llamado notas.txt

def añadir_a_archivo():
    with open("notas.txt", "a") as file:
        file.write("Texto a añadir.")
    
añadir_a_archivo()