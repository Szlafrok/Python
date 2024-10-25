
print("Wiedźmin lubi kremówki")

# Uwaga - to nie będzie poprawnie pod kątem czystego Pythona, to tylko przykład!

zdanie = False

if zdanie:
    print("Ale takie bez rodzynek")
else:
    print("Jeszcze jak!")

warunek = 4

if warunek == 0:
    print("pan_tadeusz_lubi_adama_mickiewicza")

    if warunek > 0:
        print("")

    elif warunek == 1:
        print("o ja")

    print("o ty")

elif warunek == 2:
    print("idzie na grzyby")

else:
    print("lubi też pierogi")

# Sprawdzamy, czy liczba jest parzysta?

# x = int(input())

# if x % 2 == 0:
#     print("Liczba jest parzysta")
# else:
#     print("Liczba jest nieparzysta")


# Sprawdź, czy dzielenie jest możliwe.

dzielna = int(input("Podaj dzielną: "))
dzielnik = int(input("Podaj dzielnik: "))

if dzielnik == 0:
    print("Error!")
else:
    print(f"Wynik to {dzielna/dzielnik}")

# ---------- ZADANIE SAMODZIELNE ------------

# Proszę napisać program, który sprawdzi, czy:
#   - podany wzrost jest większy lub równy 120
#   - podany wzrost jest mniejszy lub równy 200
#   - podany wiek jest większy niż 12
# i na podstawie tego określi, czy możemy udać się na kolejkę górską.

wzrost = int(input("Podaj wzrost: "))
wiek = int(input("Podaj wiek: "))

if wiek > 12 and wzrost >= 120 and wzrost <= 200:
    print("Możesz wejść na kolejkę")
else:
    print("Nuh uh")


if wzrost >= 120 and wzrost <= 200:
    if wiek > 12:
        print("Możesz iść jeździć! ADAM MAŁYSZ 102 METRY")
    else:
        print("Nie możesz jechać, jesteś zbyt młody")
        print("(Ale wzrost masz w porządku)")
else:
    print("Jesteś za niski lub za wysoki")

# Dni tygodnia z liczby na słowo

dzien = int(input("Podaj dzień: "))

if dzien == 1:
    print("Poniedziałek")
elif dzien == 2:
    print("Wtorek")
elif dzien == 3:
    print("Środa")
elif dzien == 4:
    print("Czwartek")
elif dzien == 5:
    print("Piątek")
elif dzien == 6:
    print("Sobota")
else:
    print("Niedziela")


# ZADANIE SAMODZIELNE

# Proszę ocenić, czy podana liczba jest liczbą dodatnią, ujemną, czy zerową.

liczba = float(input())

if liczba > 0:
    print("Dodatnia")
elif liczba < 0:
    print("Ujemna")
else:
    print("Liczba równa 0")