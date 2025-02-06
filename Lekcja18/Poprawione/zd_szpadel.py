# W DANEJ TURZE:

# - Losujemy kości
# - Sprawdzamy, czy chcemy przerzucać (2 razy maksymalnie)
# ---- Jeżeli tak, wybieramy te, które chcemy przerzucić
# - Wybieramy rubrykę do wpisania punktów
# - Punkty się naliczają

# Po wyczerpaniu miejsc:

import random 

# losowanie kości wyświetlanie ich oraz rubryk

def rzuc_koscmi(wybrane: str = "12345") -> None: # funkcja losuje kości na podstawie podanych indeksów
    for i in wybrane:
        kosci[int(i) - 1] = random.randint(1, 6) # random.randint() losuje cyfry z podanego zakresu

def pokaz_kosci() -> None: # printuje wszystkie kości po kolei
    print("_____________________")
    for i in range(len(kosci)):
        print(f"{i + 1}. {kosci[i]}")
    print("_____________________")

def pokaz_rubryki() -> None: # printuje wszystkie rubryki po kolei, włącznie z ich punktami
    print("_____________________")
    for i in range(len(numery_punktow)):
        print(f"{i+1}. {numery_punktow[i]} - {punkty[i]}")
    print("_____________________")

# decyzje należące do gracza: czy chce przrucać, które kości przerzucać, którą chce wybrać rubrykę

def czy_przerzucamy() -> bool: # funkcja wczytuje czy chcemy dalej przerzucać i zwraca boola
    odp = input("Czy chcesz przerzucać kości? (t / n): ")
    if odp == "t":
        return True
    else:
        return False

def wybierz_przerzuty() -> str: # wczytuje indeksy kości do przerzucenia i zwraca je w stringu
    return input("Podaj kości do przerzucenia. Wymień ich numery bez spacji: ")


def wybierz_rubryke() -> int: # wczytuje numer rubryki i ją zwraca
    return int(input("Podaj rubrykę, w którą chcesz wpisać punkty: "))

# wyznacz wynik

def wyznacz_wynik(rub: int) -> int: # funkcja dodaje do wyniku każdą kość z kosci która jest równa wybranej rubryce i zwraca wynik
    res = 0
    for k in kosci:
        if k == rub:
            res += k
    return res

# definiuje wszystkie potrzebne listy

kosci = [0] * 5 # przygotowana wcześciej lista na kości

numery_punktow = ["Jedynki", "Dwójki", "Trójki", "Czwórki", "Piątki", "Szóstki"] # nazwy rubryk
punkty = ["[Wolne]"] * 6 # przygotowana wcześniej lista na punkty

# uruchamia grę i wszystkie jej komponenty oraz podaje końcowy wynik

for tura in range(6): # powtarzamy 6 razy, ponieważ mamy 6 tur
    rzuc_koscmi()
    pokaz_kosci()

    przerzuty = 2 # ustawia liczbę przerzutów
    while przerzuty > 0: # umożliwia przerzucanie aż do końca przrzutów
        if czy_przerzucamy():
            wybrane = wybierz_przerzuty()
            rzuc_koscmi(wybrane)
            pokaz_kosci()
            przerzuty -= 1 # odejmuje 1 przrzut aby nie można było rzucać w nieskończoność
        else:
            przerzuty = 0 # w przypadku gdy nie gracz nie chce przerzucić ustawia przerzuty na zero aby pętla się zakończyła

    pokaz_rubryki()
    rubryka = wybierz_rubryke()
    
    while punkty[rubryka - 1] != "[Wolne]": # jeżeli rubryka jest już zajęta gracz wybiera ponownie
        print("W tej rubryce już masz punkty!")
        rubryka = wybierz_rubryke()

    bonus = wyznacz_wynik(rubryka)

    punkty[rubryka - 1] = bonus # w wybranej rubryce zamienia [wolne] na bonus

print(f"Twój wynik to: {sum(punkty)}")



# (4/4)