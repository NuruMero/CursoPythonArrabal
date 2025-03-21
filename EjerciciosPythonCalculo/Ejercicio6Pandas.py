# Muestra solo la columna de edades del DataFrame anterior.

import pandas as pd

datos = {
    'Nombre': ['Adan', 'Gabriel', 'Erika', 'Alicia'],
    'Edad': [23, 24, 24, 22]
}

df = pd.DataFrame(datos)
df_edades = df['Edad']
print(df_edades)

