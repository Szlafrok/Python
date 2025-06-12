# 1. Stwórz krotkę, listę, słownik i zbiór zawierający po 3 elementy
# 2. Za pomocą funkcji len() sprawdź długości poszczególnych obiektów
# 3. Za pomocą pętli for wypisz wszystkie elementy każdego z obiektów
# 4. Teraz wypisz wartości słownika zamiast kluczy
# 5. Wypisz te same elementy w odwrotnej kolejności, czy zawsze jest to możliwe
# bezpośrednio? W razie problemów skorzystaj z pomocy chataGPT
# 6. Dodaj do listy elementy z krotki, zbioru i wartości słownika.
# 7. Dodaj do listy 2 liczby - wartość maksymalna i minimalna listy.
# 8. Sprawdź długość listy.
# 9. Zamień listę na krotkę- krotka2 i sprawdź jej długość.
# 10. Zamień krotkę na zbiór - zbior2 i sprawdź jego długość, z czego wynika
# różnica?

# 1.
krotka = (1, 2, 2)
zbior = {4, 5, 6}
slownik = {"a": 7, 
           "b": 8, 
           "c": 9}
lista = [-1, -2, -3]

# 2.
print("Zad 2")
print(len(krotka))
print(len(zbior))
print(len(slownik))
print(len(lista)) # len() przyjmuje dowolny iterowalny element

# 3. 
print("Zad 3")
for elem in krotka:
    print(elem)

for elem in lista:
    print(elem)

for key, val in slownik.items(): # iteracja po słowniku bez metod przechodzi tylko po kluczach
    print(elem)

for elem in zbior:
    print(elem)

# 4. 
print("Zad 4")
for val in slownik.values():
    print(val)

# 5.
print("Zad 5 - sposób 1")
for val in reversed(slownik.values()): # funkcja reversed() przyjmuje obiekty iterowalne i zwraca obiekt iterowalny (można po nim przechodzić jak po range())
    print(val)

print("Zad 5 - sposób 2")
for val in list(slownik.values())[::-1]: # konwersja na listę, a następnie odwrócenie jej kolejności mechanizmem slicingu
    print(val)

print("Zad 5 - sposób 3")
odwrotne = list(slownik.values())
odwrotne.reverse()
for elem in odwrotne:
    print(elem)

# 6. 
print("Zad 6")

lista.extend(krotka)
lista.extend(zbior)
lista.extend(slownik.values()) # extend przyjmuje dowolny obiekt, po którym możemy iterować.

print(slownik.values()) # jest złożonym obiektem
print(lista) # ale przy wstawieniu do extend już jest

# 7. 
print("Zad 7 - sposób prosty")
lista.append(max(lista))
lista.append(min(lista))

print("Zad 7 - sposób na popisówkę :P")
lista.extend([max(lista), min(lista)])

print(lista)

# 8.
print(f"Zad 8: {len(lista)}")

# 9. 
krotka2 = tuple(lista)
print(f"Zad 9: {len(krotka2)} {krotka2}")

# 10. 
zbior2 = set(krotka2)
print(f"Zad 10: {len(zbior2)} {zbior2}") # różnice wynikają z obecności duplikatów, które są kasowane przy konwersji na zbiór


print("Dry dry :)")