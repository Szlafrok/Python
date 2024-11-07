# Stałe dane logowania
PIN = 51364
HASLO = "dragon_lore"

# Funkcja do logowania
def logowanie():
    # Zapytaj o PIN
    pin_input = input("Podaj pięciocyfrowy PIN: ")
    
    # Sprawdzamy, czy podany PIN jest zgodny z zapisanym
    if pin_input.isdigit() and int(pin_input) == PIN:
        # PIN poprawny, teraz pytamy o hasło
        haslo_input = input("Podaj hasło: ")
        
        # Sprawdzamy poprawność hasła
        if haslo_input == HASLO:
            print("Logowanie zakończone sukcesem!")
        else:
            print("Nieprawidłowe hasło.")
    else:
        print("Nieprawidłowy PIN.")

# Uruchamiamy funkcję logowania
logowanie()

# Bardzo ładna definicja funkcji :>

# 3.0 / 3.0