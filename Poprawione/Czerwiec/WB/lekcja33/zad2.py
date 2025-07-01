def find_max(tablica, start, koniec):
    indeks = start
    for i in range(start, koniec + 1):
        if tablica[i] > tablica[indeks]:
            indeks = i
    return indeks

def selection_sort(tablica):
    n = len(tablica)
    for koniec in range(n - 1, 0, -1):
        indeks_max = find_max(tablica, 0, koniec)
        tablica[koniec], tablica[indeks_max] = tablica[indeks_max], tablica[koniec]
    return tablica
lista = [5, 1, 4, 2, 3]
print("lista przed sortowaniem:", lista)
posortowana = selection_sort(lista)
print("Posortowana lista:", posortowana)

# Elegancko B)

# (4 / 4)