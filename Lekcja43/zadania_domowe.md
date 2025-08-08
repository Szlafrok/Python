## Zadanie 1. Pogodynka - walutówka (5 pkt)
Proszę uzupełnić skrypt z lekcji 43 (plik projekt.py) o funkcje:
- Nr 3: Sprawdzenie lokalizacji miejsca startowego. Opcja powinna podać nam współrzędne geograficzne, nazwę i państwo miasta startowego. Funkcja powinna wypisać odpowiedni komunikat do zmiennej `comm` jeśli miasto startowe nie zostało podane.
- Nr 4: Sprawdzenie lokalizacji miejsca docelowego. Opcja powinna podać nam współrzędne geograficzne, nazwę i państwo miasta docelowego. Funkcja powinna wypisać odpowiedni komunikat do zmiennej `comm` jeśli miasto docelowe nie zostało podane.
- Nr 5: Sprawdzenie informacji o pogodzie w miejscu startowym. Opcja powinna podać nam informację o pogodzie (krótką), temperaturę odczuwalną (w st. C), ciśnienie (w hPa) oraz procentową wilgotność. Funkcja powinna wypisać odpowiedni komunikat do zmiennej `comm` jeśli miasto startowe nie zostało podane.
- Nr 6: Sprawdzenie informacji o pogodzie w miejscu docelowym. Opcja powinna podać nam informację o pogodzie (krótką), temperaturę odczuwalną (w st. C), ciśnienie (w hPa) oraz procentową wilgotność. Funkcja powinna wypisać odpowiedni komunikat do zmiennej `comm` jeśli miasto docelowe nie zostało podane.
- Nr 7: Informacja o walutach i porównanie walut. Opcja powinna podać nam nazwy walut (np. dla złotego "PLN", dla dolara "USD", itd). Powinna też podać nam iloraz kursu waluty miasta startowego i docelowego (lub odwrotnie, ale należy podać co jest dzielnikiem, a co dzielną). Funkcja powinna wypisać odpowiedni komunikat do zmiennej `comm` jeśli któreś z miast nie zostało podane.

---
## Zadanie 2. No takie długawe wymyśliłem ale raczej fajne! (5 + 5 pkt)

a) (5 pkt) Korzystając z dokumentacji PokeAPI dostępnej pod tym [linkiem](https://pokeapi.co/docs/v2#pokemon) (zakładka Pokémon/Pokemon) oraz funkcji `pprint()` i wiedząc, że metody słowników `.keys()` oraz `.values()` pozwalają znacznie przyspieszyć przegląd dużych słowników, proszę znaleźć dane:
Dla każdego Pokemona należy znaleźć jego:

- Nazwę
- Wagę
- Wysokość
- Typ (np. dla Pikachu jest to żywioł `electric`)
- Umiejętność (wystarczy jedna)

Badamy Pokemony o ID odpowiednio: 25, 6, 94, 11, 54

b) [Dodatkowe] (+2 pkt) Proszę dokonać refaktoryzacji powyższego kodu tak, aby zapisywał dane na temat tych Pokemonów do słowników, tzn. dla każdego Pokemona należy stworzyć osobny słownik.

c) [Dodatkowe] (+3 pkt) Proszę dokonać refaktoryzacji powyższego kodu w taki sposób, żeby był on możliwie najbardziej czytelny. Sugeruję skorzystać z type hintingu, komentarzy oraz funkcji!

Powodzenia! 😎