# Funkcja sprawdzająca, czy Leopold otrzyma świadectwo z paskiem
def ocena_na_swiadectwo():
    # Wczytujemy oceny z przedmiotów
    ocena_matematyka = float(input("Podaj ocenę z matematyki: "))
    ocena_polski = float(input("Podaj ocenę z języka polskiego: "))
    ocena_angielski = float(input("Podaj ocenę z języka angielskiego: "))
    ocena_geografia = float(input("Podaj ocenę z geografii: "))
    ocena_fizyka = float(input("Podaj ocenę z fizyki: "))
    
    # Wczytujemy ocenę z zachowania
    ocena_zachowanie = float(input("Podaj ocenę z zachowania (od 2 do 6): "))
    
    # Liczymy średnią ocen z przedmiotów
    srednia_ocen = (ocena_matematyka + ocena_polski + ocena_angielski + ocena_geografia + ocena_fizyka) / 5
    
    # Sprawdzamy, czy średnia ocen i zachowanie spełniają warunki na świadectwo z paskiem
    if srednia_ocen >= 4.75 and ocena_zachowanie >= 5:
        print(f"Gratulacje! Otrzymasz świadectwo z paskiem. Twoja średnia to {srednia_ocen:.2f}")
    else:
        print(f"Niestety, nie otrzymasz świadectwa z paskiem. Twoja średnia to {srednia_ocen:.2f}")

# Uruchamiamy funkcję
ocena_na_swiadectwo()


# Elegancko B) Ładnie zrobione floaty w fstringu oraz komentarze, super!

# 3.0 / 3.0