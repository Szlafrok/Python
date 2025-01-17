######### ZADANIE 1 (1.25 / 1.00) + 1 za wyczerpujące komentarze

from math import sqrt # importuje funkcje sqrt z modulu math

def not_prime(n: int) -> bool:
    # Sprawdza czy liczba jest mniejsza lub równa 1,
    # ponieważ liczby mniejsze lub równe 1 nie są liczbami pierwszymi ani złożonymi
    if n <= 1:
        return None # Przeczytałeś treść zadania lepiej niż ja ją zapamiętałem. Masz +0.25 XD
    
    # Sprawdza po kolei dzielniki od 2 do pierwiastka z n
    for dzielnik in range(2, int(sqrt(n)) + 1):
        # Jeżeli n jest podzielne przez dzielnik to jest liczbą złożoną i zwraca True
        if n % dzielnik == 0:
            return True
    return False

# Testowanie programu
wynik = not_prime(1)
print(f"Wynik = {wynik}")
# Bezbłędnie ;)



########### ZADANIE 2 (2/2) (+1 za wyczerpujące komentarze)

def trojeczka(n: int) -> str:
    # definiuje pustą listę na kolejne cyfry naszej liczby w systemie trójkowym
    liczba = []
    # Pętla powtarza się dopóki n jest większe od 0
    while n > 0:
        # Dodaje do listy resztę z dzielenia n przez 3
        liczba.append(n % 3)
        # Dzieli n przez 3 i zaokrągla wynik do liczby całkowitej
        n = n // 3
        # Zwraca listę jako stringa, ale odwróconą
    return "".join(map(str, (liczba [::-1]))) # Uwielbiasz korzystać ze skomplikowanych funkcji XD

# Testowanie programu
wynik = trojeczka(100)
print(f"Wynik = {wynik}")

# Bardzo ładnie!

############ ZADANIE 3 (3.50 / 3.50) (+1.5 za wyczerpujące komentarze)

def cwaniak(wyrazy: list) -> int:
    # Sprawdza długość listy wyrazy i tworzy listę o tej samej długości z wartościami False
    n = len(wyrazy)
    cwane = [False] * n
    # Pętla po kolei sprawdza czy dany wyraz z listy wyrazy jest w odwróconej formie w liście wyrazy
    for i in range(n):
        if wyrazy[i][::-1] in wyrazy:
            # Jeżeli tak to zmienia wartość na True
            cwane[i] = True
    # Zwraca ilość wartości True w liście cwane
    return cwane.count(True) # A co gdyby użyć sum(cwane)? ;)

# Testowanie programu
wynik = cwaniak(["kot", "kot", "pies", "pies", "owocowo", "tok"])
print(f"Zadanie domowe 3.1: Wynik = {wynik}")

# Super!

# Łączna suma: 10.25 / 10.00