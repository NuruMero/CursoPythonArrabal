# Filtra e imprime solo las personas que tengan más de 25 años.

import pandas as pd

datos = {
    'Nombre': ['Adan', 'Gabriel', 'Erika', 'Alicia', 'Gerardo'],
    'Edad': [23, 24, 24, 22, 45]
}

df = pd.DataFrame(datos)
df_mayores = df[df['Edad'] > 25]
print(df_mayores)