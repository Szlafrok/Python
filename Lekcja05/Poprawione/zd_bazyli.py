#zadanie 1


print("cennik")
miesiac = int(input("Podaj numer miesiąca:"))
if miesiac == 1 or miesiac == 2:
    print("Cena to $150")
elif miesiac == 3 or miesiac == 4 or miesiac == 11 or miesiac == 12:
    print("Cena to $199")
elif miesiac == 5 or miesiac == 6 or miesiac == 10:
    print("Cena to $249")
elif miesiac == 7 or miesiac == 8 or miesiac == 9:
    print("Cena to $299")
else:
    print("Błąd ----- Nie ma takiego miesiąca")

# Łącząc "miesiąc == 1 or 2" w warunek w ten sposób porównujesz 2 zdania logiczne połączone ORem:
# "miesiąc == 1" oraz "2". Nie możesz tego zrobić w ten sposób :P

# Możesz to zrobić w sposób podany w poprawce lub wykorzystując listy - tym jednak będziemy
# się zajmować dopiero za kilka tygodni: if miesiac in [3, 4] jest równoważne z if miesiac == 3 or miesiac == 4.

# Unikaj poza tym polskich znaków w deklarowaniu nazw zmiennych

# (plusy: 1,5 z 3)


#zadanie 2


operacja = input("Wybierz operację: ")

if not (operacja == "+" or operacja == "-" or operacja == "*" or operacja == "/" or operacja == "//" or operacja == "%"):
    print("Nieprawidłowe działanie!")
    exit() # Brakowało

liczba_1 = float(input("Wprowadź liczbę 1: "))
liczba_2 = float(input("Wprowadź liczbę 2: "))

if operacja == "+":
    print(f"Wynik działania to {liczba_1 + liczba_2}")
elif operacja == "-":
    print(f"Wynik działania to {liczba_1 - liczba_2}")
elif operacja == "*":
    print(f"Wynik działania to {liczba_1 * liczba_2}")
elif operacja == "/" and not liczba_2 == 0: # Przy jakimkolwiek dzieleniu nie musisz sprawdzać, czy DZIELNIK jest równy 0. Jedynie dzielna nie może być.
    print(f"Wynik działania to {liczba_1 / liczba_2}")
elif operacja == "//" and not liczba_2 == 0:
    print(f"Wynik działania to {liczba_1 // liczba_2}")
elif operacja == "%" and not liczba_2 == 0:
    print(f"Wynik działania to {liczba_1 % liczba_2}")

# Poza brakiem exit() ok
# (plusy: 2,5 z 3)

# Razem plusów: 4/6