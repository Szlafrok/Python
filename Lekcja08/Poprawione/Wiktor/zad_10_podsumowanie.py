# zadanie 7, 10

# Funkcja sprawdzająca, czy liczba jest doskonała
def czy_liczba_doskonala(liczba): # Ładna definicja!
    suma_dzielnikow = 0
    for i in range(1, liczba):  # Iterujemy przez liczby mniejsze od podanej
        if liczba % i == 0:  # Sprawdzamy, czy liczba dzieli się bez reszty
            suma_dzielnikow += i                            
    return suma_dzielnikow == liczba  # Porównanie sumy dzielników z liczbą // Super!

# Pobranie liczby od użytkownika
n = int(input("Podaj liczbę naturalną: "))

# Sprawdzenie, czy liczba jest doskonała
if czy_liczba_doskonala(n):
    print(f"Liczba {n} jest liczbą doskonałą.")
else:
    print(f"Liczba {n} nie jest liczbą doskonałą.")

# Zadanie rozwiązane książkowo wręcz B)
# 3 / 3

# ---- PODSUMOWANIE ----

# Zadania 1-6 liczę możliwie najbardziej na korzyść dla Was

# ZAD 1: 4.5  / 4       Obowiązkowe A
# ZAD 2: 3.75 / 4       Zad dod - 7
# ZAD 3: 4    / 4       Obowiązkowe B
# ZAD 4: 4    / 4       Obowiązkowe C
# ZAD 5: 4    / 4       Obowiązkowe D
# ZAD 6: 4    / 4       Zad dod - 8

# Dodatkowe:

# ZAD 7:  +2.5 / 2.5
# ZAD 8:  +1.5 / 1.5
# ZAD 9:  +0   / 2
# ZAD 10: +3   / 3

# Razem:
#   Obowiązkowe: 16.5 / 16.0
#   Dodatkowe:   +7 pkt
