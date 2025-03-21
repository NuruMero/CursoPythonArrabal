# Crea un gráfico de barras con nombres y edades e imprímelo.

import matplotlib.pyplot as plt

nombres = ['Adan', 'Gabriel', 'Erika', 'Alicia']
edades = [23, 24, 24, 22]
plt.bar(nombres,edades)
plt.title("Edades de las personas")
plt.xlabel("Nombre")
plt.ylabel("Edad")
plt.show()