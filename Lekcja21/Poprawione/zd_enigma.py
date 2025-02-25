class Student:
    
    def __init__(self, nazwisko: str, ocena_matematyka: float, ocena_informatyka: float, ocena_wf: float) -> None: #przyjmuje obiekty klasy Student

        self.nazwisko: str = nazwisko #Przechowuje nazwisko
        self.ocena_matematyka: float = ocena_matematyka #Przechowuje ocene z matematyki
        self.ocena_informatyka: float = ocena_informatyka #Przechowuje ocene z informatyki
        self.ocena_wf: float = ocena_wf #Przechowuje ocene z wf
        
    def srednia(self) -> None: #oblicza Srednia
        print(f"Średnia wynosi {((self.ocena_informatyka + self.ocena_matematyka + self.ocena_wf) / 3): .2f}") #.2f - powoduje że liczba posiada dwie cyfry po przecinku
    
    def zdane(self) -> None: #stwierdza czy student zdał czy nie
        if  self.ocena_informatyka >= 3.0 and self.ocena_matematyka >= 3.0 and self.ocena_wf >= 3.0:
            print("Zdane")
        else:
            print("Nie zdano")

    def wypisz_oceny(self) -> None: # wypisyje wszytkie oceny
        print("Oceny:")
        print(f"Matematyka {self.ocena_matematyka} informatyka {self.ocena_informatyka} wf {self.ocena_wf}")
        

    def wypisz(self) -> None: # wypisuje ogolne dane
        print(f"Student {self.nazwisko}")
        self.wypisz_oceny()
        self.srednia()
        self.zdane()

żak = Student("Sobieski", 4.99, 3.74, 6) #tworzymy pierwszy "profil" studenta
żak.wypisz() #Korzystamy z funkcji wypisz()   // chciałbym takie oceny... 

żak_2 = Student("Biały", 4.1, 2.55, 3.51) #ponownie tworzymy "profil" stydenta lecz z innymi danymi
żak_2.wypisz() #korzystamy z funkcji wypisz() lecz z dannymi żak2


# Zadanie rozwiązane bezbłędnie. Dobre komentarze i wyczerpujący type hinting :)

# (5/5) (+2p za dodatkowe) -> 7 pkt :D