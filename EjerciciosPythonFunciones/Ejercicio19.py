# Crea una función invertir_diccionario que reciba un diccionario con claves y valores, y 
# retorne un nuevo diccionario donde las claves y los valores estén intercambiados.

def invertir_diccionario(diccionario:dict):
    nuevo_dicc = {value: key for key,value in diccionario.items()}
    return nuevo_dicc

diccionario = {
    "Adan" : 10,
    "Kike" : 1,
    "Manuela" : 8,
    "Pedro" : 3,
    "Federico" : 6,
    "Wenceslao" : 5,
    "María" : 4,
    "Tatyana" : 7,
    "Oliver" : 2,
    "Antonio" : 9,
    "Rodolfo" : 0,
}
print(invertir_diccionario(diccionario))