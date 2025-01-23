LIMIT = 1200
PIN = "8501"
N = 4
saldo = 0.0
wybor = 0
proba_logowania = 0
zakoncz = False

def pobierz_pin() -> str:
    kod_pin = input("Wprowadź PIN do karty: ")
    return kod_pin 



def menu_glowne() -> None:
    print("Prosze wprowadzic liczbe odpowiednia dla operacji")
    print("1. wplata ")
    print("2. wyplata ")
    print("3. sprawdz stan konta ")
    print("4. zakoncz ")
    print("UWAGA na koncie nie możesz mieć więcej niz 1200 zł.")

def wczytaj_wybor_uzytrkownika() -> int:
    return(int(input("Wskaż wybór:")))

def pobierz_kwote() -> float:
    return float(input("Podaj kwote: "))

def sprawdzanie_limitu() -> bool:
    if LIMIT <= saldo : # Powinno być "<", nie "<="!
        print("PRZECIĄŻENIE")
        print("Przekroczyłeś limit...")
        return False
    return True    

while proba_logowania < N and not zakoncz:
    if pobierz_pin() == PIN:
        while wybor != 4 and sprawdzanie_limitu() == True:
            menu_glowne()
            wybor = wczytaj_wybor_uzytrkownika()   
            if wybor == 1:
                saldo += pobierz_kwote()
            elif wybor == 2:
                kwota = pobierz_kwote()
                if saldo < kwota:
                    print("!!ERROR!!")
                else:
                    saldo -= kwota
            elif wybor == 3:
                print(f"Twój stan konta wynosi {saldo}")

            elif wybor == 4:
                zakoncz = True
            

            else:
                print("Nieprawidlowy wybór")
    
   
    proba_logowania += 1

   
print("Zamykanie aplikacji......")


# Zadanie 1: (3/3) bo zaliczone z lekcji

# Implementacja limitu wygląda ładnie :)
# Jest jednak pewien problem, ale poruszę go w następnym zadaniu.


# Zadanie 2: (3/4)

# Implementacja zamka szyfrowego jest bardzo elegancka. Nie rozumiem tylko, dlaczego
# każesz się ponownie logować w sytuacji, gdy górny limit zostanie przekroczony? Wówczas
# powinien wyskoczyć błąd i cofnąć nas do wyboru opcji, tak się jednak nie dzieje.
# Do tego dochodzi moja uwaga z linijki 30.
# Bardzo ładne wykorzystanie flagi zakoncz!!!


# Zadanie dodatkowe - Liczba prób logowania N: (+0.5 / 0.5)

# Gratuluję znakomitych rozwinięć w projekcie!

