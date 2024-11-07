# ZADANIE 1

PIN = "1987"
HASLO = "fredi_fnaf"

pin_input = input("Podaj PIN: ")
if pin_input == PIN:
    haslo_input = input("Podaj hasło: ")
    if haslo_input == HASLO:
        print("Zalogowano!")
    else:
        print("Błędne hasło")
else:
    print("Błędny pin")

# UWAGA: Lepiej jest trzymać kod PIN w stringu, ponieważ umożliwia to nam
# podanie kodu zaczynającego się od zer! Np. 0015

# ZADANIE 2

oc_1 = int(input("Podaj ocenę z PRZED"))
oc_2 = int(input("Podaj ocenę z PRZED"))
oc_3 = int(input("Podaj ocenę z PRZED"))
oc_4 = int(input("Podaj ocenę z PRZED"))
oc_5 = int(input("Podaj ocenę z PRZED"))

oc_z = int(input("Zachowanie: "))

sr = (oc_1 + oc_2 + oc_3 + oc_4 + oc_5) / 5

if sr >= 4.75 and oc_z >= 5:
    print("Pasek na świadectwie")
else:
    print("Brak paska")
print(f"Średnia wynosi {sr}")