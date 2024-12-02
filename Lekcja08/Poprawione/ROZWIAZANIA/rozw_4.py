czy_pusty = input("Czy prostokąt jest pusty? (t/n): ") == 't'

wysokosc = int(input("Podaj wysokość: "))
szerokosc = int(input("Podaj szerokość: "))

for i in range(wysokosc):
    if i in [0, wysokosc-1] or not czy_pusty or szerokosc < 3:
        print(f"{"■" * szerokosc}" )
    else:
        print(f"■{" " * (szerokosc-2)}■")