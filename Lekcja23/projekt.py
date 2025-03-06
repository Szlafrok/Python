from random import randint, choice

class Postac:
    def __init__(self):
        self.nazwa = ""
        self.hp = 1
        self.max_hp = 1

    def atakuj(self, przeciwnik): # przeciwnik - obiekt, który będzie otrzymywał obrażenia
        atak = randint(0, 3)

        if atak == 0:
            print(f"{przeciwnik.nazwa}")
        else:
            print(f"{self.nazwa} atakuje {przeciwnik.nazwa} i zadaje {atak} obrażeń.")
            przeciwnik.hp -= atak

        if self == przeciwnik:
            print("Mordo czemu naparzasz samego siebie?")

# Proszę napisać klasy: Gracz oraz Przeciwnik, które będą dziedziczyły po klasie Postać i wywołają w 
# swoim konstruktorze jej konstruktor. 

class Gracz(Postac):
    def __init__(self, hp = 10, max_hp = 10):
        super().__init__()
        self.hp = hp
        self.max_hp = max_hp
        self.nazwa = input("Podaj imię gracza: ")

    def przedstaw_sie(self):
        print(f"Nazywam się {self.nazwa} i mam {self.hp}/{self.max_hp}")

    def zjedz(self):
        self.hp += 2 # self.hp = self.hp + 2
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(f"Gracz {self.nazwa} wcina kebaba i ma teraz {self.hp}/{self.max_hp} HP.")


    def walka(self, przeciwnik):
        czy_walka = True
        while czy_walka:
            print(f"Życie gracza: {self.hp}")
            print(f"Życie przeciwnika: {przeciwnik.hp}")
            akcja = input("Wybierz: atak/ucieczka")
            if akcja == "atak":
                self.atakuj(przeciwnik)
                if przeciwnik.hp < 1:
                    print(f"{przeciwnik.nazwa} poszedł spać (a mimir)")
                    return True
                przeciwnik.atakuj(self)
            elif akcja == "ucieczka":
                print(f"{self.nazwa} ucieka fiatem 126p (pyrpyrpyrpyr)")
                czy_walka = False
            else:
                print("W sumie to nie wiesz co robić i pomijasz turę :V")
                przeciwnik.atakuj(self)
            
            if self.hp < 1:
                print(f"{self.nazwa} poszedł spać (a mimir)")
                return False
        return None


class Przeciwnik(Postac):
    def __init__(self, hp = 6, max_hp = 6):
        super().__init__()
        self.nazwa = choice(["Goblin", "Małpa", "Lizard", "Ork", "Amir", "Steve", "Chochlik", "Menel", "Diablik", "Sans"])
        self.max_hp = max_hp
        self.hp = hp


# ziomeczek = Gracz(15, 15)
# ziomeczek.przedstaw_sie()
# ziomeczek.atakuj(ziomeczek)
# ziomeczek.przedstaw_sie()
# ziomeczek.zjedz()

ziomeczek = Gracz()
gra = True

wygrane_walki = 0

while gra:
    przeciwnik = Przeciwnik()
    print(f"{ziomeczek.nazwa} napotkał {przeciwnik.nazwa}")
    gra = ziomeczek.walka(przeciwnik)

    if gra:
        wygrane_walki += 1

print(wygrane_walki)


