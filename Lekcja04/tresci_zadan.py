# ----------------- ZADANIE 1 --------------------
# -------------- dla wszystkich ------------------

"""
Proszę napisać program, który pobierze od użytkownika
do zmiennych a, b oraz c liczby zmiennoprzecinkowe.

Następnie niech program odpowie na pytania:

- Czy wartość zmiennej a jest największa spośród podanych?
- Czy wartość zmiennej b jest największa spośród podanych?
- Czy wartość zmiennej c jest największa spośród podanych?

"""

# ----------------- ZADANIE 2 --------------------
# ---------------- z gwiazdką! -------------------
# (to tylko wygląda na długie, ale nie jest takie złe)

"""
Proszę zastanowić się, w jaki sposób korzystając z podanych operatorów
porównawczych można zastąpić inne operatory porównawcze.

Możemy korzystać dowolnie z operatorów logicznych: and, or, not.

Przykładowo: Korzystając z operatorów:                          """

# >, <

"""
Możemy zastąpić inne operatory. Przykład:
"""

p = 123
q = 456 # jakakolwiek wartość liczbowa

a = (p == q)
b = not (p > q or p < q) # Jeżeli p nie jest większe od q ani mniejsze od q, to jest mu równe
# W ten sposób zastąpiliśmy sprawdzanie RÓWNOŚCI operatorami nierówności.


#Proszę teraz spróbować zapisać operatory:

# A)
a = (p != q) # wykorzystaj tylko operatory > oraz <

# B)
b = (p > q) # wykorzystaj tylko operatory < oraz ==

# C)
c = (p == q) # wykorzystaj tylko operator != (tu był błąd w zadaniu)

# D)
d = (p >= q) # wykorzystaj tylko operator <

# E)
e = (p == q) # wykorzystaj tylko operatory >= oraz <=

# ;)