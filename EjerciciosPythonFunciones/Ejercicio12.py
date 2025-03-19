# Desempaqueta una lista (valores = [1,2,3]) variables (a,b,c) muestra por pantalla las 
# variables para ver que todo ha sido correcto.

def desempaquetador(nombre, edad):
    print(f"Mi nombre es {nombre}, tengo {edad} años")

datos = ("Adan", 24)
desempaquetador(*datos)