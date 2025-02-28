PI = 3.14

class Figura():

    def __init__(self):
        
        self.pole = 0
        self.obwod = 0

    def p_p(self):
        print(f"pole wynosi {self.pole}")
    
    def p_obw(self):
        print(f"obwód wynosi {self.obwod}")
        
class Kolo(Figura):
    def __init__(self, r):
        self.r = r
        #super().__init__ Niepotrzebne
        self.obwod = 2 * PI * self.r
        self.pole = PI * self.r ** 2
        

class Prostokat(Figura):
    def __init__(self, a, b):
        self.a = a
        self.b = b    
       
        #super().__init__ # Niepotrzebne
        self.obwod = 2 * a + 2 * b
        self.pole = a * b

kolko = Kolo(10)
kolko.p_p()
kolko.p_obw()

krzywy_kwadrat = Prostokat(10, 5)
krzywy_kwadrat.p_p()
krzywy_kwadrat.p_obw()

# Zadanie rozwiązane bardzo ładnie, jednak muszę zwrócić uwagę na 1 rzecz:
# niepotrzebnie wywoływałeś konstruktory. Podstawiasz wartości 0 do zmiennych
# obiektów obwod i pole, ale zaraz po wywołaniu konstruktora figury zmieniasz
# je na inne wartości. Poza tym zadanie bezbłędne ;)

# Bonus: 2.75p / 3p