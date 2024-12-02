# Pobranie wysokości od użytkownika
wysokosc = int(input("Podaj wysokość choinki: "))

# Generowanie choinki
for i in range(1, wysokosc + 1):  # Iterujemy od 1 do wysokości
    spacje = " " * (wysokosc - i)  # Liczba spacji z lewej strony
    gwiazdki = " ".join(["*"] * i)  # Gwiazdki z odstępami
    print(spacje + gwiazdki)  # Łączenie i wypisanie

# Bardzo ładnie!

# 4 / 4