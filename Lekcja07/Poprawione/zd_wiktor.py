import math  # Importujemy bibliotekę math, aby móc skorzystać z funkcji sqrt().

# Wczytanie liczby naturalnej od użytkownika
number = int(input("Podaj liczbę naturalną: "))

# Sprawdzamy czy liczba jest większa od 1
if number <= 1:
    print("Liczba nie jest ani pierwsza, ani złożona.")  # Liczby 0 i 1 nie są liczbami pierwszymi ani złożonymi.
    exit()

# Zakładamy, że liczba jest pierwsza, dopóki nie znajdziemy dzielnika
is_prime = True

# Sprawdzamy dzielniki liczby od 2 do pierwiastka kwadratowego z liczby
for i in range(2, int(math.sqrt(number)) + 1):
    if number % i == 0:
        is_prime = False  # Jeśli znajdziemy dzielnik, ustawiamy is_prime na False i przerywamy pętlę.
        break

# Wyświetlamy wynik
if is_prime:
    print("Liczba jest pierwsza.")
else:
    print("Liczba jest złożona.")




exit()  # Zakończenie programu

# Zadanie i zadania dodatkowe rozwiązane w pełni prawidłowo. Gratuluję ;)

# 5 pkt + 4 pkt = 9 pkt