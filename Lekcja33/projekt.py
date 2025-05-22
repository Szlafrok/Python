from random import randint

def losowe():
    liczby = []
    for i in range(20):
        liczba = randint(1, 100)
        liczby.append(liczba)
    return liczby

print(losowe())



slownik = {
    "niebieski":40,
    "fiat_punto":0,
    "imie" : "Stefan",
    "nazwisko" : "Wyszyński",
    "adres" : {
        "ulica": "Kwiatowa",
        "numer": 10,
        "miasto": "Kraków"
    },
    "lista": [5, 4, 3, 2 , 1]
}

print(slownik["niebieski"])
print(slownik["imie"])
print(slownik["adres"]["ulica"])
print(slownik["lista"][0])


a, b = (5, 4)

for klucz in slownik.keys():
    print(klucz)

for wartosc in slownik.values():
    print(wartosc)

for klucz, wartosc in slownik.items():
    print(klucz, wartosc)

print("----------------------------")
liczby = losowe()
print(liczby)

def bubble_sort(liczby):
    n = len(liczby)
    for i in range(n):
        for j in range(0, n-1-i):
            if liczby[j+1] > liczby[j]:
                liczby[j], liczby[j+1] = liczby[j+1], liczby[j]
    return liczby

liczby = bubble_sort(liczby)
print(liczby)


def is_in(liczby, val): # nie wolno zrobić np. return liczby in val
    n = len(liczby)
    for i in range(n):
        if val == liczby[i]:
            return True
    return False

def find_max(liczby):
    n = len(liczby)
    res = liczby[0]
    for i in range(1, n):
        if liczby[i] > res:
            res = liczby[i]
    return res

print(is_in(liczby, 50))
print(find_max(liczby))

def binary_search(liczby, val):
    n = len(liczby)
    low = 0
    high = n - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2

        if liczby[mid] > val:
            low = mid + 1

        elif liczby[mid] < val:
            high = mid - 1

        else:
            return True
        
    return False

liczby = [97, 89, 86, 84, 81, 79, 73, 62, 62, 46, 46, 42, 40, 34, 33, 31, 27, 18, 10, 4]
print(binary_search(liczby, 78))