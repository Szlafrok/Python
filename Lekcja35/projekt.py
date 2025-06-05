import random

lista = []

for i in range(10):
    val = random.randint(1, 50000)
    lista.append(val)

print(lista)

for i in range(10):
    if i%2 == 0:
        print(lista[i])
    


# Tworzenie listy
papaja = [1, 5, 2137, "maluch", None, "kremówka"]
print(papaja)

# append
papaja.append("kebab")
print(papaja)

# extend
odjazd = ["mcqueen", "cinquecento", "da_ktos_blika", "na_kebaba"]
odjazd.extend(papaja)
print(odjazd)

# insert
print(papaja)
papaja.insert(1, "kaczucha")
print(papaja)

# pop
papaja.pop(4)
print(papaja)

# remove
papaja.extend(["kebab", "kebab"])
papaja.remove("kebab")
print(papaja)

# index
print(papaja.index(None))

#papaja.pop(papaja.index("kremówka"))

# count
print(papaja.count("kebab"))


# sort
#papaja.sort()


# [Ćwiczenie!]

# reverse
papaja.reverse()
print(papaja)

print(papaja[::-1])

# copy
marakuja = papaja.copy()
print(marakuja)
marakuja[0] = "ananasy z ósmej klasy"
print(marakuja)
print(papaja)

# clear
marakuja.clear()
print(marakuja)