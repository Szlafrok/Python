# Krok 1: Pobieramy operację od użytkownika
operacja = input("Wybierz operację (+, -, *, /, //, %): ")

# Krok 2: Sprawdzamy, czy operacja jest prawidłowa
if operacja not in ["+", "-", "*", "/", "//", "%"]:
    print("Błędna operacja! Wybierz jedną z podanych: +, -, *, /, //, %.")
else:
    # Krok 3: Pobieramy liczby od użytkownika
    try:
        liczba1 = float(input("Podaj pierwszą liczbę: "))
        liczba2 = float(input("Podaj drugą liczbę: "))
        
        # Krok 4: Sprawdzamy, czy nie zachodzi dzielenie przez 0
        if operacja in ["/", "//", "%"] and liczba2 == 0:
            print("Błąd: dzielenie przez zero jest niedozwolone!")
        else:
            # Krok 5: Obliczamy wynik w zależności od wybranej operacji
            if operacja == "+":
                wynik = liczba1 + liczba2
            elif operacja == "-":
                wynik = liczba1 - liczba2
            elif operacja == "*":
                wynik = liczba1 * liczba2
            elif operacja == "/":
                wynik = liczba1 / liczba2
            elif operacja == "//":
                wynik = liczba1 // liczba2
            elif operacja == "%":
                wynik = liczba1 % liczba2

            # Wyświetlamy wynik
            print(f"Wynik: {wynik}")

    except ValueError:
        print("Błąd: Wprowadzono niepoprawną liczbę!")
    except ZeroDivisionError: # Dopisałem sobie, żeby Wam coś zaprezentować
        print("Nie wolno dzielić przez 0!")

# Bardzo ładnie! 3/3

# Razem 6/6 plusów.