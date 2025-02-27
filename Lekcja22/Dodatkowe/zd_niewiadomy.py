"""Dane są stała i klasy:"""

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
    
    def