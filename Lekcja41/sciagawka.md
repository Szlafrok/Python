# 📘 Ściągawka z Wyrażeń Regularnych (Python)

## ✅ 1. Czym są wyrażenia regularne?

**Wyrażenia regularne** (ang. regular expressions, regex) to wzorce tekstowe pozwalające na:
- wyszukiwanie danych w tekście (np. e-maili, dat, numerów),
- walidację formatów (np. PESEL, telefon), czyli sprawdzenie ich poprawności
- wyciąganie danych z tekstu,
- modyfikację tekstu (np. `re.sub()`).

---

## 🧠 2. Funkcje z modułu `re`

| Funkcja        | Co robi                                                     | Co zwraca                                |
|----------------|-------------------------------------------------------------|---------------------|
| `re.search()`  | Szuka **pierwszego dopasowania** gdziekolwiek w ciągu       | `Match` lub `None`                        |
| `re.match()`   | Sprawdza, czy **początek** ciągu pasuje do wzorca           | `Match` lub `None`                        |
| `re.findall()` | Zwraca **wszystkie dopasowania** jako listę                 | Lista stringów
| `re.sub()`     | Zamienia dopasowane fragmenty na nowy tekst                 | `str` – tekst po zamianie                |

---

## 🧱 3. Jak budować wyrażenie regularne

1. Zidentyfikuj wzorzec tekstowy (np. e-mail, liczba, PESEL).
2. Używaj klas znaków:
   - `\d` – cyfra
   - `\w` – litera, cyfra lub podkreślenie
   - `[a-zA-Z]` – tylko litery
3. Dodaj **kwantyfikatory**:
   - `+` – jedno lub więcej wystąpień
   - `*` – zero lub więcej
   - `{m,n}` – od m do n
4. Ustal granice dopasowania: `^` (początek), `$` (koniec)

> **Przykład:** `\d{5}-\d{6}[a-z]`  
> Dopasowuje np. `12345-678901a`

---

## 🎯 4. Metaznaki – Tabela

| Metaznak | Znaczenie                                   | Przykład dopasowania                         |
|----------|----------------------------------------------|----------------------------------------------|
| `.`      | Dowolny znak (oprócz nowej linii)            | `a.b` → `"acb"`, `"a_b"`, ale nie `"ab"`     |
| `\d`     | Cyfra (0–9)                                  | `\d{3}` → `"123"`                             |
| `\w`     | Znak alfanumeryczny lub `_`                  | `\w+` → `"abc_123"`                           |
| `\s`     | Biały znak (spacja, tab, enter)              | `\s+` → `" "` lub `\t`                        |
| `\b`     | Granica słowa                                | `\bcat\b` → `"cat"` ale nie `"category"`      |
| `^`      | Początek ciągu                               | `^Start` → dopasuje `"Start here"`           |
| `$`      | Koniec ciągu                                 | `end$` → dopasuje `"The end"`                |

---


## 🔢 5. Kwantyfikatory

| Kwantyfikator | Znaczenie                                          | Przykład                | Co dopasuje?                    |
|---------------|-----------------------------------------------------|--------------------------|---------------------------------|
| `*`           | 0 lub więcej razy                                   | `a*`                     | `""`, `"a"`, `"aaa"`            |
| `+`           | 1 lub więcej razy                                   | `a+`                     | `"a"`, `"aaa"`                  |
| `?`           | 0 lub 1 raz                                         | `a?`                     | `""`, `"a"`                     |
| `{m,n}`       | od **m** do **n** razy                              | `a{2,4}`                 | `"aa"`, `"aaa"`, `"aaaa"`       |
| `{m}`         | dokładnie **m** razy                                | `a{3}`                   | `"aaa"`                         |

---

## 🧱 6. Klasy znaków

**Klasa znaków** pozwala określić, jakie znaki są dopuszczalne na danej pozycji.

| Składnia         | Znaczenie                                     | Przykład         | Co dopasuje?            |
|------------------|-----------------------------------------------|------------------|-------------------------|
| `[abc]`          | Jeden znak: a, b lub c                        | `[ch]at`         | `"cat"`, `"hat"`        |
| `[a-z]`          | Małe litery                                   | `[a-z]+`         | `"abc"`, `"hello"`      |
| `[A-Z]`          | Duże litery                                   | `[A-Z]{2}`       | `"PL"`, `"US"`          |
| `[0-9]`          | Cyfry                                          | `\d == [0-9]`    | `"123"`, `"7"`          |
| `[^abc]`         | Dowolny znak **poza** a, b, c                 | `[^0-9]`         | `"a"`, `"@"`, `" "`     |

---

## 🧩 7. Grupowanie i alternatywa

| Składnia   | Znaczenie                                         | Przykład               | Co dopasuje?                  |
|------------|----------------------------------------------------|------------------------|-------------------------------|
| `( )`      | Grupowanie wyrażeń                                 | `(ab)+`                | `"ab"`, `"abab"`              |
| `|`        | Alternatywa („lub”)                                | `kot|pies`             | `"kot"` lub `"pies"`          |
| `(...)`    | Umożliwia wydzielenie **grup** do użycia np. `group()` | `(\d{3})-(\d{2})`   | `"123-45"` z dwiema grupami   |

---

## 🧷 8. Znaki specjalne i znak ucieczki `\`

Niektóre znaki mają specjalne znaczenie w regexach – jeśli chcesz użyć ich dosłownie, **musisz poprzedzić je `\`**:

| Znak    | Znaczenie domyślne     | Aby dopasować dosłownie      |
|---------|-------------------------|-------------------------------|
| `.`     | dowolny znak             | `\.`                          |
| `*`     | 0 lub więcej             | `\*`                          |
| `+`     | 1 lub więcej             | `\+`                          |
| `?`     | 0 lub 1                  | `\?`                          |
| `(`, `)`| grupowanie               | `\(`, `\)`                    |
| `[`, `]`| klasa znaków             | `\[` , `\]`                   |
| `\`     | znak ucieczki            | `\\`                          |

> Przykład: Aby dopasować dosłownie `1+1=2`, użyj: `1\+1=2`


## 🧪 Przykład kodu

```python
import re

text = "Użytkownik: jan.kowalski_123@example.com"
pattern = r"^[\w.]+@[a-zA-Z.]+$"

if re.search(pattern, text):
    print("To jest poprawny adres e-mail.")
else:
    print("To NIE jest poprawny adres e-mail.")
