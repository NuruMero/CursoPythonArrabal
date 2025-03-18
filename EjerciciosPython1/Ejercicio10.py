# Solicita un año y verifica si es bisiesto. Un año es bisiesto si:
# ✔️ Es divisible por 4.
# ✔️ No es divisible por 100, excepto si también es divisible por 400.

anno = int(input("Indica un año: "))

esBisiesto = bool((anno % 4 == 0) and ((not anno % 100) or (anno % 400)))

print(f"Es bisiesto: {esBisiesto}")