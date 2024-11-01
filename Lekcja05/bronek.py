tekst = input("Wprowadź oczekiwany tekst: ")

if "marchewka" in tekst and "abc" in tekst and "tygrysek" in tekst:
    print("Tekst zawiera wszystkie wymagane wyrażenia.")
else:
    print("Tekst nie zawiera wszystkich wymaganych wyrażeń.")


login=input("Podaj login do zalogowania sie do konta: ")
LOGIN="misclick" # !!!!!! Nie wolno tak zrobić! Jeżeli podstawiasz login do tej samej zmiennej, kasujesz poprzednią wartość! Musisz stworzyć inną zmienną, najlepiej stałą - zapisaną wielkimi literami
if "misclick"== login: # Są takie formaty logowania (np. do google), które pytają o hasło dopiero po podaniu loginu - może tak być.
   # Chodziło mi jednak o zrobienie tego za pomocą ANDa
    haslo=input() # Brakowało nawiasów. Input jest funkcją!
    HASLO="kaczkawizardWOLOLO" # !!!!!! ten sam błąd, co przy loginie
    print("podaj jeszcze hasło: ") #!!!!!! PRINT jest funkcją, nie możesz podstawić do niego wartości za pomocą = 
    if "kaczkiwizardWOLOLO" == haslo: # Jeżeli chcesz zrobić sprawdzanie hasła po podaniu loginu, musisz zrobić wcięcie - cały czas poruszasz się w sytuacji, gdzie podałeś już prawidłowy login, nie możesz jeszcze wyjść z tego IFa!
        print("Gratulacje zalogowanie pomyślnie")
    else: 
        print("Hasło nie prawidłowe")
else:
    print("Nieprawidłowy login") # Nie rozpatrywałeś przypadku, w którym login jest nieprawidłowy