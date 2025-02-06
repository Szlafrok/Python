import random

gracz = 0
komputer = 0

def rzut() -> bool:
    rr = input("orzeł czy reszka ")
    tt = random.randint(1, 2)
    if tt == 1:
        rzucona = "orzeł"
    else:
        rzucona = "reszka"

    if rr == rzucona:
        print("Brawo zgadłeś")
        return True
    else:
        print("Brawo dla mnie")
        return False

while gracz < 10 or komputer < 10:
    res = rzut()
    if res:
        gracz += 1
    else:
        komputer += 1

if gracz == 10:
    print("Wygrałeś BRAWO!!!")

elif komputer == 10:
    print("Wygrałem")