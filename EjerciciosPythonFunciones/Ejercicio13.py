# Crea una función filtrar_pares_impares que reciba una lista de números y retorne un
# diccionario con las claves: "pares" e "impares", donde cada clave contenga una lista
# de los números correspondientes.

def filtrar_pares_impares(listaNumeros:list):
    numImpares = list()
    numPares = list()
    for num in listaNumeros:
        if num % 2 == 0: numPares.append(num)
        else: numImpares.append(num)
    diccionarioNumeros = {
        "Impares": numImpares,
        "Pares": numPares}
    return diccionarioNumeros

listaNumeros = [1,2,3,4,5,6,7,8,9,10]
d = filtrar_pares_impares(listaNumeros)
print(d)