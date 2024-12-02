# ZADANIA DOMOWE SĄ POD PRZYKŁADAMI!

# PRZYKŁAD 1
# Proszę napisać funkcję, która oceni, czy dana liczba naturalna jest parzysta

def parzysta(n):
    if n % 2 == 0:
        print("Parzysta")
    else:
        print("Nieparzysta")

# PRZYKŁAD 2
# Proszę napisać funkcję, która obliczy pole trapezu o podstawach a i b oraz wysokości h

def pole(a, b, h):
    print((a + b) * h / 2)

# PRZYKŁAD 3
# Proszę napisać funkcję, która obliczy średnią arytmetyczną liczb zawartych w liście.
# Lista zawiera wyłącznie liczby dziesiętne i całkowite.

def srednia(liczby):
    print(sum(liczby) / len(liczby))

# ZADANIE DOMOWE
# Proszę zaimplementować funkcje:

# 1) (1 pkt) funkcję prostokat(a, b), która przyjmuje jako argumenty boki prostokąta a oraz b
#    i wypisuje do konsoli jego pole 

# 2) (3 pkt) funkcję join(lacznik, teksty), która przyjmuje jako argumenty:
#       - stringa lacznik
#       - listę stringów teksty
#    i wypisuje pojedynczy ciąg złożony z kolejnych elementów listy teksty, połączonych
#    pomiędzy sobą łącznikami.
#    Przykłady:

#    join("/", ["bardzo", "lubię", "ciastka"]) -> "bardzo/lubię/ciastka"
#    join("-", ["i have", "your food", "sir"]) -> "i have-your food-sir"
#    join("%", ["pojedynczy element"])         -> "pojedynczy element"

#    Wskazówka: użyj argumentu end = "" w funkcji print()

# 3) (2 pkt) funkcję info(imie, wiek, wzrost), która przyjmuje jako argumenty:
#       - stringa imie
#       - liczbę całkowitą wiek,
#       - liczbę dziesiętną wzrost (podany w metrach)
#    i na bazie tych danych wypisuje do konsoli napis:
#    Hej, jestem (imię), mam (wiek) lat i (wzrost)cm wzrostu

#    Przykład: Dla danych: imie = "Piotrek", wiek = 20, wzrost = 180
#    otrzymujemy "Hej, jestem Piotrek, mam 20 lat i 180cm wzrostu"


# *4) (+0.5 pkt) Proszę nie wpaść na pewną prostą pułapkę ukrytą w zadaniu 3 :)


# Zadanek jest kilka, ale są mega króciutkie i dobre na wyćwiczenie funkcji. 
# Powodzenia!! :D