PI = 3.14

class Figura():
    def __init__(self):
        self.obwod = 0
        self.pole = 0 # Konstuktor niepotrzebny, ale nie przeszkadza :)

    def obw_wp(self):
        print(self.obwod)
    def pol_wp(self):
        print(self.pole)
    

class Kolo(Figura):
    def __init__(self, r):
        #super().__init__() Niepotrzebne
        self.r = r
        self.obwod = 2 * PI * self.r
        self.pole = PI * self.r ** 2


class Prostokat(Figura):
    def __init__(self, a, b):
        #super().__init__() Niepotrzebne
        self.a = a
        self.b = b
        self.obwod = 2 * a + 2 * b
        self.pole = a * b


#przykład
print("kolo")
kolo = Kolo(10)
kolo.obw_wp() 
kolo.pol_wp()
print("prostokat")
prostakat = Prostokat(6, 5)
prostakat.obw_wp()
prostakat.pol_wp()

# Zadanie rozwiązane bardzo ładnie, jednak muszę zwrócić uwagę na 1 rzecz:
# niepotrzebnie wywoływałeś konstruktory. Podstawiasz wartości 0 do zmiennych
# obiektów obwod i pole, ale zaraz po wywołaniu konstruktora figury zmieniasz
# je na inne wartości. Poza tym zadanie bezbłędne ;)

# Bonus: 2.75p / 3p