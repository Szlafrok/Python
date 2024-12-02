#zadanie 7
#zadanie 8
#zadanie 9
import math

# Pobranie liczby naturalnej większej od 2
n = int(input("Podaj liczbę naturalną większą od 2: "))

# Funkcja do obliczania liczby dzielników
def liczba_dzielnikow(n):
    dzielniki = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            dzielniki += 2 if i != n // i else 1
    return dzielniki

# Sprawdzamy, czy liczba dzielników jest nieparzysta
if liczba_dzielnikow(n) % 2 == 1:
    # Sprawdzamy, czy liczba jest kwadratem liczby naturalnej
    if int(math.sqrt(n))**2 == n:
        print(f"Liczba {n} ma nieparzystą liczbę dzielników i jest kwadratem liczby naturalnej.")
    else:
        print(f"Liczba {n} ma nieparzystą liczbę dzielników, ale NIE jest kwadratem liczby naturalnej (co jest sprzeczne z teorią).")
else:
    print(f"Liczba {n} nie ma nieparzystej liczby dzielników.")




# uzasadnienie
# tak może być, gdyż jest to pokazane i kocdzie powyżej

# Uzasadniasz to, rozliczając wskazane przypadki. Chodziło jednak o uzasadnienie dla DOWOLNEJ liczby, a tego w kodzie zrobić się nie da :/
# Wyjaśnienie pojawi się dziś na nagraniu!