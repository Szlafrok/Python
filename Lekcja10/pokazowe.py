# ITEROWANIE PO STRINGACH

# WPROWADZENIE DO FUNKCJI

imiona = ["Zenek", "Amir", "Harold", "Hermiona", "Leszek"]
nazwiska = ["Martyniuk", "Dostawski", "Sokół", "Bajtocka", "Adamski"]
staz_pracy = [2, 1, 14, 8, 9]

# (Wypisać imiona i nazwiska, a następnie staż pracy wszystkich zawodników)

def zawodnik(x):
    print(f"Jestem {imiona[x]} {nazwiska[x]}")
    print(f"Pracuję w tej firmie {staz_pracy[x]} lat")

for i in range(5):
    zawodnik(i) # Wywołanie funkcji


# ------- ZADANIE SAMODZIELNE 1 -------
print("--------------------")

def statki():
    for i in range(5):
        print("Błyskawica stoi w porcie w Gdyni")

statki()

def powitanie():
    print("dry dry witam")

powitanie()

# Proszę napisać funkcję powitanie(), która wypisze w konsoli jakiś zabawny tekst.
# Proszę ją następnie wywołać.


# ARGUMENTY

print("Ta treść jest argumentem")

for i in range(1, 5, 2): # 1, 5 i 2 to są ARUGMENTY tej funkcji
    pass

def powitanie(imie, nazwisko):
    print(f"Cześć, jestem {nazwisko*2} {imie}")

powitanie("Włodek", "Biały")



def powitanie(imie, nazwisko = "Makłowicz"):
    print(f"Cześć, jestem {nazwisko} {imie}")

powitanie("Mieszko")


powitanie(nazwisko= "Wołodyjowski", imie = "Pan")

# (powitanie() z argumentem imie)
# (powitanie() z argumentami imie, powtorzenia)
# (powitanie() z argumentami imie i powtorzeniami z wartością domyślną)

# ------- PRZYKŁAD -------

# Proszę napisać funkcję pasek_ladowania(gotowe, limit), przyjmującą jako argumenty:
# > liczbę całkowitą (gotowe), która wyraża punkt postępu
# > liczbę całkowitą (limit), która wyraża, ile punktów postępu powinno zapełnić pasek do końca. Domyślna wartość: 100

# Funkcja powinna wydrukować w konsoli pasek postępu, reprezentujący aktualny poziom postępu. Pasek
# powinien mieć długość 10 znaków.

# Wykorzystamy znacznik \r w princie: print(f"\r", end = ' ')

# [##########] - 100%
# [#####-----] - 50%

def pasek_ladowania(gotowe, limit = 100): # Procent postępu to gotowe / limit. Gotowe == Limit: 100%
    punkty_postepu = gotowe * 10 // limit
    print(f"\r[{"#" * punkty_postepu}{"-" * (10 - punkty_postepu)}]", end = " ")


from time import sleep
for i in range(1, 101):
    pasek_ladowania(i, 100)
    sleep(0.03)

print("Mieszko Książe Polski", end = " ")
print("\rMIESZ")




# ----- ZADANIE SAMODZIELNE 2 -----

# Napisz funkcję, która przyjmuje dwa argumenty: n - liczba powtórzeń, a -
# liczba startowa. Funkcja ma generować kolejne kwadraty liczb, zaczynając od a. Ma
# wyświetlić n kolejnych liczb.


# kwadraty(5, 3) -> 9, 16, 25, 36, 49 - kwadraty liczb 3, 4, 5, 6, 7
# kwadraty(2, 9) -> 81, 100
# kwadraty(8, -2) -> 4, 1, 0, 1, 4, 9, 16, 25

def kwadraty(n = 5, a = 2): # n to liczba powtórzeń, a to liczba startowa
    for i in range(n):
        print(a**2)
        a += 1

kwadraty(5, 2)