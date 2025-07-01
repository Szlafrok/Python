lista = [4, 6, 2.5, 1, 2, "zabawny", "tekst", True, False, (0, 0)]
try:
    sorted(lista) # OK
except:
    pass

def list_purge(arr: list):
    sortable = []
    for x in arr:
        if isinstance(x, (int, float, bool)): # Jest to poniekąd odpowiedź na pytanie z zadania 1a, także spoko
            sortable.append(x)
    return sortable
# Ciekawostka: np. krotki można sortować między sobą, podobnie jak listy
# (5 / 5) Ładnie :)

lista1 = [4, 7, 2]
lista2 = [9, 3, 6] # +

polaczona = lista1 + lista2 # +

del polaczona[5] # +
del polaczona[2] # ok kolejność
print(polaczona)

polaczona.remove(min(polaczona))
polaczona.remove(max(polaczona)) # +

polaczona.append(10) # +

polaczona.sort() # +

kopia = polaczona[:] # +

kopia.reverse() # +

polaczona = [x + 1 for x in polaczona] # +
kopia = [x - 1 for x in kopia] # +

print("Oryginalna:", polaczona) # +
print("Kopia:", kopia) # +

# (3 / 3) Ekstra!