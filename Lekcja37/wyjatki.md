1. ZeroDivisionError
- Zgłaszany, gdy następuje dzielenie przez zero.
2. OverflowError
- Zgłaszany, gdy obliczenie przekracza zakres liczby reprezentowanej
w pamięci.
3. FloatingPointError
- Zgłaszany w przypadku błędów w operacjach na liczbach
zmiennoprzecinkowych.
4. AssertionError
- Zgłaszany, gdy instrukcja assert zwróci fałsz.
5. AttributeError
- Zgłaszany, gdy przypisanie lub odczyt atrybutu jest nieprawidłowy.
6. EOFError
- Zgłaszany, gdy funkcja wejściowa natrafia na koniec pliku (EOF) bez
uprzedniego pobrania danych.
7. ImportError
- Zgłaszany, gdy nie udaje się zaimportować modułu.
ModuleNotFoundError jest jego podklasą w Pythonie 3.6+.
8. IndexError
- Zgłaszany, gdy indeks sekwencji jest poza zakresem.
9. KeyError
- Zgłaszany, gdy klucz słownika jest nieobecny.
10. KeyboardInterrupt
- Zgłaszany, gdy użytkownik przerwie wykonywanie programu za
pomocą klawiatury (np. Ctrl+C).
11. MemoryError
- Zgłaszany, gdy nie można przydzielić pamięci.
12. NameError
- Zgłaszany, gdy zmienna lub nazwa nie jest zdefiniowana.
13. OSError
- Bazowa klasa dla wyjątków związanych z systemem operacyjnym,
takich jak FileNotFoundError, PermissionError, i
TimeoutError.
14. FileNotFoundError
- Zgłaszany, gdy operacja otwarcia pliku nie powiedzie się, ponieważ
plik nie istnieje.
15. PermissionError
- Zgłaszany, gdy brak jest odpowiednich uprawnień do wykonania
operacji.
16. TimeoutError
- Zgłaszany, gdy czas wykonywania operacji przekracza czas
oczekiwania.
17. TypeError
- Zgłaszany, gdy operacja lub funkcja jest stosowana do obiektu
niewłaściwego typu.
18. ValueError
- Zgłaszany, gdy funkcja otrzymuje argument o niewłaściwej wartości,
nawet jeśli typ jest poprawny.
19. RuntimeError
- Bazowa klasa dla wyjątków, które nie pasują do żadnej innej
kategorii.
20. SyntaxError
- Zgłaszany, gdy parser napotyka błąd składniowy.
21. IndentationError
- Zgłaszany, gdy napotkany zostanie błąd w poziomie wcięcia. Jest
podklasą SyntaxError.
22. TabError
- Zgłaszany, gdy wcięcia zawierają mieszankę tabulatorów i spacji.
Jest podklasą IndentationError.