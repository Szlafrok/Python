class Student:
    """
    Klasa reprezentująca studenta, przechowująca jego oceny oraz sprawdzająca zaliczenie.
    """
    
    def __init__(self, nazwisko: str, ocena_matematyka: float, ocena_informatyka: float, ocena_wf: float) -> None:
        """
        Konstruktor inicjalizujący obiekt studenta.
        :param nazwisko: Nazwisko studenta
        :param ocena_matematyka: Ocena z matematyki
        :param ocena_informatyka: Ocena z informatyki
        :param ocena_wf: Ocena z wychowania fizycznego
        """
        self.nazwisko = nazwisko
        self.oceny = {
            "matematyka": ocena_matematyka,
            "informatyka": ocena_informatyka,
            "wf": ocena_wf
        }
        self.srednia: float = sum(self.oceny.values()) / len(self.oceny)  # Obliczenie średniej ocen
        self.wszytko_zal: bool = all(ocena >= 3.0 for ocena in self.oceny.values())  # Sprawdzenie zaliczenia
    
    def wypisz_oceny(self) -> None:
        """
        Metoda wypisująca oceny studenta.
        """
        print(f"Oceny studenta {self.nazwisko}:")
        for przedmiot, ocena in self.oceny.items():
            print(f"- {przedmiot}: {ocena}")
    
    def zdane(self) -> str:
        """
        Metoda sprawdzająca, czy student zaliczył wszystkie przedmioty.
        :return: Informacja o zaliczeniu w formie tekstowej
        """
        return "Student zaliczył wszystkie przedmioty." if self.wszytko_zal else "Student nie zaliczył wszystkich przedmiotów."
    
# Test klasy
if __name__ == "__main__":
    student1 = Student("Kowalski", 4.0, 3.5, 2.5)
    student1.wypisz_oceny()
    print(student1.zdane())
    
    student2 = Student("Nowak", 5.0, 4.5, 3.0)
    student2.wypisz_oceny()
    print(student2.zdane())


# X

L = [True for i in range(10)]
L[1] = False
print(L)
print(all(L))