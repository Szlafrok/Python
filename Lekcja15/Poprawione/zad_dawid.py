#zadanie 1 (0.75 / 1.00) (+1 za komentarze)
def not_prime(n: int) -> bool:
    if n < 2:
        return False  # Liczby mniejsze niż 2 są złożone // (!!!) liczby <2 nie są ani pierwsze, ani złożone!
    for i in range(2, int(n**0.5) + 1):  # Sprawdzamy dzielniki od 2 do √n
        if n % i == 0:
            return True  # Liczba ma dzielnik -> jest złożona
    return False  # Liczba jest pierwsza

# Przykład użycia:
wynik = not_prime(2)
print(f"Zadanie domowe 1: Wynik = {wynik}")


#zadanie 2
# Konwersja dziesiętna → trójkowy

def trojeczka(n: int) -> str: # (2/2) (Brak komentarzy)
    if n == 0:
        return "0" # Przypadek szczególny ;)
    result = ""
    while n > 0:
        result = str(n % 3) + result # OK!
        n //= 3
    return result

# Przykład użycia:
wynik = trojeczka(15)
print(f"Zadanie domowe 2: Wynik = {wynik}")


# Zadanie 3.1: Liczba cwanych słów (3.5 / 3.5) (+1.5 za komentarze)

def cwaniak(wyrazy: list) -> int:
    n = len(wyrazy)  # Liczba słów w liście
    cwane = [False] * n  # Lista logiczna oznaczająca cwane słowa
    for i, word in enumerate(wyrazy):
        reversed_word = word[::-1]
        if word == reversed_word or reversed_word in wyrazy:  # Palindrom lub odwrócenie jest w liście
            cwane[i] = True
    return sum(cwane)  # Zliczamy True w liście cwane

# Przykład użycia:
wynik = cwaniak(["kot", "kot", "pies", "pies", "owocowo", "tok"])
print(f"Zadanie domowe 3.1: Wynik = {wynik}")


# Zadanie 3.2: Czy wynik funkcji może wynosić 0 lub 1? (+1/1)
'''
a) Czy wynik może być 0? (+)
Tak, wynik może wynosić 0. Dzieje się tak, gdy żadna para słów (ani palindrom) nie występuje w liście.
Przykład: cwaniak(["abc", "def", "ghi"]) zwróci 0, ponieważ żadne słowo nie jest cwane.

#------------------------------------------

b) Czy wynik może być 1? (+)
Tak, wynik może wynosić 1. Dzieje się tak, gdy w liście występuje tylko jedno słowo będące palindromem.
Przykład: cwaniak(["aba", "xyz"]) zwróci 1, ponieważ tylko "aba" jest cwane.

#------------------------------------------

Podsumowanie:
Wynikami funkcji mogą być zarówno 0, jak i 1.
'''