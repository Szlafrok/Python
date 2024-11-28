# Pobranie liczby od użytkownika
while True:
    try:
        liczba = float(input("Podaj dodatnią liczbę całkowitą: "))
        if liczba > 0 and liczba.is_integer():
            liczba = int(liczba)
            break
        else:
            print("Podaj dodatnią liczbę całkowitą!")
    except ValueError:
        print("To nie jest poprawna liczba!")

# Generowanie ciągu Fibonacciego
ciag_fibonacciego = []
a1, a2 = 0, 1

for _ in range(liczba): # Elegancko
    ciag_fibonacciego.append(a1)
    a1, a2 = a2, a1 + a2 # Bardzo eleganckie podstawienie ;)

# Wypisanie wyników
print(f"Pierwsze {liczba} elementów ciągu Fibonacciego: {', '.join(map(str, ciag_fibonacciego))}")


def alternatywnie(): # Dopisuję inne podejście w ramach ciekawostki ;)
    ciag = [0] * liczba
    ciag[0], ciag[1] = 0, 1
    for i in range(2, liczba):
        ciag[i] = ciag[i-1] + ciag[i-2]

# Zadanie zrobione bardzo dobrze i elegancko B)

# (4.0 / 4.0)