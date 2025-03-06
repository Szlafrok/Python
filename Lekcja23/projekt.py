from random import randint

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

# Proszę napisać klasy: Gracz oraz Przeciwnik, które będą dziedziczyły po klasie Postać i wywołają w 
# swoim konstruktorze jej konstruktor.