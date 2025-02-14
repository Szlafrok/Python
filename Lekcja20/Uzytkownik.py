class Uzytkownik():
    imie = ""
    nazwisko = ""
    wiek = 0

    def wypisz_dane(self):
        print(self.imie, self.nazwisko, self.wiek)

    def pelnoletni(self):
        if self.wiek >= 18:
            print(f"Użytkownik {self.imie} {self.nazwisko} jest pełnoletni")
        else:
            print(f"Użytkownik {self.imie} {self.nazwisko} nie jest pełnoletni")

    def zmiana_wieku(self, nowy_wiek: int):
        self.wiek = nowy_wiek

    # Proszę napisać metodę, która poinformuje, czy użytkownik
    # jest pełnoletni czy nie (ma wypisać też jego dane osobowe)

    # Następnie proszę wywołać tę metodę w projekcie

    # (*) Proszę napisać metodę zmiana_wieku, która zmieni
    # wiek użytkownika

    