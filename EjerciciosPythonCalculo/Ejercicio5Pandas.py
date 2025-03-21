# Crea un DataFrame en Pandas con nombres y edades e imprímelo.

import pandas as pd

datos = {
    'Nombre': ['Adan', 'Gabriel', 'Erika', 'Alicia'],
    'Edad': [23, 24, 24, 22]
}

df = pd.DataFrame(datos)
print(df)

