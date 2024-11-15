from math import sqrt

n = int(input("Podaj liczbę: "))

if n < 2:
    print("Nie jest ani pierwsza, ani złożona")
    exit()
if n == 2:
    print("Liczba jest pierwsza")
    exit()
if n % 2 == 0:
    print("Liczba jest złożona")
    exit()


czy_pierwsza = True
i = 3

while i <= sqrt(n):
    if n % i == 0:
        czy_pierwsza = False
        break
    i += 2

if czy_pierwsza:
    print("Liczba jest pierwsza")
else:
    print("Liczba jest złożona")
exit()


# -----------------

for i in range(3, sqrt(n) + 1, 2):
    if n % i == 0:
        czy_pierwsza = False
        break