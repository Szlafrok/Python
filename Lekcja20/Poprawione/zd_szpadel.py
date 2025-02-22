### ZD 1

class Przedmiot():
    srednia = 0

    def stworz_liste(self):
        self.oceny = []

    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena) # Dodajemy ocenę do listy
        self.srednia = sum(self.oceny) / len(self.oceny) #obliczamy średnią

    def wyswietl_oceny(self):
        print(self.oceny)

    def wyswietl_srednia(self):
        print(self.srednia)

informatyka = Przedmiot()
informatyka.stworz_liste()

informatyka.dodaj_ocene(5)
informatyka.dodaj_ocene(4)
informatyka.dodaj_ocene(5)
informatyka.dodaj_ocene(3)
informatyka.dodaj_ocene(6)
informatyka.wyswietl_oceny()
informatyka.wyswietl_srednia()

# Elegancko zrobione :) (5 pkt)

# -------------------------------------------

### ZD 2

# a) Funkcja i metoda to w sumie ta sama rzecz, metodę definujemy w klasie, a funkcje poza nią // Prawie. Twoja wypowiedź jest prawidłowa, ale nieprecyzyjna - wartałoby dopowiedzieć, że metody mogą korzystać i modyfikować obiekty, które je wykonują (1.5 pkt)
# b) Klasa jest szblonem dzięki któremu możemy tworzyć różne obiekty. Z klas korzystamy gdy naprzykład chcemy // Do opisu klasy nie mam wątpliwości. Ucięło Ci jednak opis zastosowań, toteż (1 pkt) :P

# (2.5 / 4.0)


# Razem 7.5p, ładnie rozwiązane zadanka :D