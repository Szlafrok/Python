from random import randint

szukana = randint(1, 100000)

odp = 0
proby = 0

while szukana != odp:
    odp = int(input("Podaj liczbę: "))
    proby += 1
    if odp > szukana:
        print("Podana liczba jest zbyt duża!")
    elif odp < szukana:
        print("Podana liczba jest zbyt mała!")

print(f"Gratulacje! Znalazłeś szukaną liczbę w {proby} próbach!")