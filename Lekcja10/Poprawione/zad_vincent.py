# ZADANIE 1
def prostokat(bok_a, bok_b):
    pole = bok_a * bok_b
    print(pole)

prostokat(7,5)
# Bardzo ładnie :) (1/1)

# ZADANIE 2
def join(lacznik, teksty):
    print(lacznik.join(teksty))

join("*", ["kiełbasa", "bułka", "keputch"])
# Jest OK, metoda str.join, której tu użyłeś, nie koliduje z zadeklarowaną funkcją join(). Ładnie zrobione!
# (3/3)

# ZADANIE 3
def info(imie, wiek, wzrost):
    print(f"Hej, jestem {imie}, mam {wiek} lat i {wzrost * 100:.0f}cm wzrostu")

info("Janek", 40, 1.8)

# (2/2) (+0.5 za ominięcie pułapki - zad 4)

# Bardzo ładnie B) 