### Moduły i klasy
`from fpdf import FPDF` – importuje główną klasę do tworzenia PDF-ów.

`from fpdf.enums import XPos, YPos` – importuje stałe do sterowania pozycją kursora po wypisaniu tekstu lub grafiki.

`import glob` – umożliwia pobieranie ścieżek do wielu plików z np. danego folderu

### Tworzenie PDF-a
`pdf = FPDF()` – tworzy nowy obiekt PDF.

`pdf.add_page()` – dodaje nową stronę do dokumentu.

`pdf.output(path)` – zapisuje gotowy plik PDF do podanej ścieżki.

### Czcionki
`pdf.add_font(name, style, path)` – dodaje czcionkę z pliku .ttf (np. DejaVuSansCondensed). Należy to zrobić raz.

`pdf.set_font(name, size=...)` – ustawia aktualną czcionkę dla tekstu, który zaraz zostanie wypisany. Argument size określa rozmiar.

**Różnica między add_font, a set_font:** `add_font` - dodaje czcionkę do puli; `set_font` - wybiera ją do użycia.

`pdf.set_text_color(r, g, b)` – ustawia kolor tekstu w RGB. Wszystkie zmienne `r, g, b` wybieramy w przedziale od `0` do `255`. Ustawienie RGB na `(0, 0, 0)` daje kolor czarny, `(255, 255, 255)` daje kolor biały.

### Tekst i obraz
`pdf.text(x, y, text)` – umieszcza tekst w absolutnej pozycji na stronie. Pozycja absolutna `(x, y)` to pozycja niezależna od jakichkolwiek innych elementów na stronie - wyznaczamy ją tylko i wyłącznie względem **lewego górnego** rogu kartki, gdzie współrzędne wynoszą `(0, 0)`.

`pdf.image(path, x=..., y=..., w=..., h=...)` – wstawia grafikę do dokumentu PDF w określonym miejscu i rozmiarze. Jednostki to mm.

### Komórki i kursor
W kontekście biblioteki fpdf2, **kursor** to niewidoczny punkt określający, gdzie na stronie będzie rysowany kolejny element (tekst, obraz, tabela itd.). Każde polecenie, np. `pdf.cell()`, może przesuwać ten kursor dalej, żeby kolejne treści się nie nakładały.

`pdf.cell(w, h, text, new_x=..., new_y=..., align="L/C/R")` – wypisuje pojedynczą linię tekstu, często używaną jako nagłówek. Parametry new_x i new_y sterują, gdzie znajdzie się następny tekst. Parametr align pozwala określić, czy tekst będzie wyrównany do lewej, prawej, lub do środka.

`pdf.multi_cell(w, h, text, ...)` – jak `pdf.cell()`, ale automatycznie łamie tekst na linie, jeśli jest za długi.

Argument `link = pdf.image(...)` w `pdf.cell()` – umożliwia osadzenie obrazka w komórce. W tym przypadku to skrót, żeby dodać obrazek i od razu przesunąć kursor.