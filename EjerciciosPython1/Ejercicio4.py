# Solicita una frase al usuario y muestra la misma frase en mayúsculas, minúsculas, con
# iniciales en mayúscula y reemplazando una palabra.

frase = input("Escribe una frase que te describa: ").strip()

print(f"En mayúscula: {frase.upper()}")
print(f"En minúscula: {frase.lower()}")
print(f"Con iniciales en mayúscula: {frase.title()}")
print(f"Sustituyendo s por z: {frase.replace("s", "z")}")