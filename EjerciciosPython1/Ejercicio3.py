# Solicita el nombre y la edad del usuario e imprime un mensaje formateado con
# format() y otro con f-strings.

nombre = input("Nombre: ")
edad = input("Edad: ")

print("Hola, mi nombre es {} y tengo {} años".format(nombre, edad))
print(f"Hola, mi nombre es {nombre} y tengo {edad} años")