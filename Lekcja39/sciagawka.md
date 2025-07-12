# Powtórka – Python, NumPy i podstawy obsługi tablic

## Interpretacja, a kompilacja
Python jest językiem interpretowanym, a jego struktura i elastyczność, choć bardzo ułatwiają działanie w nim, znacznie ograniczają szybkość programów napisanych w tym języku. NumPy jest głównie napisane w języku C, języku kompilowanym i bardziej ograniczonym pod kątem pracy na nim, a przez to o wiele wydajniejszym.

| Cecha                      | Interpretacja                   | Kompilacja                         |
|---------------------------|----------------------------------|------------------------------------|
| **Sposób działania**          | Kod wykonywany linijka po linijce | Kod tłumaczony całościowo do pliku binarnego, zrozumiałego dla komputera |
| **Kiedy wykrywają błędy**     | W trakcie działania              | Przed uruchomieniem                |
| **Prędkość działania**        | Wolniejsza                       | Szybsza                            |
| **Przykład języka**           | Python, JavaScript,               | C, C++, Rust                       |

---

## NumPy – co to i po co?

**NumPy** to biblioteka do obliczeń numerycznych w Pythonie.

- Wprowadza tablice (array) – wydajniejsze niż listy
- Umożliwia szybkie operacje na dużych zbiorach danych
- Obsługuje wektory, macierze, statystykę, losowość

---

## Czym jest tablica NumPy?

- To **jednorodna struktura danych** (wszystkie elementy tego samego typu)
- Może być 1D, 2D, 3D, ... (jedno, dwu, trójwymiarowa)
- Zwykle szybsza niż lista, dzięki swoim ograniczeniom nie musi sprawdzać wielu warunków, które musi sprawdzać lista (np. typ danych, długość listy).

---

## 📊 Tablica vs Lista – różnice

| Cecha                 | Lista (`list`)          | Tablica NumPy (`np.array`)      |
|----------------------|-------------------------|---------------------------------|
| Typy danych          | Mogą być różne          | Muszą być takie same            |
| Prędkość działania   | Wolniejsza              | Szybsza          |
| Operacje matematyczne| Trzeba pisać pętle      | Można robić zbiorczo            |
| Wymiary              | Tylko 1D, ale możemy zagnieżdżać w niej inne struktury, także listy   | Wielowymiarowa |

---

## Funkcje i metody NumPy

### 🔹 `np.array(data, dtype=...)`
Tworzy tablicę. Można podać typ:

- `'U'` – string (np. `dtype='U'`)
- `'f'` – float (np. `dtype='f'`)
- `'i'` – int (np. `dtype='i'`)

Argument `dtype` jest nieobowiązkowy - jeżeli podajemy poprawne dane (np. same inty i floaty), to NumPy wybierze odpowiedni typ i sam zrzutuje na niego zawartość tablicy (tutaj wybierze float). 

Uwaga na pojęcie: **rzutowanie danych** to zmiana ich typu na inny typ.

```py
np.array(["1", "2", 3.1], dtype='i') # -> [1 2 3]
```

---

### 🔹 `arr.reshape(...)`

Zmienia kształt istniejącej tablicy bez zmiany jej danych.

- Można użyć `-1` jako wymiaru, by NumPy wyliczyło go automatycznie. Możemy tak zamienić **tylko jeden wymiar**.

```python
arr = np.array([1, 2, 3, 4, 5, 6])
arr.reshape((2, 3))     # macierz 2x3
arr.reshape((3, -1))    # automatycznie zgadnij liczbę wierszy
```

---

### 🔹 `np.array_split(array, n)`

Dzieli tablicę na `n` podtablic (równych lub prawie równych rozmiarów). Uwaga: Jeżeli liczba elementów w podanej tablicy jest niepodzielna przez `n`, wówczas niektóre tablice będą miały `n+1` elementów. Przykładowo:

```py
arr = np.array([1, 2, 3, 10, 4, 5, 6, 7, 8, 9]) # 10 elementów
spl_arr = np.array_split(arr, 3)
for a in spl_arr:
    print(a) # wypisze po kolei: [1 2 3 10], [4 5 6], [7 8 9] # n = 3: Pierwsza tablica ma n+1 elementów.
```

---

### 🔹 `np.random.randint(limit, size=...)`

Zwraca losowe liczby całkowite z zakresu `[0, limit)`, czyli cały ten przedział z wzięciem pod uwagę zera, ale nie wartości podanej jako limit.

- `limit`: górna granica wartości
- `size`: ile wartości wylosować - wówczas zwróci nam tablicę złożoną z takich liczb.

```python
np.random.randint(10, size=5) # -> [3 7 1 9 4]
```

---

### 🔹 `np.random.rand(d1, d2, ...)`

Generuje losowe liczby zmiennoprzecinkowe z przedziału `[0.0, 1.0)`.

```python
np.random.rand(2, 3)
```

---

### 🔹 `np.random.choice(data, size=...)`

Losowy wybór elementów z `data`.

- `data`: lista lub tablica z możliwymi wartościami
- `size`: ile wartości wybrać

```python
np.random.choice([1, 2, 3], size=4) # -> [2 2 1 3]
```

---

### 🔹 `np.random.shuffle(arr)` vs `np.random.permutation(arr)`

| Funkcja               | Opis                                        |
|-----------------------|---------------------------------------------|
| `np.random.shuffle`   | Tasuje **w miejscu** (modyfikuje oryginał)  |
| `np.random.permutation` | Zwraca **nową przetasowaną tablicę**      |

---

### 🔹 `np.linspace(start, stop, num)`

Zwraca `num` równomiernie rozłożonych wartości od `start` do `stop`.

```python
np.linspace(0, 1, 5)  # -> [0.   0.25 0.5  0.75 1.  ]
```

---

### 🔹 Funkcje analityczne

```python
np.sum(arr)    # suma wszystkich wartości
np.min(arr)    # najmniejsza wartość
np.max(arr)    # największa wartość
np.mean(arr)   # średnia
np.var(arr)    # wariancja
np.std(arr)    # odchylenie standardowe
```

---

### 🔹 Stałe i funkcje matematyczne
Przydatne przy zaawansowanych obliczeniach matematycznych - to tajemniczy mysi sprzęt, który może pomóc Wam potem!

```python
np.pi       # π = 3.14159...
np.e        # e = 2.71828...
np.exp(x)   # e^x
np.round(x) # zaokrąglenie
```