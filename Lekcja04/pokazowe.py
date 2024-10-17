x = 5

x += 5

x -= 5

x *= 5

x /= 5

x **= 2

x //= 5

print(f"Tu mamy jakiś fstring ze wstawioną zmienną x o wartości {x}")


# LOGIKA - WPROWADZENIE


# NOT
p = (50 < 25)

q = not p # Fałsz

q = not not p # Prawda

q = not not not not not not p # Prawda

p = not True
p = (1 - True)

print(q)

# OR
p = True
q = True
print(p or q)

p = True
q = False
print(p or q)

p = False
q = True
print(p or q)

p = False
q = False
print(p or q)


# AND

p = False
q = False
print(p and q)

p = True
q = False
print(p and q)

p = False
q = True
print(p and q)

p = True
q = True
print(p and q)

print("---------------------")

a = 5.0
b = 5
c = 6

p = (a == b) # Porównywanie czy są RÓWNE: pamiętamy o dwóch znakach "=" (Prawda)

p = (a > b) # Nierówność ostra: a większe niż b (Fałsz)

p = (a >= b) # Większe lub równe
p = (a <= b) # Mniejsze lub równe


p = not (a < b) # Równoważne (a >= b)

p = a > b or a == b # Równoważne (a >= b)

p = (a != c) # Różność


# PRZYKŁAD

# Korzystamy z operatorów: ==, >=, <=, >, <, !=

print(250 > 42.01) # Prawda

print(490 == 450) # Fałsz

print(24 <= 12) # Fałsz

print(40 >= 40) # Prawda

# ZADANIE Z LEKCJI 1

print(12 >= 15) # Fałsz # ==, <, !=, <=
print(5 < 15000) # Prawda # ==, >, >=, <=
print(120 != 120) # Fałsz # ==, >=, !=, <=
print(60 < 15) # Fałsz # ==, <, !=, >=
print(25.3421 >= 25.3421) # Prawda # ==, <, !=, <=


# ZADANIE Z LEKCJI 2

# Program pytający użytkownika o jego wzrost, aby na tej podstawie określić czy może
# skorzystać z rollercoastera.

wzrost = int(input("Proszę podać swój wzrost w cm: "))
werdykt = wzrost >= 160
print(werdykt)



# KOLEJNOŚĆ WYKONYWANIA DZIAŁAŃ LOGICZNYCH

d = "BIGOS"

p = a or b and c and not d

p = a or b and c and (not d) # NOT jako pierwsze
p = a or (b and c and (not d)) # AND jako drugie

# W pierwszej kolejności patrzymy na NOT, potem na AND i na końcu na OR

p = 0 < 1 <= 1 < 2 < 3 <= 4 # True


# ZADANIE Z LEKCJI 3

print(True, 25 < 140 or 10 == 10)
print(True, 100 >= 1 or 2 > 10)
print(False, 25 < 14 and 10 != 10)
print(False, -1 < 3 and 2 < 9 and 10 == 15)
print(True, 20.05 < 21 < 10 or -10 < 20 < 150 <= 150)
print(False, 1 < 10 and 2 < 15 and -50 == 42)
print(True, not 2 == 10)


# ZADANIE Z LEKCJI 4

# Proszę zmodyfikować kod z zadania 2 tak, aby oprócz wzrostu sprawdzał
# także wiek.

wzrost = int(input("Proszę podać swój wzrost w cm: "))
wiek = int(input("Proszę podać swój wzrost w cm: "))
werdykt = wzrost >= 140 and wiek >= 12
print(werdykt)

# Pytanie o XOR - Wojtek

a = True
b = False
c = False

if (sum(a, b, c) % 2 == 1):
    pass