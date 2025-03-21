# Escribe un programa que cree un archivo llamado saludo.txt y escriba en él el texto "¡Hola, Mundo!".

with open("saludo.txt", "w") as file:
    file.write("¡Hola Mundo!")