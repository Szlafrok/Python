class Ogl():

    def __init__(self, nazwa, opis, cena, kat):
        self.nazwa = nazwa
        self.opis = opis
        self.cena = cena
        self.kat = kat
    
    def pokaz(self):
        print(f"Nazwa {self.nazwa}")
        print(f"Opis {self.opis}")
        print(f"Cena {(self.cena): .2f} zł")
        print(f"kategoria {self.kat}")

class Chinski_0iX():
    
    def __init__(self):
        self.ogłoszenia = []
    
    def dod_ogl(self):
        while True:
            nazwa = input("\nPodaj nazwe ")
            opis = input("Opisz pordukt ") # literówka
            cena = float(input("Podaj cene "))
            kat = input("podaj kategorie ")
            
            akceptacja = input("\nCzy chcesz dodać to ogłoszenie? t/n ")

            if akceptacja == "t":
                ogloszenie = Ogl(nazwa, opis, cena, kat)
                self.ogłoszenia.append(ogloszenie)
                print("Dodano ogloszenie")
                break
            elif akceptacja == "n":
                print("Usuwanie ogłoszenia...")
                break  
            else:
                print("Podaj t lub n")
    
    def pokaz_ogl(self):
        if not self.ogłoszenia:
            print("Brak ogłoszeń")
            return
        
        ii = 1
        for ogloszenie in self.ogłoszenia:
            print(f"\n{ii}. ")
            ogloszenie.pokaz()
            ii += 1

    def opcje(self):
        while True:
            print("\n―――Menu―――")
            print("1. Dodaj ogłoszenie")
            print("2. Pokaż ogłoszenia")
            print("3. Zakończ")

            wyb = int(input("Podaj wybór ").strip())

            if wyb == 1:
                self.dod_ogl()
            
            elif wyb == 2:
                self.pokaz_ogl()
            
            elif wyb == 3:
                print("dziękujemy za korzystanie z naszego portalu")
                break
            else:
                print("Niepoprawny wybór")

LOG = "abcd"
HASLO = 12345


def logowanie(proby = 3):
    while proby > 0:
        login = input("Podaj login ")
        haslo = int(input("Podaj hasło "))
        if login == LOG and haslo == HASLO:
            olx = Chinski_0iX()
            olx.opcje()
            break # dopisałem
        else:
            proby -= 1
            print(f"Złe dane pozsoatały {proby} proby")
            if proby == 0:
                    print("error\nbrak prób")
                    break
            print("Sprobuj ponownie..\n")


logowanie()
# Między innymi:

# - bdb użycie stałych przy logowaniu
# - bdb użycie argumentów domyślnych i samo zastosowanie funkcji
# - zamiast break w 88 linijce mógłbyś użyć else w 89tej, efekt ten sam, ale wygląda bardziej elegancko XD
# - super, że w konstruktorze tworzysz pustą listę ;)
# - książkowe użycie tzw. wzkaźników (tworzysz obiekt i dodajesz odnośnik do listy, linijki 30-31)
#       - czegoś takiego nie powstydziliby się informatycy na pierwszym semestrze studiów!
# - bdb sprawdzenie, czy lista jest pusta w 41 linijce
# - bdb iteracja po kolejnych ogłoszeniach
# - bezbłędne operowanie na klasach
# - przewidywanie ew. błędów użytkownika
# - jeden, jedyny błąd: po zamknięciu programu dalej pytasz o login i nie resetujesz liczby prób - linijka 83

"""
Wszystko to, z czego skorzystałeś, pojawiło się na zajęciach, choć niektóre elementy
wykorzystywaliśmy w mniej lub bardziej pobocznej formie - chociażby lista ogłoszeń pojawiła
się w Inteligentnym Kalkulatorze jako baza liczb. Daj mi znać proszę, czy rzeźbiłeś projekt
samodzielnie, czy korzystałeś z pomocy sztucznej inteligencji, dobrze? Praca jest bardzo
złożona i niemal bezbłędna, intuicja podpowiada mi Twój duży wkład, ale jestem ciekaw, czy korzystałeś
z pomocy AI i jeśli tak, w jaki sposób pomogło Ci utworzyć ten projekt :)

Za tydzień nie będę mógł za bardzo zostać po zajęciach, ale bardzo chętnie porozmawiam o
tym projekcie za dwa tygodnie - jestem pod dużym wrażeniem, chętnie poznam Twój proces
twórczy i rozwieję ewentualne wątpliwości, jeżeli takowe się wysunęły podczas pisania projektu.
Mogę również wraz z Tobą zastanowić się nad implementacją któregoś z poniższych podpunktów.

Moje propozycje rozwinięcia pracy:
- opcja edycji i usuwania ogłoszeń
    - opcja tworzenia nowych kont (funkcja rejestracja) i wstawiania ogłoszeń z danego konta
    - możliwość otwarcia profilu użytkownika i wyświetlenia jego wszystkich ogłoszeń (i ew. daty powstania konta)
- zapisywanie ogłoszeń (i ew. rejestracji/loginów) do pliku
- skompletowanie obsługi błędów (użyj try/except) - Twój program jest częściowo odporny na
  błędy użytkownika, ale nie całkiem
- data wpisu i data modyfikacji ogłoszenia

"""