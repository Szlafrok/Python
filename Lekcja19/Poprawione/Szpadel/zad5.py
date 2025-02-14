import random

def gra() -> None:
    punkty_g = 0
    punkty_k = 0
    opcje = ["orzeł", "reszka"]
    while True:
        wybor = input("Jak myślisz co wypadnie (orzeł/reszka): ").lower()
        losowanie = random.choice(opcje)
        print(f"Wypadł/a {losowanie}")
        if losowanie == wybor:
            print("Gracz otrzymuje 1 punkt")
            punkty_g += 1
        else:
            print("Komputer otrzymuje 1 punkt")
            punkty_k +=1
        
        if punkty_g >= 10 and punkty_g - punkty_k >= 2: # Tu była równość przy punkty_g!
            print("Gracz wygrał")
            break
        elif punkty_k >= 10 and punkty_k - punkty_g >= 2: # Tu była równość przy punkty_k!
            print("Komputer wygrał")
            break

gra()

# Rozważmy następujący scenariusz:

# Wynik         Kto zdobywa punkt
# 9-9           Gracz
# 10-9          Komputer
# 10-10         Gracz
# 11-10         Komputer
# 11-11         Gracz
# 12-11         Gracz
# 13-11         KONIEC GRY

# Kiedy doprowadzasz do gry na przewagi, musisz rozpatrywać nie przypadek, kiedy Twoje punkty
# będą dokładnie na progu, ale kiedy ten próg osiągniesz lub przekroczysz. Dlatego nie punkty == 10, tylko punkty >= 10 :)


# 5/5 za zadanie podstawowe + 0.5 za zadanie dodatkowe -> 5.5 punktu. Ładnie zrobione :)