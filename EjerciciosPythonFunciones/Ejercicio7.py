# Crea una función mostrar_datos que reciba un nombre y una edad. La función debe
# permitir enviar los argumentos de forma posicional y nominal.
def mostrar_datos(nombre, edad):
    print(f"Llamadme {nombre}, tengo {edad} años")

# Crea una función informacion_persona que reciba nombre, edad y ciudad como
# parámetros e imprima por pantalla la información de la persona.
def informacion_persona(nombre, edad, ciudad):
    print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

mostrar_datos("Ishmael", 34)
mostrar_datos(nombre="Ishmael", edad=34)
informacion_persona("Ishmael", 34, "Nantucket")
informacion_persona(nombre="Ishmael", edad=34, ciudad="Nantucket")