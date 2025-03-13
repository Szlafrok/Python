from random import randint, choice

class Postać:
    def __init__(self):
        self.nazwa = ""
        self.hp = 1
        self.max_hp = 1
    
    def atakuj(self, przeciwnik):
        atak = randint(0, 3)

        if atak == 0:
            print(f"{przeciwnik.nazwa}")
        else:
            print(f"{self.nazwa} atakuje {przeciwnik.nazwa} i zadaje {atak} obrażeń.")
            przeciwnik.hp -= atak
        
        if self == przeciwnik:
            print("Mordo czemu bijesz samego siebie?")

class Gracz(Postać):
    def __init__(self, nazwa = "", hp = 10, max_hp = 10 ):
        super().__init__()
        self.nazwa = input("Podaj nazwę gracza: ")
        self.hp = hp
        self.max_hp = max_hp
    
    def przedstaw_sie(self):
        print(f"Nazywam się {self.nazwa} i mam {self.hp}/{self.max_hp} punktów zdrowia.")
    
    def am_am(self):
        self.hp += 2
        if self.hp > self.max_hp:
            self.hp == self.max_hp
        print(f"Gracz {self.nazwa} wcina kebabika i ma teraz {self.hp}/{self.max_hp} punktów zdrowia.")
    
    def walka(self, przeciwnik):
        self.ile_leczenia = 0
        czy_walka = True
        while czy_walka:
            print(f"Życie gracza: {self.hp}")
            print(f"Życie przeciwnika: {przeciwnik.hp}")
            akcja = input("wybierz: atak/ucieczka/leczenie")
            if akcja == "atak":
                print(choice(["kamenameha", "kaboom", "pif", "pciu"]))
                self.atakuj(przeciwnik)
                if przeciwnik.hp < 1:
                    print(f"{przeciwnik.nazwa} poszedł lulu (those who know).")
                    return True
                przeciwnik.atakuj(self)
            elif akcja == "ucieczka":
                print(f"{self.nazwa} ucieka fiatem 126p")
                czy_walka = False
            elif akcja == "leczenie":
                if self.ile_leczenia < 5:
                    print(f"{self.nazwa} jest głodny.")
                    self.am_am()
                    self.ile_leczenia += 1 # Fajne ograniczenie! Dodałem tylko self., aby ta zmienna była przypisana do obiektu.
                else:
                    print("Brak jedzonka.")
            else:
                print("Jesteś tam jescze?")
                przeciwnik.atakuj(self)
            
            if self.hp < 1:
                print(f"{self.nazwa} poszedł spać (a mimir)")
                return False



class Przeciwnik(Postać):
    def __init__(self, hp = 6, max_hp = 6):
        super().__init__()
        self.nazwa = choice(["B4b4_0d_P014k4", "Goblin", "Małpa", "Lizard", "Ork", "Amir", "Steve", "Chochlik", "Menel", "Diablik", "Sans"])
        self.max_hp = max_hp
        self.hp = hp

ziomeczek = Gracz()
gra = True
wygrane_walki =0

while gra:
    przeciwnik = Przeciwnik()
    print(f"{ziomeczek.nazwa} napotkał {przeciwnik.nazwa}.")
    gra = ziomeczek.walka(przeciwnik)

    if gra:
        wygrane_walki += 1

print(f"wygrałeś {wygrane_walki} walk.")


# 3/3 +0.5 za ograniczenie :)

# Zmieniłem zmienną lokalną ile_leczenia na zmienną obiektu self.ile_leczenia.
# W ten sposób ilość zużytych uzdrowień przenosi się pomiędzy walkami. Przydałoby
# się tylko ustawienie tej wartości na 0 w konstruktorze, nie na początku walki, aby
# mogło to tak w pełni zadziałać.

# W razie pytań możesz śmiało odpisać na maila lub zostać po zajęciach :)