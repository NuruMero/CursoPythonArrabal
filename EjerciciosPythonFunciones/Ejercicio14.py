# Crea una función min_max_lista que reciba una lista de números y retorne un
# diccionario con las claves "minimo" y "maximo" que contengan el número 
# más pequeño y más grande respectivamente

def min_max_lista(listaNumeros:list):
    diccionarioNumeros = {
        "minimo":min(listaNumeros),
        "maximo":max(listaNumeros)}
    return diccionarioNumeros

listaNumeros = [1,2,3,4,5,6,7,8,9,10]
d = min_max_lista(listaNumeros)
print(d)