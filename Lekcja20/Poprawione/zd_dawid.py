class Przedmiot:
    def __init__(self):
        self.oceny = []
        self.srednia = 0.0

    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)
        self.srednia = sum(self.oceny) / len(self.oceny)

    def wyswietl_oceny(self):
        print("Oceny:" , self.oceny)
    
    def wyswietl_srednia(self):
        print("Średnia ocen:", round(self.srednia, 2))

informatyka = Przedmiot()
informatyka.dodaj_ocene(5)
informatyka.dodaj_ocene(4)
informatyka.dodaj_ocene(5)
informatyka.dodaj_ocene(3)
informatyka.dodaj_ocene(6)

informatyka.wyswietl_oceny()
informatyka.wyswietl_srednia()

# Zadanie rozwiązane bardzo ładnie (5/5)


# Odpowiedzi na pytania:
# a) Metoda to funkcja, która jest zdefiniowana w klasie i działa na jej obiektach, 
#    natomiast funkcja jest niezależnym blokiem kodu, który można wywołać w dowolnym miejscu.
# b) Klasa to szablon do tworzenia obiektów, które mogą przechowywać dane i metody. 
#    Używamy ich, aby uporządkować kod i umożliwić ponowne wykorzystanie.

# (4/4) Elegancko B)