# ------------- Zadanie 1 --------------


a = float(input("Podaj zmienną a: "))
b = float(input("Podaj zmienną b: "))
c = float(input("Podaj zmienną c: "))

# Sposób 1
if a >= b and a >= c:
    print("Wartość zmiennej a jest największa")

if b >= a and b >= c:
    print("Wartość zmiennej b jest największa")

if c >= b and c >= a:
    print("Wartość zmiennej c jest największa")

# Sposób 2
if a == max(a, b, c):
    print("Wartość zmiennej a jest największa")

if b == max(a, b, c):
    print("Wartość zmiennej b jest największa")

if c == max(a, b, c):
    print("Wartość zmiennej c jest największa")

# Maksymalnie plusów: (+++)


# ------------- Zadanie 2 --------------
p, q = True, True # Ciekawostka - możemy deklarować kilka zmiennych naraz ;)

# A)
a = (p != q) # wykorzystaj tylko operatory > oraz <
a = (p > q or p < q)

# B)
b = (p > q) # wykorzystaj tylko operatory < oraz ==
b = not (p < q or p == q)

# C)
c = (p == q) # wykorzystaj tylko operator !=
c = not (p != q)

# D)
d = (p >= q) # wykorzystaj tylko operator <
d = not (p < q)

# E)
e = (p == q) # wykorzystaj tylko operatory >= oraz <=
e = (p >= q and p <= q)

# Maksymalnie plusów: (++++)