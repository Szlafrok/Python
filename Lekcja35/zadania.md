1. a) (2 pkt) W liście `wartosci` przechowujemy typy danych:
> - int (liczba całkowita)
> - float (liczba zmiennoprzecinkowa)
> - str (string)
> - bool (wartość logiczna)
> - tuple (krotka)
Przykładowo:
```py
lista = [4, 6, 2.5, 1,2, "zabawny", "tekst", True, False, (0, 0)]
```
Proszę wykonać kilka eksperymentów na sortowaniu takiej listy - jakie typy danych nie są dopuszczalne przy sortowaniu?
b) (3 pkt) Następnie proszę zaimplementować funkcję
```py
def list_purge(arr: list):
    # miejsce na Twoją implementację
    return arr
```
która usunie z podanej w argumencie listy `arr` wszystkie spośród wymienionych powyżej typów danych, które uniemożliwiają sortowanie. Wskazówka: Proszę skorzystać z funkcji
```py
isinstance(val, typ) 

# Przykłady:
isinstance(15, int) # True
isinstance("inwokacja", float) # False
```
która zwraca True, jeżeli podana wartość `val` ma typ `typ`, lub False, jeżeli tak nie jest.
Powodzenia!

2. (3 pkt) Wykonaj następujące polecenia: 
> - Stwórz 2 listy składające się z 3 liczb każda
> - Połącz stworzone wcześniej listy
> - Usuń elementy z indeksami 2 i 5 , który element należy usunąć najpierw?
> - Usuń największą i najmniejszą liczbę z listy
> - Dodaj liczbę do listy
> - Posortuj listę
> - Utwórz kopię listy
> - Odwróć kolejność elementów w kopii
> - Dodaj do każdej wartości w oryginalnej liście 1, a w kopii odejmij 1
> - Wyświetl obie listy

3. (3 pkt) Proszę napisać funkcję, która przyjmie jako argument listę liczb całkowitych, a następnie usunie z niej powtarzające się elementy (jeżeli są 3 takie same elementy, powinien zostać tylko 1) i zwróci tak poprawioną listę.
Szablon:
```py
def unikaty(arr: list):
    # Miejsce na Twoją implementację
    return arr
```

Bonusowe (+1 pkt): Zwracana lista powinna zachować tę samą kolejność pośród elementów, które nie zostały usunięte ;)