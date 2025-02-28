PI = 3.14

class Figura():

  # Możemy utworzyć konstruktor, ale NIE MUSIMY:
  # def __init__(self):
  #     self.obwod = 0
  #     self.pole = 0

  # OBWOD i POLE zostaną podstawione w DZIEDZICZĄCYCH KLASACH, więc nie będzie błędu!
  # Każda klasa podstawi je sobie osobno, więc nie musimy się o nie martwić.


    def obw_wypisz(self):
        print(self.obwod)

    def pole_wypisz(self):
        print(self.pole)


class Kolo(Figura):
    def __init__(self, r):
        self.r = r
        self.obwod = 2 * PI * self.r
        self.pole = PI * self.r ** 2

class Prostokat(Figura):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.obwod = 2 * a + 2 * b
        self.pole = a * b


obj = Prostokat(4, 5) # Tworzymy obiekt i w tym momencie on ma zapisany swoje: a, b, obwód i pole.
obj.obw_wypisz() # Możemy swobodnie wywołać na nim te metody.
obj.pole_wypisz()

obj_2 = Kolo(10)
obj_2.obw_wypisz()
obj_2.pole_wypisz()