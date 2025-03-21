# Agrega una nueva columna de altura al DataFrame e imprímelo.

import pandas as pd

datos = {
    'Nombre': ['Adan', 'Gabriel', 'Erika', 'Alicia'],
    'Edad': [23, 24, 24, 22]
}

df = pd.DataFrame(datos)
df['Altura'] = [1.80, 1.90, 1.65, 1.67]
print(df)