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
        print(f"{i + 1}. {kosci[i]}")
    print("_____________________")

def pokaz_rubryki() -> None:
    print("_____________________")
    for i in range(len(numery_punktow)):
        print(f"{i+1}. {numery_punktow[i]} - {punkty[i]}")
    print("_____________________")

def czy_przerzucamy() -> bool:
    odp = input("Czy chcesz przerzucać kości? (t / n): ")
    if odp == "t":
        return True
    else:
        return False

def wybierz_przerzuty() -> str:
    return input("Podaj kości do przerzucenia. Wymień ich numery bez spacji: ")


def wybierz_rubryke() -> int:
    return int(input("Podaj rubrykę, w którą chcesz wpisać punkty: "))


def wyznacz_wynik(rub: int) -> int:
    res = 0
    for k in kosci:
        if k == rub:
            res += k
    return res




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
    rubryka = wybierz_rubryke()
    
    while punkty[rubryka - 1] != "[Wolne]":
        print("W tej rubryce już masz punkty!")
        rubryka = wybierz_rubryke()

    bonus = wyznacz_wynik(rubryka)

    punkty[rubryka - 1] = bonus

print(f"Twój wynik to: {sum(punkty)}")