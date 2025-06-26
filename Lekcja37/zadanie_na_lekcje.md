## Wyrażenia listowe

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
slowa = ["ala", "kot", "pies", "kamilslimak", "zebra", "madam", "Adam"]
```
napisz wyrażenie listowe, które utworzy listę zawierającą same palindromy (wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej). Następnie wypisz proszę 

*Wskazówka - dla listy lub stringa `a` odwrócenie jego kolejności osiągamy wyrażeniem `a = a[::-1]`*

3. Na podstawie listy krotek zawierającej długości boków trójkąta stwórz listę zawierającą tylko krotki z których można skonstruować trójkąt (warunek - najdłuższy bok musi być krótszy niż suma dwóch pozostałych).
```py
trojkaty = [(1, 3, 5), (2, 2, 3), (3, 1, 8), (3, 4, 5)]
```

4. Z podanego ciągu znaków usuń znaki będące literami.
```py
sequence = "hello@123world!456"
```
*Wskazówka - dla pojedynczego znaku metoda `c.islower()` zwraca True, jeżeli znak jest małą literą.*

## Obsługa wyjątków

1. Proszę zaimplementować funkcję zgodnie z szablonem
```py
def dzielenie_i_mnozenie(a, b):
    pass
```
która przyjmie dwie wartości `a` i `b`, a następnie wyświetli wynik działania `a/b` i `a*b`. Co się wydarzy jeżeli nie zaimplementujemy obsługi wyjątków i spróbujemy dzielić przez 0? 

2. Proszę uzupełnić powyższą funkcję w taki sposób, aby wypisywała do konsoli błąd, jeżeli podane dane nie będą typu `int` (bez takiego wyjątku dopuszczone zostaną również typy `float`. `bool` również zostanie dopusczony, pod warunkiem że `b != False`).