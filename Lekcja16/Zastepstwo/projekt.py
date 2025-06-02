saldo = 50
wybor = 0

def glowne_menu():
    print("Wybierz opcje:")
    print("1. Wpłać pieniądze")
    print("2. Wypłac pieniądze")
    print("3. Sprawdź stan konta")
    print("4. Zamknij aplikację")

def pobierz_wybor_klienta():
    return int(input("Proszę wybrać operację: "))

def pobierz_kwote():
    kwota = int(input("Proszę podać kwotę: "))
    if kwota < 0:
        return -1
    return kwota

def wplac_pieniadze(saldo):
    kwota = pobierz_kwote()
    if kwota == -1:
        print("Podano nieprawidłową kwotę")
        return saldo
    else:
        print("Wpłacono pieniądze")
        return saldo + kwota

def wyplac_pieniadze(saldo):
    kwota = pobierz_kwote()
    if kwota == -1:
        print("Podano nieprawidłową kwotę")
        return saldo
    elif kwota > saldo:
        print("Masz za mało siana")
        return saldo
    else:
        print("Wypłacono pieniądze")
        return saldo - kwota

def sprawdz_saldo():
    print(f"Twój stan konta: {saldo} zł.")


while wybor != 4:
    glowne_menu()
    wybor = pobierz_wybor_klienta()

    if wybor == 1:
        saldo = wplac_pieniadze(saldo)
        sprawdz_saldo()
    elif wybor == 2:
        saldo = wyplac_pieniadze(saldo)
        sprawdz_saldo()
    elif wybor == 3:
        sprawdz_saldo()
    elif wybor == 4:
        print("Zamykanie aplikacji...")
    else:
        print("Spróbuj ponownie - błędny wybór.")