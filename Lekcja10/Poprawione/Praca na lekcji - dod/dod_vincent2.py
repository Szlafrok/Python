from math import sqrt

def is_prime(liczba):
    if liczba <= 1:
        return False
        return print(False)
    
    for dzielnik in range(2, int(sqrt(liczba)) + 1):
        if liczba % dzielnik == 0:
            return False
            return print(False)
    return True
    return print(True)
    
is_prime(3)

# Pomijając zwracanie printów, brak zastrzeżeń. Brawo!

# (+2 / 2)