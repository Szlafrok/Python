#owoc mojej (krótkiej) pracy na lekcji, coś nie działa.


PI = 3.14

class Figura():
    def __init__(self, a,obw,pol):
        self.a = a
        self.obw = obw
        self.pol = pol


class Kolo(Figura):
    def __init__(self, a, obw = 0, pol = 0):
        super().__init__(a, obw, pol)
        self.obw = 2 * PI * self.a
        self.pol = PI * self.a ** 2
        
    def obw_wypisz(self):
        print(self.obw)
    
    def pole_wypisz(self):
        print(self.pol)

class Prostokat(Figura):
    def __init__(self, a, b, pol = 0, obw = 0):
        super().__init__(a, obw, pol) # Pomyliłeś kolejność - było: (obw, pol, a)
        self.b = b
        
    def obw_wypisz(self):
        self.obw = 2 * self.a + 2 * self.b
        print(self.obw)
    
    def pole_wypisz(self):
        self.pol = self.a * self.b
        print(self.pol)

obj = Prostokat(4, 5)
obj.obw_wypisz()
obj.pole_wypisz()

obj_2 = Kolo(10)
obj_2.obw_wypisz()
obj_2.pole_wypisz()

# Trochę przekombinowałeś :P

# Kluczem w dobrym rozwiązaniu zadania było zauważenie, co wspólnego
# mają figury i to zauważyłeś - pole i obwód. Zgubiłeś jednak fakt, że
# pole i obwód figury wyznaczamy na bazie ich promienia lub boków. Dlatego
# nie podajemy ich w argumentach :P

# Po naniesieniu poprawki w 27 linijce Twoje klasy działają, ale nie rozwiązałeś
# trudności, którą postawiło przed Tobą to zadanie. Trzeba było zauważyć wspólny
# element obu klas - pole i obwód - co zauważyłeś, ale umknął Ci sposób ich wyznaczenia
# - czyli metody. To one powinny znaleźć się w klasie Figura. Zbieranie w kole
# parametru a zamiast r teoretycznie umożliwiłoby przemieszczenie go do Figury,
# ale znacznie skomplikowałoby zadanie i czytelność rozwiązania - jednak celnym
# spostrzeżeniem jest fakt, iż jest to możliwe.

# Rozwiązanie zadania zawieram w pliku rozwiazanie.py w folderze Lekcja22/Dodatkowe ;)

# Bonus: za dobrą intuicję i częściowe rozwiązanie +1.75 pkt (z 3.00 możliwych)