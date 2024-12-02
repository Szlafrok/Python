while True: # +
    try: 
        wysokosc = int(input("Podaj wysokość prostokąta: "))
        szerokosc = int(input("Podaj szerokość prostokąta: "))
        break
    except ValueError:
        print("Zły typ danych, spróbuj ponownie")

while True: # +
    tryb = input("Wybierz tryb (pusty/pełny): ").lower()
    if tryb == "pusty":
        czy_pusty = True
        break
    elif tryb == "pełny":
        czy_pusty = False
        break
    else:
        print("Nie ma takiej opcji, spróbuj ponownie")


if czy_pusty:
    for i in range(1, wysokosc + 1):
        for j in range(1, szerokosc + 1):
            if i == 1 or i == wysokosc or j == 1 or j == szerokosc:
                print("⬛", end="")
            else:
                print("  ", end="") # Nie takiej metody się spodziewałem, ale jak najbardziej działa :P
        print()
else:
    for i in range(1, wysokosc + 1):
        for j in range(1, szerokosc + 1):
            print("⬛", end="")
        print()

# Zadanie bezbłędne, gratki!

# 4 / 4