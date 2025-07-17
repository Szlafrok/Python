## Model RGB

### ● Struktura:
○ Składa się z trzech komponentów: czerwonego (Red), zielonego (Green), i niebieskiego (Blue).
○ Każdy z tych kolorów jest reprezentowany przez wartość od 0 do 255.
○ Przykład: (255, 0, 0) to czysty czerwony, (0, 255, 0) to czysty zielony, (0, 0, 255)
to czysty niebieski, a (255, 255, 255) to biały.

### ● Jak działa:
○ Model RGB jest modelem addytywnym, co oznacza, że kolory są tworzone przez dodawanie
świateł trzech podstawowych barw (R, G, B).
○ Im wyższe wartości, tym jaśniejszy kolor.

### ● Zastosowanie:
○ Najczęściej używany w wyświetlaczach, monitorach, telewizorach, aparatach cyfrowych i
wszędzie tam, gdzie kolory są wyświetlane za pomocą światła.
○ W programowaniu i grafice komputerowej.


## Model HSV

### ● Struktura:
○ Hue (Odcień): Wartość od 0 do 360, która określa kolor, np. 0 = czerwony, 120 = zielony, 240 =
niebieski.
○ Saturation (Nasycenie): Wartość od 0% do 100%, gdzie 0% oznacza brak koloru (szarość), a
100% pełne nasycenie.
○ Value (Jasność): Wartość od 0% do 100%, gdzie 0% oznacza czarny, a 100% pełną jasność.
● Jak działa:
○ Model HSV jest bardziej intuicyjny dla ludzi, ponieważ oddziela pojęcia koloru (odcień),
intensywności (nasycenie) i jasności.
○ Jest oparty na modelu stożka kolorów, gdzie wartość "Hue" określa pozycję na kole kolorów.
### ● Zastosowanie:
○ Używany często w programach do edycji obrazów i grafiki,
○ Aplikacje graficzne


## Model CMYK

### ● Struktura:
○ Składa się z czterech komponentów: cyjan (Cyan), magenta (Magenta), żółty (Yellow) oraz
czarny (Key).
○ Każdy z tych kolorów jest reprezentowany przez wartość od 0% do 100%.
○ Przykład: (0%, 100%, 0%, 0%) to czysta magenta.
### ● Jak działa:
○ Model CMYK jest modelem subtraktywnym, co oznacza, że kolory są tworzone przez
odejmowanie świateł od białego papieru za pomocą tuszu lub farby.
○ Używa czarnego koloru (Key), ponieważ mieszanie cyjanu, magenty i żółtego nie daje idealnej
czerni.
### ● Zastosowanie:
○ Standardowy model w drukarstwie i publikacji materiałów.
○ Używany w projektowaniu wszelkich materiałów przeznaczonych do druku, takich jak plakaty,
ulotki czy książki.


## Model RGBA

### ● Struktura:
○ Rozszerzenie modelu RGB o Alpha, który reprezentuje przezroczystość.
○ Składa się z czterech komponentów: czerwonego (Red), zielonego (Green), niebieskiego
(Blue) oraz alpha (przezroczystość).
○ Alpha: Wartość od 0 do 1, gdzie 0 oznacza całkowitą przezroczystość, a 1 pełną
nieprzezroczystość.
○ Przykład: (255, 0, 0, 0.5) to półprzezroczysty czerwony.
### ● Jak działa:
○ Wartość alpha pozwala na kontrolowanie przezroczystości koloru, co jest przydatne w
nakładaniu kolorów lub tworzeniu efektów wizualnych.
○ Kolor w tym modelu jest wyświetlany jako mieszanka RGB z uwzględnieniem przezroczystości.
### ● Zastosowanie:
○ W grafice komputerowej, tworzeniu aplikacji webowych i mobilnych.
○ Używany do rysowania półprzezroczystych elementów w interfejsach użytkownika, cieniach,
nałożeniach kolorów i warstwach.


## Model HEX

### ● Struktura:
○ Składa się z sześciu cyfr szesnastkowych, które reprezentują wartości RGB.
○ Każda para cyfr szesnastkowych reprezentuje jeden z kolorów: czerwony, zielony, niebieski.
○ Przykład: #FF0000 to czysty czerwony, #00FF00 to czysty zielony, #0000FF to czysty
niebieski.
○ Alternatywnie można zapisać w formie skróconej: #FFF zamiast #FFFFFF (biały).
### ● Jak działa:
○ Każda z wartości od 00 do FF (0-255 w systemie dziesiętnym) określa intensywność danej
składowej koloru.
○ Jest często używany w językach takich jak HTML i CSS do określania kolorów na stronach
internetowych.
### ● Zastosowanie:
○ Bardzo popularny w projektowaniu stron internetowych, ponieważ jest kompaktowy i łatwy
do użycia w kodzie.
○ Umożliwia precyzyjne definiowanie kolorów za pomocą jednego ciągu znaków, co jest idealne
do stylizowania elementów w CSS.

