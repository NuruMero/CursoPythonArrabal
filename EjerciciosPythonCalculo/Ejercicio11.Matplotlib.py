# Genera un historiograma con 20 valores aleatorios entre 1 y 10 y muéstralo.

import numpy as np
import matplotlib.pyplot as plt

numAleatorios = np.random.randint(1, 10, 20)
plt.hist(numAleatorios)
plt.title("Historiograma de valores aleatorios")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.show()