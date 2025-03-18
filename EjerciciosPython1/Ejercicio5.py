# Pide al usuario que escriba una frase y separa sus palabras en una lista. Luego, muestra
# cada palabra en una línea diferente.

frase = input("Escribe una frase que te describa: ").strip()

listaPalabras = list(frase.split())
for palabra in listaPalabras:
    print(palabra)