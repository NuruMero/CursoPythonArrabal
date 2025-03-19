# Crea una función calcular_area_rectangulo que reciba base y altura como parámetros 
# y retorne el área. Si no se proporcionan valores, que use base=10 y altura=5 por 
# defecto.

def calcular_area_rectangulo(base=10, altura=5):
    return (base*altura)/2

base = int(input("Base: "))
altura = int(input("Altura: "))
area = calcular_area_rectangulo(base, altura)
print(f"Area: {area}")