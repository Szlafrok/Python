class Uzytkownik:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def czy_pełnoletni(self):
        return self.wiek >= 18
    
    def wyswietl_info(self):
        status = "pełnoletni" if self.czy_pełnoletni() else "niepełnoletni"
        print(f"{self.imie} {self.nazwisko}, wiek: {self.wiek} lat - {status}")

    # tworzenie użtkownika
uzytkownicy = [
    Uzytkownik("Jan", "Korek", 34),
    Uzytkownik("Anna", "Nowak", 17),
    Uzytkownik("Piotr", "Lis", 22),
    Uzytkownik("Maria", "Zając", 15)
]

# wyświetlania
for uzytkownik in uzytkownicy:
    uzytkownik.wyswietl_info()