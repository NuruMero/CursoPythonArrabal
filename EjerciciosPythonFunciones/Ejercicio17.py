# Crea una función elementos_comunes que reciba dos listas y retorne una lista con los 
# elementos que aparecen en ambas listas

def elementos_comunes(lista1:list, lista2:list):
    return list(set(lista1).intersection(set(lista2)))

lista1 = [1,2,3,4,5,6,7,8,9,10]
lista2 = [2,4,6,8,10,12,14,16,18]
listaComun = elementos_comunes(lista1, lista2)
print(listaComun)