LIMIT = 1200 # maklsymalne saldo konta
PIN = 1234

def glowne_menu() -> None: # Funkcja printuje opcje dla użytkownika
    print("Proszę wprowadzić liczbę odpowiednią dla operacji: ")
    print("1. Wpłata")
    print("2. Wypłata")
    print("3. Sprawdź stan konta")
    print("4. Zakończ")
    return # to samo co return None

def wczytaj_wybor_uzytkownika() -> int: # Funkcja wczytuje i zwraca numer wybranej opcji
    return int(input("Proszę podać wybór: "))

def pobierz_kwote() -> float: # Wczytuje i zwraca kwotę do wpłaty/wypłaty. Nie obsługuje samej wpłaty ani wypłaty.
        return float(input("Podaj kwotę większą od 0: "))

def wplata(poprzednie_saldo: float) -> float: # Funkcja zwracająca obecne saldo po wpłacie przez użytkownika
    kwota = pobierz_kwote()
    if poprzednie_saldo + kwota > LIMIT:
        print(f"Nie można wpłacić tej kwoty, saldo przekroczy limit {LIMIT}.")
        return poprzednie_saldo
    wynik = poprzednie_saldo + kwota
    pokaz_stan_konta(wynik) 
    return wynik

def pokaz_stan_konta(obecne_saldo: float) -> None: # Informacja o ob. stanie konta
    print(f"Twój stan konta: {obecne_saldo}")
    return

def wyplata(obecne_saldo: float) -> float: # Obsługa wypłaty pieniędzy
    kwota = pobierz_kwote()
    if obecne_saldo >= kwota: 
        wynik = obecne_saldo - kwota
        pokaz_stan_konta(wynik)
        return wynik # Zwraca obecne saldo po wypłacie pieniędzy (powodzenie)
    else:
        print("Masz za mało pieniędzy") # Zwraca obecne saldo po próbie wypłaty pieniędzy
        return obecne_saldo

def pobierz_pin() -> bool:
    for proba in range(3):
        kod_pin = input("wprowadź pin do konta: ")
        if kod_pin == PIN:
            print("PIN jest poprawny. masz dostęp do konta.")
        else:
            print(f'Niepoprawny PIN pozostało Prób: {2 - proba} ')
    print('Trzykronie wprowadzono zły PIN. Dostęp do konta został zablokowany.')
    return False


saldo = 0
wybor = 0

while wybor != 4:
    if not pobierz_pin(): exit()
    glowne_menu()
    wybor = wczytaj_wybor_uzytkownika()

    if wybor == 1: # Wpłata
        saldo = wplata(saldo)
    elif wybor == 2: # Wypłata
        saldo = wyplata(saldo)
    elif wybor == 3: # Sprawdzenie stanu konta
        pokaz_stan_konta(saldo)
    elif wybor == 4:
        print("Zamykanie aplikacji...")
    else:
        print("Nieprawidłowy wybór")
exit() # Koniec projektu

# Zadanie 1: (3/3)
# Zadanie 2: (3/4)