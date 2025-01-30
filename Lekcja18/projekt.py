# W DANEJ TURZE:

# - Losujemy kości
# - Sprawdzamy, czy chcemy przerzucać (2 razy maksymalnie)
# ---- Jeżeli tak, wybieramy te, które chcemy przerzucić
# - Wybieramy rubrykę do wpisania punktów
# - Punkty się naliczają

# Po wyczerpaniu miejsc:

import random


def rzuc_koscmi(wybrane: str = "12345") -> None:
    for i in wybrane:
        kosci[int(i) - 1] = random.randint(1, 6)

def pokaz_kosci() -> None:
    print("_____________________")
    for i in range(len(kosci)):
        print(f"{i + 1}. {kosci[i]}") # Proszę uzupełnić tego printa tak, aby funkcja wypisała wszystkie wartości
    print("_____________________") # kości z ich numerami

def pokaz_rubryki() -> None:
    print("_____________________")
    for i in range(len(numery_punktow)):
        print(f"{i+1}. {numery_punktow[i]} - {punkty[i]}")
    print("_____________________")

def czy_przerzucamy() -> bool:
    odp = input("Czy chcesz przerzucać kości? (t / n): ")
    # Proszę napisać instrukcję warunkową, która zwróci True, jeżeli chcemy przerzucać
    # lub False, jeżeli nie chcemy.
    if odp == "t":
        return True
    else:
        return False

def wybierz_przerzuty() -> str:
    return input("Podaj kości do przerzucenia. Wymień ich numery bez spacji: ")

kosci = [0] * 5 # [0, 0, 0, 0, 0]

numery_punktow = ["Jedynki", "Dwójki", "Trójki", "Czwórki", "Piątki", "Szóstki"]
punkty = ["[Wolne]"] * 6


for tura in range(6):
    rzuc_koscmi()
    pokaz_kosci()

    przerzuty = 2
    while przerzuty > 0:
        if czy_przerzucamy():
            wybrane = wybierz_przerzuty()
            rzuc_koscmi(wybrane)
            pokaz_kosci()
            przerzuty -= 1
        else:
            przerzuty = 0

    pokaz_rubryki()
    