# Crea una función clasificar_estudiantes que reciba un diccionario de estudiantes y sus 
# notas, y retorne dos listas: una con los estudiantes que aprobaron (nota mayor o igual 
# a 6) y otra con los que no aprobaron (nota menor a 6).

def clasificar_estudiantes(diccionarioEstudiantes:dict):
    listaAprobados = list()
    listaSuspensos = list()
    for key, value in diccionarioEstudiantes.items():
        if value >= 6: listaAprobados.append(key)
        else: listaSuspensos.append(key)
    return (listaAprobados, listaSuspensos)

diccionarioEstudiantes = {
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

listas = clasificar_estudiantes(diccionarioEstudiantes)
print(listas)