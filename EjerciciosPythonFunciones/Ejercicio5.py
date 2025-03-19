# Crea una función calcular_descuento que reciba un precio y un porcentaje de
# descuento, y devuelva el precio final. El descuento debe ser opcional y por defecto 10%

def calcular_descuento(precio, descuento=10):
    precioDescuentado = precio*(descuento/100)
    return(precio - precioDescuentado)

precio1 = int(input("Primer precio: "))
print(calcular_descuento(precio1))

precio2 = int(input("Segundo precio: "))
descuento2 = int(input("Descuento en %: "))
print(calcular_descuento(precio2, descuento2))