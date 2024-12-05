def dzialanie(a, b):
    print(a * b + a + b)

# ZADANIE NA ROZGRZEWKĘ

# Proszę napisać funkcję trojkat(a), która obliczy i
# wyprintuje w konsoli pole trójkąta równobocznego o boku
# a.

# P = a**2 * sqrt(3) / 4

from math import sqrt

def trojkat(a):
    p = a**2 * sqrt(3) / 4
    print(p)



def kwadrat(a):
    print("dry dry")
    print("kremówek")
    #return a + 5
    if True:
        return 1
    print("delulu")
    print("pan Piotrek zjadł współlokatora")

k = kwadrat(6)
print(k)


# Proszę napisać funkcję logowanie(login, haslo). Funkcja powinna pytać użytkownika o
# login i hasło, a następnie zwrócić True, jeżeli logowanie się powiodło lub False,
# jeżeli się nie powiodło.

def logowanie(login, haslo):
    l = input("Podaj login: ")
    h = input("Podaj hasło: ")

    if l == login and h == haslo:
        return True
    return False
    

def doskonala(n): # Liczba doskonała to taka liczba, której suma dzielników mniejszych od niej samej jest równa jej
    # 6 = 1 + 2 + 3
    i = 1
    total = 0
    while i < n:
        if n % i == 0: # Jeżeli i jest dzielnikiem n
            total += 1
        i += 1

    if total == n:
        return True
    # (else, ale działa również bez niego)
    return False

n = int(input("Podaj liczbę, co do której chcesz się dowiedzieć, czy jest doskonała: "))
n = 6
d = doskonala(n)

if d:
    print("Liczba jest doskonała")
else:
    print("Liczba nie jest doskonała")

if doskonala(n):
    print("Liczba jest doskonała")
else:
    print("Liczba nie jest doskonała")