# Crea una función numeros_primos que reciba un número n y retorne una lista con los 
# primeros n números primos.

def numeros_primos(numero):
    sieve = set(range(2, numero+1))
    listaPrimos = list()
    while sieve:
        prime = min(sieve)
        listaPrimos.append(prime)
        sieve -= set(range(prime, numero+1, prime))
    return listaPrimos

n = int(input("Introduce un número: "))
primos = numeros_primos(n)
print(f"Numeros primos: {primos}")