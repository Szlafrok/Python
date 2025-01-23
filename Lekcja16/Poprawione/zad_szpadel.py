def glowne_menu() -> None: # Funkcja printuje opcje dla użytkownika
    print("Proszę wprowadzić liczbę odpowiednią dla operacji: ")
    print("1. Wpłata")
    print("2. Wypłata")
    print("3. Stan konta")
    print("4. Historia konta")
    print("5. Zakończ")
    return # to samo co return None

def sprawdzenie_pinu() -> None:
    blad = 0 # Liczba początkowych błędów
    print(PIN)
    while True: # jest jak najbardziej dobrze, poniżej pokażę Ci alternatywę ;)
        pin = pobierz_pin()
        #print(f"{pin} == {PIN}?")
        if pin != PIN:
            print(f"Zły pin, pozostało prób: {(N - 1) - blad}") # niepotrzebny nawias ;P
            blad += 1
            if blad == N: # Gdy błędów jest N wychodzimy
                exit()       
        else:
            break
    return
    # Bezbłędnie!

def wczytaj_wybor_uzytkownika() -> int: # Funkcja wczytuje i zwraca numer wybranej opcji
    return int(input("Proszę podać wybór: "))

def pobierz_kwote() -> float: # Wczytuje i zwraca kwotę do wpłaty/wypłaty. Nie obsługuje samej wpłaty ani wypłaty.
    return float(input("Podaj kwotę: "))

def pobierz_pin() -> str: # Zwraca wprowadzony kod PIN w formie stringa
    kod_pin = input("Wprowadź PIN do karty: ") # Błąd! Usunąłem robienie z tego inta.
    return kod_pin

def wplata(poprzednie_saldo: float) -> float: # Funkcja zwracająca obecne saldo po wpłacie przez użytkownika
    kwota = pobierz_kwote()
    wynik = poprzednie_saldo + kwota
    if wynik > LIMIT: 
        print("Nie możesz tyle wpłacić, przekroczysz limit konta.")
        stan_konta(poprzednie_saldo) # Zwracamy nie zmienione saldo, ponieważ przekroczyliśmy LIMIT
        return poprzednie_saldo
    else:
        historia.append((1, kwota, wynik)) # Dodajemy wpis do historii
        stan_konta(wynik) 
        return wynik
    # Super!

def stan_konta(obecne_saldo: float) -> None: # Informacja o ob. stanie konta
    print(f"Twój stan konta: {obecne_saldo}")
    return

def historia_konta(historia: list) -> None:
    for wpis in historia:
        if wpis[0] == 1:
            print(f"Wpłata {wpis[1]} zł - obecne saldo {wpis[2]} zł.")
        else:
            print(f"Wypłata {wpis[1]} zł - obecne saldo {wpis[2]} zł.")
    return

def wyplata(obecne_saldo: float) -> float: # Obsługa wypłaty pieniędzy
    kwota = pobierz_kwote()
    if obecne_saldo >= kwota: 
        wynik = obecne_saldo - kwota
        historia.append((2, kwota, wynik)) # Dodajemy wpis do historii
        stan_konta(wynik)
        return wynik # Zwraca obecne saldo po wypłacie pieniędzy (powodzenie)
    else:
        print("Masz za mało pieniędzy") # Zwraca obecne saldo po próbie wypłaty pieniędzy
        return obecne_saldo

saldo = 0
wybor = 0
historia = []
PIN = "8215"
LIMIT = 1200    
N = 3
   
sprawdzenie_pinu()
while wybor != 5:
    glowne_menu()

    wybor = wczytaj_wybor_uzytkownika()

    if wybor == 1: # Wpłata
        saldo = wplata(saldo)
    elif wybor == 2: # Wypłata
        saldo = wyplata(saldo)
    elif wybor == 3: # Sprawdzenie stanu konta
        stan_konta(saldo)
    elif wybor == 4: # Sprawdzenie historii konta
        historia_konta(historia)
    elif wybor == 5:
        print("Zamykanie aplikacji...")
    else:
        print("Nieprawidłowy wybór")
exit() # Koniec projektu


# Bardzo ładnie!
# Rozwiązanie zawiera jedynie drobny błąd nieuwagi, tzn. w linijce 33
# zrobiłeś z tej funkcji inta, a w stałej podajesz stringa, co skutkuje
# niemożnością podania poprawnego pinu. Poza tym bez uwag :>


# Zadanie 1: (3.0 / 3.0)
# Zadanie 2: (3.5 / 4.0)

# Zadania dodatkowe: 
# >>> Ograniczenie prób do N: (+0.5)
# >>> Historia operacji:      (+2.0)



# Sprawdzenie PINu alternatywnie:

def sprawdzenie_pinu_alter() -> None:
    blad = 0 # Liczba początkowych błędów
    while blad < N: # jest jak najbardziej dobrze, poniżej pokażę Ci alternatywę ;)
        pin = pobierz_pin()
        if pin != PIN:
            print(f"Zły pin, pozostało prób: {(N - 1) - blad}") # niepotrzebny nawias ;P
            blad += 1
        else:
            return # Pin poprawny
    exit()