import random


class linganguli(): # klasy nazywamy z dużej litery :P

    def __init__(self, czy_sigma : bool, imie, wiek, pochodzenie):
        self.czy_sigma = czy_sigma
        self.imie = imie
        self.wiek = wiek
        self.pochodzenie = pochodzenie
    
    def wypisz_danonki(self): # Fajne XD
        print(f"Czy sigma?")
        if self.czy_sigma:# == True: // Możesz stosować tę zmienną jako warunek sam w sobie (tak jak każdą inną zmienną) ;)
            print("Yes sir")
        else:
            print("Oj nie nie")
        print("________________")
        print("Twoje imię: ")
        print(self.imie)
        print("________________")
        print("Twój level w życiu:")
        print(self.wiek)
        print("________________")
        print("Pochodzenie:")
        print(self.pochodzenie)

    def czy_polska_gurom(self):
        if self.czy_sigma == True and self.pochodzenie == "Polska": # Uwaga na temat czy_sigma jak wyżej
            print("Widzę żę ty też uważasz że Polska gurom!!!")
            print("https://youtu.be/wGeFVtLo1RA?si=xkfEnHltjBfWR7qH") # To tak w kontekście XD
        else:
            print("O ty ziemniaku.")
    
    def spiew(self):
        x = random.randint(1, 2)
        if x == 1:
            print("Lingan guli guli guli wacha lingan gu linagan gu ...")
        else:
            print("Przez twe oczy zielone zielone oszalałem ...")


ziomek = linganguli(True, "Jakubu", 15, "Polska")
ziomek.wypisz_danonki()
ziomek.czy_polska_gurom()
ziomek.spiew()

# Chyba muszę zacząć częściej dawać Wam takie zadania XDDD
# Napisałeś dobre metody, skorzystałeś z prostych operatorów logicznych i instrukcji warunkowych B)

# Ładny popis, niestety pokaz pod kątem elementów Pythona na 3 punkty nie starczy, ale 2 bonusowe dam ;)