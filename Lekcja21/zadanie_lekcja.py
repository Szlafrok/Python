# Proszę zadeklarować dwie klasy - Kolo i Prostokat. Ich obiekty przy konstrukcji powinny otrzymać odpowiednio:

# - dla obiektu Kolo: promień (r)
# - dla obiektu Prostokat: boki (a) oraz (b)
# MUSIMY UŻYĆ KONSTRUKTORA

# Proszę dla każdej z tych klas podczas konstrukcji podstawić do zmiennej pole oraz obwód odpowiednio
# pole oraz obwód. Następnie proszę napisać metody wypisujące pole oraz obwód.


# Przed wykonaniem projektu należy podstawić do stałej wartość PI = 3.14

# Pole koła wyrażamy wzorem PI * r**2
# Obwód koła wyrażamy wzorem PI * 2 * r


# Proszę potem utworzyć obiekty z przykładowymi danymi, dla których wywołamy utworzone metody.

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

kolko = Kolo(10)

kolko.obw_wypisz()
kolko.pole_wypisz()


    




"""

(0-3 pkt)
ZADANIE DODATKOWE: Proszę napisać taką klasę dla trójkąta. Przyjmuje boki a, b, c. Nie wyznaczamy pola,
ale określamy, czy jest 1) równoboczny, 2) równoramienny, 3) prostokątny

"""