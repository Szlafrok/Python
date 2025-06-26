# WYRAŻENIA LISTOWE

# Zadanie 1

def is_prime(n: int) -> bool: # zwraca True gdy n jest pierwsze, False jeżeli nie
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    d = 3
    while d <= n**0.5:
        if n % d == 0:
            return False
        d += 2
    return True

sol_a = [x for x in range(0, 51) if x > 1 and not is_prime(x)] # złożona: musi być większa od 1 i nie może być pierwsza
print(sol_a)


# Zadanie 2

slowa = ["ala", "kot", "pies", "kamilslimak", "zebra", "madam", "Adam"]

sol_b = [x for x in slowa if x == x[::-1]] # sprawdzamy czy słowo i odwrócone słowo są takie same
print(sol_b)

# Zadanie 3

trojkaty = [(1, 3, 5), (2, 2, 3), (3, 1, 8), (3, 4, 5)]

sol_c = [t for t in trojkaty if sum(sorted(t)[:2]) > max(t)] # sposób 1: sortujemy boki trójkąta rosnąco i porównujemy sumę dwóch pierwszych z trzecim
sol_c = [t for t in trojkaty if sum(t) - max(t) > max(t)] # sposób 2: sumujemy boki trójkąta i odejmujemy najdłuższy - zostają pozostałe 2 - i porównujemy z najdłuższym
print(sol_c)


def dzielenie_mnozenie(a, b): # sposób 1
    try:
        if b == 0: # b to dzielnik
            raise Exception("Nie można dzielić przez 0!")
    except Exception as e:
        print(e)
    else:
        print(a/b)
        print(a*b)

print(dzielenie_mnozenie(5, 0))
print(dzielenie_mnozenie(5, 2))


def dzielenie_mnozenie_2(a, b): # sposób 2
    try:
        return a/b, a*b # próbujemy od razu zwrócić wartość; jeżeli b == 0, nie uda się i mamy wyjątek
    except Exception as a:
        print(a)
        return None # brak wyniku, zwracamy None
    
print(dzielenie_mnozenie_2(5, 0))
print(dzielenie_mnozenie_2(5, 2))