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
    if LIMIT <= saldo :
        print("PRZECIĄŻENIE")
        print("Przekroczyłeś limit...")
        return False
    return True    

while proba_logowania < N and not zakoncz:
    if pobierz_pin() == PIN:
        while wybor != 4: # Usuwam stąd warunek limitu - nie jest on potrzebny przy logowaniu...
            menu_glowne()
            wybor = wczytaj_wybor_uzytrkownika()   
            if wybor == 1: # ...i wstawiam go tu:
                kwota = pobierz_kwote()
                if saldo + kwota > LIMIT:
                    print("!!ERROR!!")
                    continue # Słowo kluczowe continue umożliwia nam cofnięcie się na początek pętli
                # ponieważ użyliśmy continue, else nie jest potrzebny!
                saldo += kwota
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