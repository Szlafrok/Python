"""Proszę napisać klasę Zwierze(), która:
- w konstruktorze przyjmie argumenty: imie oraz wiek.
- ma metodę dzwiek(), która wypisze do konsoli, że zwierzę o takim imieniu robi dźwięk.
- ma metodę jedz(), która wypisze do konsoli, że zwierzę o takim imieniu je.

"""

class Zwierze():

    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def dzwiek(self):
        print(f"{self.imie} wydaje dzikie odgłosy (telewizor poszedł w drzazgi)")

    def jedz(self):
        print(f"{self.imie} ma {self.wiek} lat i wcina cokolwiek zostało z mojej kanapy (om nom nom)")


class Pies(Zwierze):

    def __init__(self, imie, wiek, rasa):
        super().__init__(imie, wiek)
        self.rasa = rasa

    def jaka_rasa(self):
        print(self.rasa)


""" ZADANIE 1
Proszę napisać klasę Papuga, która będzie dziedziczyła
z klasy Zwierze i dodatkowo będzie mieć:
- zmienną kolor, która będzie trzymać kolor piór
- metodę papuguj(), która opowie jakiś żart."""

class Papuga(Zwierze):

    def __init__(self, imie, wiek, kolor):
        super().__init__(imie, wiek)
        self.kolor = kolor
    
    def papuguj(self):
        print(f"Przychodzi baba do lekarza...")

class Kakadu(Papuga):
    def __init__(self, imie, wiek, kolor):
        super().__init__(imie, wiek, kolor)

    def orzeszki(self):
        print(f"{self.imie} wcina orzeszki :)")


ptaszek = Kakadu("Panoramix", 247, "Biały")
ptaszek.orzeszki()

""" ZADANIE 2
Proszę następnie napisać klasę Kakadu, która dziedziczy
z klasy Papuga i ponadto ma metodę orzeszki(), która mówi nam,
że Kakadu je orzeszki :)
"""

# Potem robimy ZADANIE DODATKOWE



piesek = Zwierze("Szaman", 4)

print(piesek.imie)
piesek.dzwiek()
piesek.jedz()

lepszy_piesek = Pies("Kwiat", 6, "Doberman")
lepszy_piesek.jedz()
