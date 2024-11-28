import random

# Losowanie liczby
wylosowana_liczba = random.randint(1, 10) # Powinno być 100000! 
proby = 0

print("Zgadnij wylosowaną liczbę z zakresu 1-100000!") #

while True:
    # Pobieranie liczby od użytkownika
    proba = int(input("Podaj liczbę: "))
    proby += 1

    # Sprawdzanie, czy liczba jest za duża, za mała, czy równa
    if proba < wylosowana_liczba:
        print("Za mała!")
    elif proba > wylosowana_liczba:
        print("Za duża!")
    else:
        print(f"Brawo! Zgadłeś liczbę {wylosowana_liczba} w {proby} próbach!")
        break

# Program zrobiony bardzo ładnie, zrobiłeś natomiast błąd nieuwagi - wczytujesz liczbę
# losową od 1 do 10, a nie od 1 do 100000.

# (3.75 / 4.00)