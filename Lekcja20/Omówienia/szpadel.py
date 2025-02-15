osoba_1 = {
    "imie" : "Jan",
    "nazwisko" : "Kowalski",
    "wiek" : 32
}

osoba_2 = {
    "imie" : "Michał",
    "nazwisko" : "Paluch",
    "wiek" : 17
}

osoba_3 = {
    "imie" : "Jarek",
    "nazwisko" : "Kościuszko",
    "wiek" : 43
}

osoba_4 = {
    "imie" : "Władysław",
    "nazwisko" : "Chrobry",
    "wiek" :8 
}

print(osoba_1["imie"])
print(osoba_1["nazwisko"])
print(osoba_1["wiek"])

if osoba_1["wiek"] >= 18:
    print("Jesteś pełnoletni\n")
else:
    print("Nie jesteś pełnoletni\n")

print(osoba_2["imie"])
print(osoba_2["nazwisko"])
print(osoba_2["wiek"])

if osoba_2["wiek"] >= 18:
    print("Jesteś pełnoletni\n")
else:
    print("Nie jesteś pełnoletni\n")

print(osoba_3["imie"])
print(osoba_3["nazwisko"])
print(osoba_3["wiek"])

if osoba_3["wiek"] >= 18:
    print("Jesteś pełnoletni\n")
else:
    print("Nie jesteś pełnoletni\n")

print(osoba_4["imie"])
print(osoba_4["nazwisko"])
print(osoba_4["wiek"])

if osoba_4["wiek"] >= 18:
    print("Jesteś pełnoletni\n")
else:
    print("Nie jesteś pełnoletni\n")

def polacz(ciag: list) -> str:
    res = ""
    for elem in ciag:
        res += str(elem) + " "
    return res[:-1]


druk = list(osoba_4.values())

print(polacz(druk))