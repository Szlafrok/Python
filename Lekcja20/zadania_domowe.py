"""
    ZADANIE 1 (0-3) + 2 dodatkowe (max. 5)

    Proszę dokończyć klasę Przedmiot, która będzie przechowywać następujące informacje:
        oceny - lista ocen
        srednia - średnia ocen z danego przedmiotu
    
    Proszę uzupełnić jej metody:
        dodaj_ocene - dopisuje ocenę do listy i aktualizuje średnią
        wyswietl_oceny - wyświetla listę ocen
        wyswietl_srednia - wyświetla średnią

    Następnie proszę uzupełnić wywołania w skrypcie pod klasą tak, aby spełnić podane tam warunki.


"""

class Przedmiot(): # SZABLON
    srednia = 0

    def stworz_liste(self):
        self.oceny = []

    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena) # Dodajemy ocenę do listy
        pass # Proszę w tym miejscu zaktualizować średnią tak, aby była ona średnią arytmetyczną ocen z listy oceny

    def wyswietl_oceny(self):
        pass # Proszę uzupełnić metodę

    def wyswietl_srednia(self):
        pass # Proszę uzupełnić metodę

informatyka = Przedmiot()
informatyka.stworz_liste()

# Korzystając z metod proszę wpisać następujące oceny do obiektu: 5, 4, 5, 3, 6
# Następnie proszę wyświetlić listę ocen oraz ich średnią.






"""
    ZADANIE 2 (0-4) 

    Proszę wybrać dwa z trzech podanych pytań i odpowiedzieć na nie:

    a) Czym różni się metoda od funkcji? 
    b) Czym jest klasa? Po co z nich korzystamy?
    c) Czy każda metoda jest funkcją? Czy każda funkcja jest metodą? Dlaczego?

"""