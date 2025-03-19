# Crea una función que modifique una lista dentro de una función y observa su efecto.
def modificar_lista(listaACambiar:list):
    listaACambiar[0] = "Inicio"
    return

lista = ["Algo", "Quien", "Nadie", "Puede"]
modificar_lista(lista)
print(lista)