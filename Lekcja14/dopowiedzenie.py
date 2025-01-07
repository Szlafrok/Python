# ITEROWANIE PO STRINGACH

arr = [1, 2, 3, 4, 5]

for elem in arr:
    pass#print(elem)


arr = "23456"

for char in arr:
    print(char)

tekst = "Ala ma kota a kot ma dosyć Ali spółka ZOO"
for char in tekst:
    print(char, end = ".")


# TYPE HINTING, czyli sugerowanie typu funkcji

def funkcja(x: float, y: int = 5) -> int:
    return x**y

funkcja(5)

def simple(x, y = 5): # Funkcja równoważna funkcji funkcja(), ale bez type hintingu.
    return x**y


print("Ale ten tekst jest jednolity", end = ".")