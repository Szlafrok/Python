import math

from random import randint, shuffle # Po co shuffle? Nie korzystasz z niego :P

x = randint(1, 100000)
y = int(input("Podaj liczbę między 1 a 100000:"))
i = 0

while not y == x:
    if y > x:
        print("Liczba jest mniejsza.")
        i += 1
        y = int(input("Podaj liczbę między 1 a 100000:"))
    elif y < x:
        print("Liczba jest większa.")
        i += 1
        y = int(input("Podaj liczbę między 1 a 100000:"))
i += 1
print(f"Gratulację zgadłeś liczba była równa {x} , wykonałeś {i} prób.")
print("__________________________________")

# Bardzo ładnie !!!!

# 4 / 4