lista = [0, 2, 4, 6, 8]

lista = []
for i in range(5000):
    lista.append(i)

#print(lista)

# [WYRAŻENIE dla ELEMENTU z OBIEKTU jeżeli spełniony WARUNEK]

# [EXPR for ELEM in ITER if COND]

from pprint import pprint


lista = [x - 5 for x in range(10) if x > 5]
print(lista)

lista = [x**2 for x in range(1, 21) if x % 2 == 0]
print(lista)


kwadraty = tuple(i**2 for i in range(10))
print(f" krotka) {kwadraty}")

kwadraty = {i**2 for i in range(10)}
print(f"  zbiór) {kwadraty}")

kwadraty = {i:i**2 for i in range(10)}
print(kwadraty)

### Zadanie 4

sequence = "HELLO@123world!456"

lista = [c for c in sequence if not(c.isalpha())]

sequence = "".join(lista)
print(sequence)