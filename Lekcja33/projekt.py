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

def bubble_sort():
    