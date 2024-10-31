try:
    miesiac = int(input("Podaj numer miesiąca (1-12): "))
    if miesiac in [1, 2]:
        koszt = 150
    elif miesiac in [3, 4]:
        koszt = 199
    elif miesiac in [5, 6]:
        koszt = 249
    elif miesiac in [7, 8, 9]:
        koszt = 299
    elif miesiac == 10:
        koszt = 249
    elif miesiac in [11, 12]:
        koszt = 199
    else:
        print("Nieprawidłowy numer miesiąca! Podaj liczbę od 1 do 12.")
        exit()

    print(f"Koszt atrakcji w wybranym miesiącu wynosi: ${koszt}")

except ValueError:
    print("Nieprawidłowy format! Podaj numer miesiąca jako liczbę całkowitą.")

# Bezbłędnie! 3 z 3 plusów. Dobre użycie list, ale dopiero będziemy się w nie zagłębiać ;)
# Mogłeś poza tym zwinąć te warunki w przypadkach, gdzie w dwóch różnych weryfikacjach dostawaliśmy tę samą wartość


try:
    liczba1 = float(input("Podaj pierwszą liczbę: "))
    liczba2 = float(input("Podaj drugą liczbę: "))
    operacja = input("Wybierz działanie (+, -, , /, //, %): ")

    if operacja == '+':
        wynik = liczba1 + liczba2
    elif operacja == '-':
        wynik = liczba1 - liczba2
    elif operacja == '':
        wynik = liczba1 * liczba2
    elif operacja == '/':
        if liczba2 == 0:
            print("Błąd! Nie można dzielić przez 0.")
        else:
            wynik = liczba1 / liczba2
    elif operacja == '//':
        if liczba2 == 0:
            print("Błąd! Nie można dzielić przez 0.")
        else:
            wynik = liczba1 // liczba2
    elif operacja == '%':
        if liczba2 == 0:
            print("Błąd! Nie można dzielić przez 0.")
        else:
            wynik = liczba1 % liczba2
    else:
        print("Nieprawidłowa operacja. Wybierz jedną z: +, -, *, /, //, %.")
        exit()
    print(locals())
    if 'wynik' in locals(): #Miałeś tu wcięcie, co produkowało błąd. Poza tym bardzo ładnie!
        print(f"Wynik: {wynik}")

except ValueError:
    print("Nieprawidłowy format! Podaj liczby w formacie liczby zmiennoprzecinkowej.")

# Plusów: 2,5 / 3


# Razem plusów: 6/6 w zaokrągleniu z 5,5