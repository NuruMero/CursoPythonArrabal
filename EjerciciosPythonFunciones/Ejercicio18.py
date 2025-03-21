# Crea una función sumar_valores_diccionario que reciba un diccionario de números y 
# retorne la suma de todos los valores.

def sumar_valores_diccionario(numeros):
    suma = 0
    for key, value in numeros.items():
        suma += value
    return suma

numeros = {
    "a":1,
    "b":2,
    "c":3,
    "d":4
}
print(sumar_valores_diccionario(numeros))