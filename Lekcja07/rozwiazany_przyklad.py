import random

x = random.randint(2, 100)
i = 1

print(f"Wylosowana liczba: {x}")

while i <= x:
    if x%i == 0:
        print(f"{i} jest dzielnikiem {x}")
    i += 1

# sqrt() - pierwiastek kwadratowy

# from math import sqrt

# print(sqrt(25))