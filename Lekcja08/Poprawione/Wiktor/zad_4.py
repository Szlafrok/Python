# Pobranie danych od użytkownika
wysokosc = int(input("Podaj wysokość prostokąta: "))
szerokosc = int(input("Podaj szerokość prostokąta: "))
czy_pusty = input("Czy prostokąt ma być pusty w środku? (tak/nie): ").strip().lower() == "tak"

# Generowanie prostokąta
if czy_pusty:
    for i in range(wysokosc):
        if i == 0 or i == wysokosc - 1:
            # Pierwszy i ostatni wiersz pełny
            print("■" * szerokosc)
        else:
            # Środkowe wiersze z pustym środkiem
            print("■" + " " * (szerokosc - 2) + "■" if szerokosc > 1 else "■") # Spoko zrobiony warunek :)
else:
    # Pełny prostokąt
    for _ in range(wysokosc): # Krótko i na temat ;)
        print("■" * szerokosc)


# Elegancko B)

# 4 / 4