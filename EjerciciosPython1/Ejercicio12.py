# Solicita un número y muestra su tabla de multiplicar del 1 al 10.

num = int(input("Numero: "))

print(f"Tabla del {num}")
for i in range(1, 11):
    print(f"{num} * {i} = {num*i}")