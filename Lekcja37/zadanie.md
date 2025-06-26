1. Korzystając z poniższej funkcji proszę napisać wyrażenie listowe, które utworzy listę zawierającą wszystkie liczby **złożone** w przedziale od 0 do 50. Proszę następnie wypisać tę listę do konsoli. Proszę pamiętać o tym, jakie warunki musi spełnić liczba pierwsza!

```py
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
```

2. Na podstawie podanej listy 
```py
slowa = ["ala", "kot", "pies", "kamilslimak", "zebra", "madam", "Adam"] stwórz listę 
```
zawierającą same palindromy (wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej).