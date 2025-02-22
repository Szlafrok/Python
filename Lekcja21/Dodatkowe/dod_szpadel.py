# ---------------------------Dodatkowe---------------------------
class Trojkat():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def rodzaj(self):
        self.boki = [self.a, self.b, self.c]
        self.boki = sorted(self.boki)

        if self.a == self.b == self.c:
            print("Równoboczny")
        elif self.a == self.b or self.b == self.c or self. a == self.c:
            print("Równoramienny")
        elif self.boki[1]**2 + self.boki[0]**2 == self.boki[2]**2:
            print("Prostokątny")
        else:
            print("Ani równoboczny, równoramienny lub prostokątny")

    def obwod(self):
        print(self.a * 2 + self.b * 2) # To nie jest wzór na obwód trójkąta! Zgaduję, że to błąd nieuwagi :P

trojkat_kwadratowy = Trojkat(3, 4, 5)
trojkat_kwadratowy.rodzaj()
trojkat_kwadratowy.obwod()

# Nie będę ciął nikomu punktów za obwód, bo nie wymieniłem go bezpośrednio w tresci
# zadania i to by było trochę czepialskie z mojej strony :P

# Poza tym zadanie zrobione bardzo ładnie B)

# 3p / 3p