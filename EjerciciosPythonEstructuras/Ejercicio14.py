# 1. Crea una tupla con los días de la semana.
diasSemana = ("lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo")

# 2. Pide al usuario un día.
dia = str.lower(input("Introduce un dia de la semana: "))

# 3. Verifica si el día ingresado está en la tupla y muestra un mensaje.
diaEncontrado = diasSemana.__contains__(dia)
print(f"Se ha encontrado el dia: {diaEncontrado}")