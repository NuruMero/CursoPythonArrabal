# 1. Pide al usuario una palabra.
palabra = str.upper(input("Introduce una palabra: "))

# 2. Usa un diccionario para contar cuántas veces aparece cada letra.
contarLetras = {}

for letra in palabra:
    if contarLetras.keys().__contains__(letra):
        contarLetras[letra] += 1
    else:
        contarLetras[letra] = 1

# 3. Muestra el diccionario con los resultados.
print(contarLetras)