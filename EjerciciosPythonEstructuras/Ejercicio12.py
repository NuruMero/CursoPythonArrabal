# 1. Crea una lista con varias palabras repetidas.
palabras = ["Atencion", "Paciencia", "Templanza", "Atencion", "Cuidado", "Atencion"]

# 2. Pide al usuario una palabra.
eleccion = input("Indica una palabra: ")

# 3. Muestra cuántas veces aparece en la lista.
print(f"Veces que aparece {eleccion}: {palabras.count(eleccion)}")