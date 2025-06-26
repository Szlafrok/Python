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

sol_a = [x for x in range(0, 51) if x > 1 and not is_prime(x)]
print(sol_a)


# Zadanie 2

slowa = ["ala", "kot", "pies", "kamilslimak", "zebra", "madam", "Adam"]

sol_b = [x for x in slowa if x == x[::-1]]
print(sol_b)

# Zadanie 3

trojkaty = [(1, 3, 5), (2, 2, 3), (3, 1, 8), (3, 4, 5)]

sol_c = [t for t in trojkaty if sum(sorted(t)[:2]) > max(t)] # sposób 1
sol_c = [t for t in trojkaty if sum(t) - max(t) > max(t)] # sposób 2
print(sol_c)