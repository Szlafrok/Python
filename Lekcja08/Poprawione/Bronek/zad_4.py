wysokosc = int(input("Podaj wysokość: "))
szerokosc = int(input("Podaj szerokość: ")) # Tu był niedomknięty cudzysłów :/
czy_pusty = input("Czy prostokąt ma być pusty? (tak/nie): ").strip().lower() == "tak"

for i in range(wysokosc):
    if i == 0 or i == wysokosc - 1 or not czy_pusty:
        print("■" * szerokosc)
    else:
        print("■" + " " * (szerokosc - 2) + "■") # Tutaj nawias, poza tym fragment >>  + "■" << powinien być poza nawiasem, w którym wyliczasz szerokość.

# Masz dwa błędy nieuwagi i drobny błąd w obliczeniach, który w zasadzie jest również błędem nieuwagi.
# Podejście bardzo dobre, ale przed wysłaniem wystarczyło uruchomić program, aby wyeliminować problemy!

# Odczyt danych 0.25 / 0.50
# Drukowanie prostokąta 2 / 2
# Dwa warianty 1.0 / 1.5
# Razem 3.25/4, liczę do dodatkowych!

# Podsumowanie w zad 10