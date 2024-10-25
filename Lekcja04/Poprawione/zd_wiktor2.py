# zadanie 2
p = 132
q = 478

# a) # OK
a = (p != q)
# Zastępujemy:

a = p > q or p < q


# b)
b = (p > q)
# Zamiana:

b = not (p <= q) # Logicznie spoko, ale nie miałeś tego operatora w puli. Trzeba było użyć < oraz ==.

# c) OK
c = (p == q)
# Zamiana (przykład już gotowy w zadaniu, ale można zostawić):

c = not (p > q or p < q)


# d) OK 
d = (p >= q)
# Zamiana:

d = not (p < q)


# e) OK
e = (p == q)
# Zamiana:

e = p >= q and p <= q

# (+++)

# Należy się odznaka ;)