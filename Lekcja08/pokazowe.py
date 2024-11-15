# BREAK

i = 0
j = 0

while True:
    print("amir")
    while True:
        print("2137 to liczba pierwsza")
        i += 1
        if i > 5:
            break

    j += 1
    if j > 20:
        break


# CONTINUE
while True:
    break
    print("papaj")
    continue
    print("ja tak zaciąłem komputer w szkole")


import math

x = math.sqrt(25) # Pierwiastek kwadratowy

from random import randint, shuffle

x = randint(1, 10) # Losowa liczba z podanych

from time import sleep

sleep(1)


# ------- ZADANIE SAMODZIELNE -------
# Proszę napisać program, który wczyta losową liczbę całkowitą z przedziału od 5 do 15 i zrobi timer:
# Timer ma wyświetlać co sekundę informację "Pozostało _ sekund."

x = 3 #randint(5, 15)

while x > 0:
    print(f"Pozostało Ci {x} sekund")
    x -= 1
    #sleep(1)
print("Koniec czasu i elo :)")

# ----------------------------------
print("FORY --------------------")


# for element in object:
#     # Coś się dzieje
#     pass

for elem in (3, 10, 2):
    print(f"Element == {elem}")

# RANGE: Wariant 1

range(10) # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
range(4) # 0, 1, 2, 3

for i in range(5):
    print(i**2) # 0, 1, 4, 9, 16

# RANGE: Wariant 2

range(4, 7) # 4, 5, 6
range(-2, 2) # -2, -1, 0, 1

for i in range(-3, 1):
    print(i + 1) # -2, -1, 0, 1

# RANGE: Wariant 3

range(1, 10, 2)
for i in range(1, 10, 2):
    print(i)


# --------- ZADANIE SAMODZIELNE 2

# Proszę wczytać od użytkownika rok urodzenia Maryli Rodowicz, a następnie wypisać dla każdego roku
# od roku urodzenia do obecnego, ile lat w danym roku miała Maryla Rodowicz.

# Dla wczytania n = 1945 powinniśmy otrzymać:

# W 1945 M.R. miała 0 lat
# W 1946 M.R. miała 1 lat
# ...
# W 2024 M.R. miała 79 lat

x = int(input("1945"))
wiek = 0

for i in range(x, 2024):
    print(f"W roku {i} Maryla Rodowicz miała {wiek}")
    wiek += 1



# PĘTLE ZAGNIEŻDŻONE

for i in range(3):
    for j in range(2):
        print(i + j) # 0, 1, 1, 2, 2, 3

##### :)

for i in range(1000, 995, -1):
    print(i)

range(5) # - prawa granica
range(1, 5) # - obie granice
range(1, 5, 2) # - obie granice i krok pomiędzy poszczególnymi