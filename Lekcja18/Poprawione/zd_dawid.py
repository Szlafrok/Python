# W DANEJ TURZE:

# - Losujemy kości
# - Sprawdzamy, czy chcemy przerzucać (2 razy maksymalnie)
# ---- Jeżeli tak, wybieramy te, które chcemy przerzucić
# - Wybieramy rubrykę do wpisania punktów
# - Punkty się naliczają

# Po wyczerpaniu miejsc:

import random

# Funkcja rzucająca kośćmi. Domyślnie rzucamy wszystkimi kośćmi (wybrane: "12345"),
# ale można podać tylko numery kości, które chcemy ponownie rzucić.
def rzuc_koscmi(wybrane: str = "12345") -> None:
    # Dla każdej pozycji w łańcuchu 'wybrane' (np. "13" -> rzucamy kość nr 1 i 3)
    for i in wybrane:
        # Przypisujemy do odpowiedniego indeksu nową losową wartość z zakresu 1-6
        kosci[int(i) - 1] = random.randint(1, 6)

# Funkcja wyświetlająca aktualny stan kości z ich numerami.
def pokaz_kosci() -> None:
    print("_____________________")
    # Iterujemy po liście kości i wypisujemy każdą wartość wraz z numerem (indeks + 1)
    for i in range(len(kosci)):
        print(f"{i + 1}. {kosci[i]}")
    print("_____________________")

# Funkcja wyświetlająca rubryki (kategorie punktowe) oraz obecne wyniki.
def pokaz_rubryki() -> None:
    print("_____________________")
    # Iterujemy po dostępnych rubrykach i wypisujemy ich numer, nazwę oraz przypisane punkty.
    for i in range(len(numery_punktow)):
        print(f"{i+1}. {numery_punktow[i]} - {punkty[i]}")
    print("_____________________")

# Funkcja pytająca gracza, czy chce przerzucać kości.
def czy_przerzucamy() -> bool:
    odp = input("Czy chcesz przerzucać kości? (t / n): ")
    # Jeśli gracz odpowie "t", zwracamy True, w przeciwnym razie False.
    if odp == "t":
        return True
    else:
        return False

# Funkcja pobierająca od gracza numery kości do przerzutu, wpisane jako ciąg bez spacji.
def wybierz_przerzuty() -> str:
    return input("Podaj kości do przerzucenia. Wymień ich numery bez spacji: ")

# Funkcja pobierająca od gracza numer rubryki, do której chce przypisać punkty.
def wybierz_rubryke() -> int:
    return int(input("Podaj rubrykę, w którą chcesz wpisać punkty: "))

# Funkcja wyznaczająca wynik dla danej rubryki.
# Sumujemy wartość kości, które odpowiadają numerowi rubryki (np. dla rubryki "Jedynki", sumujemy tylko jedynki).
def wyznacz_wynik(rub: int) -> int:
    res = 0
    for k in kosci:
        if k == rub:
            res += k
    return res

# Inicjalizacja listy kości - początkowo 5 kości ustawionych na 0.
kosci = [0] * 5  # [0, 0, 0, 0, 0]

# Lista dostępnych rubryk (kategorii) punktowych.
numery_punktow = ["Jedynki", "Dwójki", "Trójki", "Czwórki", "Piątki", "Szóstki"]
# Lista punktów dla każdej rubryki; początkowo każda rubryka jest wolna.
punkty = ["[Wolne]"] * 6

# Główna pętla gry: mamy 6 tur, czyli tyle rubryk, do których można wpisać punkty.
for tura in range(6):
    # Losujemy wszystkie kości na początku tury
    rzuc_koscmi()
    pokaz_kosci()

    # Gracz ma możliwość wykonania maksymalnie dwóch przerzutów
    przerzuty = 2
    while przerzuty > 0:
        # Sprawdzamy, czy gracz chce przerzucić kości
        if czy_przerzucamy():
            # Pobieramy numery kości, które chce przerzucić
            wybrane = wybierz_przerzuty()
            # Rzucamy tylko wybrane kości
            rzuc_koscmi(wybrane)
            pokaz_kosci()
            przerzuty -= 1
        else:
            # Jeśli gracz nie chce przerzucać, wychodzimy z pętli przerzutów
            przerzuty = 0

    # Po zakończeniu rzutów, wyświetlamy dostępne rubryki
    pokaz_rubryki()
    rubryka = wybierz_rubryke()

    # Sprawdzamy, czy wybrana rubryka jest wolna; jeśli nie, prosimy o ponowny wybór
    while punkty[rubryka - 1] != "[Wolne]":
        print("W tej rubryce już masz punkty!")
        rubryka = wybierz_rubryke()

    # Obliczamy wynik dla danej rubryki (suma wartości kości, które pasują do rubryki)
    wynik = wyznacz_wynik(rubryka)
    # Przypisujemy wynik do wybranej rubryki
    punkty[rubryka - 1] = wynik
    print(f"punkty w rubryce {numery_punktow[rubryka - 1]}: {wynik}")

# Po rozegraniu 6 tur gra się kończy
print("\n------KONIEC GRY ---")
# Wyświetlamy końcowy stan rubryk z punktami
pokaz_rubryki()

# Obliczamy sumę punktów z wszystkich rubryk
suma_punktow = sum([punkt if isinstance(punkt, int) else 0 for punkt in punkty])
# >>>>>>>>> Fajne dodatkowe zabezpieczenie ;) Choć z algorytmu wynika, że nie będzie konieczne :P
    
print(f"Suma punktów: {suma_punktow}")


# Bardzo dobrze napisane i wyczerpujące komentarze :D

# (4/4)