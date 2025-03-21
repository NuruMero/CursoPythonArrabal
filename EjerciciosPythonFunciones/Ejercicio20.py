# Crea una función es_palindromo que reciba una palabra y retorne True si es un 
# palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda), y False en 
# caso contrario.

def isPalindrome(word):
    i = 0
    j = len(word)-1
    palindrome = True
    
    while i < j:
        if word[i].lower() != word[j].lower():
            palindrome = False
            break
        i += 1
        j -= 1

    return palindrome

word = input("Introduce una palabra: ")
print(f"Es palíndromo: {isPalindrome(word)}")