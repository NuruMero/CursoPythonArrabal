# Crea una función saludo_personalizado que reciba un nombre y un saludo opcional
# (por defecto "Hola") y retorne el mensaje

def saludo_personalizado(nombre, saludo="Hola"):
    return (f"{saludo}, mi nombre es {nombre}")

nombre = input("Introduce tu nombre: ")
saludo = input("Introduce un saludo: ")
print(saludo_personalizado(nombre))
print(saludo_personalizado(nombre, saludo))