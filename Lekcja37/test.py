def is_even(n):
    return True if n%2 == 0 else False

L = [n if n%2 == 0 else 0 for n in range(20)]

print(L)

def is_prime(n: int) -> bool:
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

for i in range(100):
    if is_prime(i):
        print(i)

lista = [1,2,3,4,5,6,7,8,9,50]
kwadraty = (i**2 for i in lista)
print(kwadraty)
kwadraty = {i**2 for i in lista}
print(kwadraty)
kwadraty = {i:i**2 for i in lista}
print(kwadraty)