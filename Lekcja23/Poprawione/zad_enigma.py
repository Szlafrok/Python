from random import randint, choice

class Postac():
    def __init__(self):
        self.nazwa = ""
        self.hp = 1
        self.maxhp = 1

    def atakuj(self, przeciwnik):
        atak = randint(0, 3)

        if atak == 0:
            print(f"{przeciwnik.nazwa} ")
        else:
            print(f"{self.nazwa} atakuje {przeciwnik.nazwa} i zadaje {atak} obrażeń")
            przeciwnik.hp -= atak
        
        if self == przeciwnik:
            print("Mordo bedzie dobrze")

class Gracz(Postac):
    def __init__(self, hp = 10, maxhp = 10):
        super().__init__()
        self.hp  = hp
        self.maxhp = maxhp
        self.nazwa = input("Podaj nazwe gracza: ")

    def przedstaw_sie(self):
        print(f"Nazywam sie {self.nazwa} i mam {self.hp}/{self.maxhp}")

    def zjedz(self):
        self.hp += 2
        if self.hp >= self.maxhp:
            self.hp = self.maxhp
        print(f"Gracz {self.nazwa} je kebaba i ma teraz {self.hp} HP")

    def walka(self, przeciwnik): # było zjedz jako argument
        czy_walka = True
        while czy_walka:
            print(f"Mordo masz {self.hp}")
            print(f"Nie morda ma {przeciwnik.hp}")
            akcja = input("wybierz: atak/ucieczka/zjedz ")
            if akcja == "atak":
                self.atakuj(przeciwnik)
                if przeciwnik.hp < 1:
                    print(f"{przeciwnik.nazwa} poszedł lulu")
                    return True
                przeciwnik.atakuj(self)

            elif akcja == "ucieczka": # Była literówka
                print(f"{self.nazwa} ucieka swoim parowozem")
                czy_walka = False

            elif akcja == "zjedz":
                self.zjedz() # było: zjedz()

            else:
                print("Nie wiesz co robisz w zyciu wiec idziesz sie napoic i omija cie tura")
                przeciwnik.atakuj(self)
            
            if self.hp < 1:
                print(f"{self.nazwa} poszedł spać")
                return False



class Przeciwnik(Postac):
    def __init__(self, hp = 6, max_hp = 6):
        super().__init__()
        self.nazwa = choice(["Goblin", "Małpa", "Lizard", "Ork", "Amir", "Steve", "Chochlik", "Menel", "Diablik", "Sans"])
        self.max_hp = max_hp
        self.hp = hp




ziomo = Gracz()
gra = True
wygrane_walki = 0


while gra:
    przeciwnik = Przeciwnik()
    print(f"{ziomo.nazwa} napotkał {przeciwnik.nazwa}")
    gra = ziomo.walka(przeciwnik)

    if gra:
        wygrane_walki += 1

# Będzie bez bonusu za logikę gry, bo możemy leczyć się w nieskończoność i przeciwnik nie atakuje
# nas po naszym uzdrowieniu.

# Co do moich poprawek: poprawiłem kod, porównaj sobie ze swoim:

# Przyjmowałeś zjedz jako argument w metodzie walka, przez co było to traktowane jako zmienna, nie metoda.
# Poprawnym wywołaniem metody jest obiekt.metoda(), więc w linijce 55 zapisałem to jako self.zjedz().
# Zgaduję, że dodałeś zjedz jako argument, ponieważ podkreślało Ci zjedz() jako nieistniejący element.
# Jest to jednak metoda, dlatego musiało być odniesienie do obiektu ;)

# Poza tym poprawiłem literówkę w warunku ucieczki - zwykle nie biorę tego pod uwagę, jednak tutaj
# to dość ważny błąd - mówisz graczowi, że musi wpisać "ucieczka", on wpisuje "ucieczka" (zamiast "uciczka", jak
# to było dotąd w kodzie) i ukarałbyś go utratą tury.

# Poza tym w porządku, ale jednak błędy są dość poważne, toteż dam 1.5p / 3p.
# Pamiętaj o poprawnym wywoływaniu metod i będzie dobrze :)