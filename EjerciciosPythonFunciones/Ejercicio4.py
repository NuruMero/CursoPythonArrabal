# Crea una función calcular_promedio que reciba una lista de números y retorne el 
# promedio.

def calcular_promedio(numeros:list):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma/len(numeros)

lista = [1, 2, 4, 7, 98, 34, 22]
print(calcular_promedio(lista))