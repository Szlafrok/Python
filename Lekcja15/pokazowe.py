# Systemy liczbowe

# Proszę zaimplementować funkcję, która przyjmie jako argument stringa zawierającego liczbę w systemie binarnym
# i przekonwertuje tę liczbę na system dziesiętny

def deci(bin: str) -> int:
    i = len(bin) - 1 # Indeks ostatniego znaku stringa bin
    potega = 1 # Potęga dwójki przez którą mnożymy
    res = 0 # Zmienna do przechowywania wyniku
    while i >= 0:
        res += int(bin[i]) * potega
        i -= 1
        potega *= 2
    return res

print(deci("11001")) # ->



def bin(deci: int) -> str:
    res = ""

    while deci > 0:
        znak = str(deci % 2)       
        deci //= 2
        res = znak + res
    return res

print(bin(213))




a = ""
a[::-1] # Odwrócony string lub lista

def palindrom(a: str) -> bool:
    return a == a[::-1]



def is_prime(n: int) -> bool:
    d = 3
    while d < n:
        if n % d == 0:
            return False
    return True






# Przykład 1: dziesiętne -> binarny

#  Zadanie 1: binarny -> dziesiętny

# Powtórzenie wiadomości - Liczby pierwsze

#  Zadanie 2: is_prime(n)

# Palindromy

#  Zadanie 3: Czy wyrażenie jest palindromem?