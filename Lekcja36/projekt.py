inner = [1, 2]
arr = [5, 4, 2, inner]
print(arr)

slownik = {1: 5,
           "klucz":"wartosc"}

tuple()
krotka = (1, 0, 2, 1)
krotka_jednoelementowa = (5,)
print(krotka_jednoelementowa)

print(krotka.count(2))
print(len(krotka))

print(krotka.index(1))


a, b, c, d = krotka
print(a)

for keys, values in slownik.items():
    print(keys, values)


# Zbiory

zbior = {2, 5, 6, 7, 8, 1, 4, 4}
print(zbior)

zbior = set(krotka)
print(zbior)


zbior.add(9)
zbior.add("eeee")

print(zbior)

#zbior.remove(10)
print(zbior)

zbior.discard(10)
print(zbior)

val = zbior.pop()
print(val)

zbior.clear()
print(zbior)

# Krotka, lista, zbiór, słownik


zbior = {1,2,3}
krotka = (4,5,6)
lista = [7,8,8,9]

# zbiór -> lista
print(list(zbior))
print(type(list(zbior)))

# krotka -> lista
print(list(krotka))
print(type(list(krotka)))

# zbiór -> krotka
print(tuple(zbior))
print(type(tuple(zbior)))

# lista -> krotka
print(tuple(lista))
print(type(tuple(lista)))

# krotka -> zbiór
print(set(krotka))
print(type(set(krotka)))

# lista -> zbiór
print(set(lista))
print(type(set(lista)))


A = {1, 2, 3}
B = {3, 3, 4, 5}

print(A | B)
print(A & B)
print(B - A)