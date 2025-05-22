## Zadanie domowe

### 1)
*Termin wykonania: 05.06 / 4 pkt*

Proszę napisać program, który losuje i podaje użytkownikowi losową liczbę z zakresu 1000.
Proszę następnie napisać program, który będzie zgadywał tę liczbę, a my będziemy udzielać mu odpowiedzi
w postaci "za mało" / "za dużo" / "tak", zależnie od tego, czy zgadnięta liczba jest mniejsza lub większa
od wylosowanej liczby, lub poprawna.

Program powinien korzystać z algorytmu, który umożliwi mu zgadnięcie prawidłowej liczby w możliwie najmniejszej
liczbie prób. 

(Bonusowe 1.5 pkt: Proszę podać i uzasadnić, dla jakiej przykładowo wylosowanej liczby komputer będzie potrzebował
najwięcej prób. Ile będzie potrzebował tych prób?)

### 2)
*Termin wykonania: 05.06 / 4 pkt*

https://pl.wikipedia.org/wiki/Sortowanie_przez_wybieranie

Sortowanie przez wybór to typ sortowania, który działa w następujący sposób:

Wybieramy granice przedziału `low = 0` oraz `high = n - 1`. Z przedziału tablicy od `low` do `high` wybieramy element największy i zamieniamy go miejscami z elementem ostatnim. Zmniejszamy high o 1 i wybieramy element największy spośród nowego przedziału, z którego usunęliśmy poprzedni element największy. W ten sposób wybieramy kolejne elementy największe i układamy je po kolei od końca, uzyskując posortowaną rosnąco listę.

Proszę zaimplementować funkcję
```py
def selection_sort(arr: list) -> list:
    pass
```
która zwróci posortowaną listę `arr`. Program powinien wykorzystywać zapisaną na lekcji funkcję `find_max()` oraz algorytm sortowania przez wybór.



## Zadanie dodatkowe
*Termin wykonania: 05.06 / +5 pkt*
*Vincent, Wiktor, Patryk, Bazi*

https://www.algorytm.edu.pl/grafy/bfs.html
Algorytm BFS (Przeszukiwanie wszerz) to wykorzystujący kolejki algorytm służący do przeszukiwania grafów. Każdy graf w matematyce to połączenie wierzchołków i krawędzi je łączących. Za pomocą grafu możemy przykładowo utworzyć mapę międzymiejskich połączeń kolejowych, tak jak na rysunku w pliku miasta.png. 

Taki graf możemy przedstawić w formie tzw. listy sąsiedztwa - listy zawierającej listę wierzchołków, gdzie wewnętrzna lista o danym indeksie przechowuje wszystkie punkty, z którymi sąsiaduje dany wierzchołek. Dla przykładu z obrazka lista będzie wyglądać tak:
```py
MIASTA = [
    [1],
    [0, 2, 3],
    [1, 3],
    [2, 4],
    [3]
]
```
oznacza to, że miasto 0 jest połączone z miastem 1, miasto 1 jest połączone z miastami 0, 2 i 3, etc.

Algorytm BFS przyjmuje wybrane miasto jako punkt startowy i przeszukuje graf warstwami. W każdym kolejnym cyklu rozpatruje **sąsiadów miast, którzy byli sprawdzani poprzednio.** Zapisujemy przy tym, które miasto zostało już
odwiedzone, aby nie rozpatrywać go ponownie.

1. W pierwszym cyklu rozpatrzymy miasto 0
2. W drugim cyklu rozpatrzymy jego sąsiada - miasto 1
3. W trzecim cyklu rozpatrzymy miasta 2 oraz 3 (miasto 0 już było rozpatrzone)
4. W czwartym cyklu rozpatrzymy miasto 4 (miasta 1, 2 i 3 były już rozpatrzone)

W praktyce ten algorytm opiera się na kolejce. Tworzymy listy na podstawie liczby wierzchołków:

```py
from math import inf

n = len(MIASTA)
distances = [None] * n
visited = [False] * n
```
Lista distances przechowuje dystans od punktu startowego, do punktu o podanym indeksie. Lista visited przechowuje informację, czy miasto o danym indeksie zostało już odwiedzone.

Algorytm korzysta z kolejki, aby przechowywać kolejne wierzchołki, które będziemy odwiedzać. Dla każdego miasta, które wyciągamy z kolejki:
- zapisujemy jego odległość od startu
- badamy, czy ma sąsiadów, których jeszcze nie odwiedziliśmy; jeżeli tak, dodajemy ich do kolejki i oznaczamy jako odwiedzonych.

W pseudokodzie wygląda to tak:
```
utwórz listę przechowującą odległości od miasta startowego
utwórz listę True/False, przechowującą informację czy dane miasto zostało odwiedzone
utwórz kolejkę
dodaj do kolejki miasto startowe oraz jego dystans (0)
oznacz miasto startowe jako odwiedzone

dopóki kolejka nie jest pusta:
    wyjmij z kolejki miasto oraz jego dystans (**d**)
    zapisz dystans miasta do listy
    dla każdego spośród wszystkich sąsiadów miasta:
        jeżeli sąsiad nie został odwiedzony:
            dodaj do kolejki sąsiada oraz jego dystans(**d+1**)
            oznacz sąsiada jako odwiedzony

wypisz do konsoli listę odległości
```
Dla naszego przykładu z pliku miasta.png - określamy miasto 0 jako startowe:
1. Wkładamy do kolejki miasto 0
2. Wyjmujemy z kolejki miasto 0
> - Dystans miasta 0 od miasta 0 = 0
> - Wkładamy do kolejki miasto 1
3. Wyjmujemy z kolejki miasto 1
> - Dystans miasta 1 od miasta 0 = 1
> - Wkładamy do kolejki miasto 2
> - Wkładamy do kolejki miasto 3
4. Wyjmujemy z kolejki miasto 2
> - Dystans miasta 2 od miasta 0 = 2
> - Brak nowych miast wkładanych do kolejki - wszystkie już odwiedziliśmy lub są w kolejce
5. Wyjmujemy z kolejki miasto 3
> - Dystans miasta 3 od miasta 0 = 2
> - Wkładamy do kolejki miasto 4
6. Wyjmujemy z kolejki miasto 4
> - Dystans miasta 4 od miasta 0 = 3
> - Brak nowych miast wkładanych do kolejki - wszystkie już odwiedziliśmy lub są w kolejce
7. Kolejka jest pusta - zwracamy listę odległości. Koniec algorytmu.

Wasze zadanie jest następujące:
**Proszę zaimplementować w Pythonie algorytm BFS.**
# Powodzenia!!!