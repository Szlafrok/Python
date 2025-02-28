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
            opis = input("Opisz pordukt ")
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
        else:
            proby -= 1
            print(f"Złe dane pozsoatały {proby} proby")
            if proby == 0:
                    print("error\nbrak prób")
                    break
            print("Sprobuj ponownie..\n")


logowanie()
