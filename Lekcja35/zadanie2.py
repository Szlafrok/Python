lista1 = [1, 2, 3]
lista2 = [6, 7, 8]

#lista1 += lista2
lista1.extend(lista2)

lista1.pop(5)
lista2.pop(2)


lista1.remove(max(lista1))
lista1.remove(min(lista1))

print(lista1)

lista1.append(1)

lista1.sort()
print(lista1)

kopia = lista1.copy()

kopia.reverse() # kopia = kopia[::-1]

for i in range(len(lista1)):
    lista1[i] += 1
for i in range(len(kopia)):
    kopia[i] -= 1

print(lista1)
print(kopia)