operacja = input("Wybierz rodzaj działania: ")

if operacja not in ["+", "-", "*", "/", "//", "%"]:
    print("Nieprawidłowy rodzaj działania!")
    exit()

liczba_1 = float(input("Wprowadź 1 liczbę: "))
liczba_2 = float(input("Wprowadź 2 liczbę: "))

if operacja == "+":
    print(f"Wynik działania to {liczba_1 + liczba_2}")
elif operacja == "-":
    print(f"Wynik działania to {liczba_1 - liczba_2}")
elif operacja == "*":
    print(f"Wynik działania to {liczba_1 * liczba_2}")
else:
    if liczba_1 == 0 or liczba_2 == 0:
        print("Nie da się dzielić przez zero, wprowadź liczbę większą od zera.") # sprytnie
    else:
        if operacja == "/":
            print(f"Wynik działania to {liczba_1 / liczba_2}")
        elif operacja == "//":
            print(f"Wynik działania to {liczba_1 // liczba_2}")
        else:
            print(f"Wynik działania to {liczba_1 % liczba_2}")

# Bardzo ładnie :>

# 3/3 za to zadanie, razem 6/6 plusów ;)