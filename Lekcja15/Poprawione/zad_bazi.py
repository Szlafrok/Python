#z1) (0.75 / 1.00) (+1 za komentarze)
from math import sqrt
def not_prime(n):
    if n <= 1:
        return True  # Liczby <= 1 są uznawane za złożone, bo nie są liczbami pierwszymi // Nie!
    for i in range(2, int(sqrt(n)) + 1):  # Sprawdzamy dzielniki od 2 do pierwiastka z n
        if n % i == 0:
            return True  # Jeśli n jest podzielna przez i, to jest złożona
    return False  # Jeśli nie znaleziono dzielnika, to liczba jest pierwsza
print(not_prime(int(input("Podaj liczbę."))))

# Jedyny błąd - linijka 5. Poza tym klasa B)




#z2) (2/2) + 1 za komentarze
def trojeczka(n: int) -> str:
    trójkowy = ""
    
    while n > 0:
        reszta = n % 3
        trójkowy = str(reszta) + trójkowy  # Dodajemy resztę na początek wyniku
        n = n // 3  # Dzielenie całkowite przez 3
    
    return trójkowy
print(trojeczka(int(input("Podaj liczbę w systemie dziesiętnym."))))

# Elegancko :D


# Suma: 4.75 / 5.00 za te zadania ;)