# ZADANIE 1

imie = input("Podaj imię\n") # Wstawka "\n" sprawia, że przejdziemy do kolejnej linijki i będzie to ładniejsze
nazwisko = input("Podaj nazwisko\n")
rok_urodzenia = int(input("Podaj rok urodzenia\n")) # Muszę zamienić na int, ponieważ to będzie liczba. Dzięki temu mogę ją odejmować od innych liczb.

print(f"{imie} {nazwisko} ma {2024 - rok_urodzenia} lat.") #Pamiętamy o "f" przed cudzysłowiem!


# ZADANIE 2

dzielna = int(input("Podaj dzielną\n")) # Pobieram liczbę całkowitą od użytkownika
dzielnik = int(input("Podaj dzielnik\n"))

print(f"Wynik z dzielenia {dzielna} przez {dzielnik} to {dzielna // dzielnik} i {dzielna % dzielnik} reszty.")
# Mogłem to zrobić równie dobrze podstawiąc działania do zmiennych, ale tak jest ładniej i zgrabniej :)