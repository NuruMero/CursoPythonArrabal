# Dibuja un gráfico de línea con Matplotlib usando los valores dados.

import matplotlib.pyplot as plt

tiempo = [0, 15, 30, 45, 60]
intensidad = [4, 3, 6, 5, 5]
plt.plot(tiempo, intensidad)
plt.title("Resultados por tiempo")
plt.xlabel("Tiempo")
plt.ylabel("Resultados")
plt.show()
