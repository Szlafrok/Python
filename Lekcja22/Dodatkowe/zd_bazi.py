PI = 3.14

class Kolo():
    def __init__(self, r):
        self.r = r
        self.obwod = 2 * PI * self.r
        self.pole = PI * self.r ** 2

    def obw_wypisz(self):
        print(self.obwod)
    
    def pole_wypisz(self):
        print(self.pole)

class Prostokat():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.obwod = 2 * a + 2 * b
        self.pole = a * b

    def obw_wypisz(self):
        print(self.obwod)
    
    def pole_wypisz(self):
        print(self.pole)

class Figura(Kolo, Prostokat):
    def __init__(self, r, a, b):
        Kolo.__init__(self, r) # rozbiłem super() na 2 osobne klasy. Teraz powinno działać ;)
        Prostokat.__init__(self, a, b)

    def obwody_wypisz(self):
        print("Obwód koła : ", 2 * PI * self.r)
        print("Obwód prostokąta : ", self.a * 2 + self.b * 2)
    
    def pola_wypisz(self):
        print("Pole koła : ", PI * self.r ** 2)
        print("Pole prostokąta : ", self.a * self.b)

figurki = Figura(2, 4, 5)
figurki.obwody_wypisz()
figurki.pola_wypisz()


# Ogólnie zrobiłeś zadanie odwrotnie - utworzyłeś figurę, która dziedziczy po Prostokącie
# i Kole (super intuicja, że można dziedziczyć z wielu klas). Korzystanie z metody super()
# na wielu klasach dziedziczonych jest jednak bardzo złożonym zagadnieniem. W obecnej formie
# korzystasz tylko z konstruktora pierwszej podanej klasy - czyli Koła. Z tego powodu
# konstruktor się wywala.

# Dlaczego jednak dopisałem self jako argument w wywołaniu konstuktorów Koła i Prostokąta?
# Wejdziemy teraz w głębszą wiedzę. To jest coś, co fajnie tłumaczy czat GPT:
# W skrócie: Python, korzystając z metody super() automatycznie zakłada, że korzystamy
# z niej jako TEN KONKRETNY OBIEKT, a więc dodanie self nie jest konieczne.
# Kiedy odwołujemy się jawnie do klasy Kolo, musimy dookreślić Pythonowi, z jakiego
# obiektu korzystamy - dlatego dodajemy self.

# Mogą zdarzyć się sytuacje, że będziesz potrzebował odnosić się do klas ręcznie ;)

# Wyszedłeś ze złych założeń, ale metody masz zrobione konsekwentnie do nich, dlatego
# za te metody i dobre spostrzeżenie daję bonus 1.5 pkt :)