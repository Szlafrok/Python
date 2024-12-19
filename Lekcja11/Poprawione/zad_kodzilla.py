# Zadanie 1

def znajdz_pary(lista, n):
    pary = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == n:
                pary.append((lista[i], lista[j]))
    return pary

# Fajne! (3/3)

# Zadanie 2
def logowanie(popr_login, popr_haslo, n):
    for i in range(n):
        login = input("Podaj login: ")
        haslo = input("Podaj hasło: ")
        if login == popr_login and haslo == popr_haslo:
            return True
        print(f"Niepoprawne dane. Pozostało prób: {n - i - 1}")
    return False

# Bardzo ładnie! (3/3)

# Zadanie 3
def cyfry(n):
    suma = 0
    while n > 0:
        suma += n % 10
        n //= 10
    return suma

# Również bardzo ładnie, ba, wręcz książkowo :P (2/2)


# Zadanie 5
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def ciag(liczby): # Nie było wstawki o argumencie, ale nie wymieniłem go w zadaniu, więc nie obetnę punktów
    max_length = 0
    current_length = 0

    for liczba in liczby:
        if is_prime(liczba):
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0

    return max_length

# Pięknie! (+5/5)