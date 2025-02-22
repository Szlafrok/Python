class Trojkat():
    a = 0
    b = 0
    c = 0
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b    
        self.c = c

    def row_boczny(self):
        if self.a == self.b == self.c:
            return True
        
    def row_ramienny(self):
        if self.a == self.b or self.b == self.c or self.a == self.c:
            return True
        
    def prostokatny(self):
        if self.a**2 + self.b**2 == self.c**2 or self.a**2 + self.c**2 == self.b**2 or self.b**2 + self.c**2 == self.a**2:
            return True
    
    def sprawdzenie(self):
        if self.row_boczny():
            print("Trojkat jest rownoboczny.")

        elif self.row_ramienny():
            print("Trojkat jest rownoramienny.")

        elif self.prostokatny():
            print("Trojkat jest prostokatny.")
        else:
            print("Trojkt jest roznoboczny")

trojkacik = Trojkat(10, 8, 6)

trojkacik.sprawdzenie()


# Bardzo sprytne podejście do problemu, ale trochę niekonwencjonalne - raczej zachęcałbym
# do zwracania także wartości False w metodach badających typ trójkąta, nie tylko True.

# Nie zmienia to faktu, że to znakomite spostrzeżenie :)
# Poza tym zadanie super

# 3p / 3p