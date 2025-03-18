# 1. Crea dos conjuntos de números.
numeros1 = {1, 2, 3, 5, 7, 9}
numeros2 = {1, 2, 4, 6, 8, 10}

# 2. Verifica si tienen algún número en común.

# 3. Muestra los elementos en común (si los hay) o un mensaje indicando que son conjuntos disjuntos.
if any(i in numeros1 for i in numeros2):
    print("Hay numeros en común.")
    print(set.intersection(numeros1, numeros2))
