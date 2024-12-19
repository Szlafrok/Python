# zadanie 1
def suma_kwadratow(lista):
    return sum(x ** 2 for x in lista)

# Przykład użycia:
print(suma_kwadratow([1, 2, 3, 4, 5]))  # Wynik: 55

# Jest spoko, ładne, zwięzłe rozwiązanie :)

# 3/3



# zadanie 2
def logowanie(popr_login, popr_haslo, n):
    for i in range(n):
        login = input("Podaj login: ")
        haslo = input("Podaj hasło: ")
        if login == popr_login and haslo == popr_haslo:
            return True
        print(f"Pozostało prób: {n - i - 1}")
    return False

# Przykład użycia:
print(logowanie("admin", "1234", 3))  # Funkcja prosi o login i hasło do 3 prób

# Elegancko. Brawo!
# (3/3)


#zadanie 3



def cyfry(n):
    return sum(int(cyfra) for cyfra in str(n)) # Bardzo sprytnie zrobione!

# Przykład użycia:
print(cyfry(1235))  # Wynik: 11 (1 + 2 + 3 + 5)

# (2/2)