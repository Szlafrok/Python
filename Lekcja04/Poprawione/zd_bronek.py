# Zadanie 1 (++)

a = float(input("Podaj wartość zmiennej a (liczba zmiennoprzecinkowa): "))
b = float(input("Podaj wartość zmiennej b (liczba zmiennoprzecinkowa): "))
c = float(input("Podaj wartość zmiennej c (liczba zmiennoprzecinkowa): "))


Najwieksze_jest_a = a >= b and a >= c
Najwieksze_jest_B = b >= a and b >= c
Najwieksze_jest_C = c >= a and c >= b # Dodaję >= zamiast >: Jeżeli największą wartość ma kilka zmiennych, to one wszystkie są największe


print(f"Czy wartość zmiennej a ({a}) jest największa? {'Tak' if Najwieksze_jest_a else 'Nie'}")
print(f"Czy wartość zmiennej b ({b}) jest największa? {'Tak' if Najwieksze_jest_B else 'Nie'}")
print(f"Czy wartość zmiennej c ({c}) jest największa? {'Tak' if Najwieksze_jest_C else 'Nie'}") # Niedomknięty nawias, nazwa zmiennej miała "6" na końcu


# Bronek, zdarzają Ci się błędy nieuwagi, a na to trzeba bardzo uważać. Gubisz się w konwencji:
# zmienna sprawdzająca "a" kończy się małą literą, pozostałe zmienne sprawdzające kończą się na wielką literę.
# Tu nie domkniesz nawiasu, tam wkradnie Ci się jakiś błąd i tak pojawiają się problemy w kodzie, a można ich łatwo uniknąć.

# Poza tym zadanie wykonane bardzo ładnie



#zad *
p, q = True, True

a = (p > q or p < q)  # p jest różne od q jeśli jest większe lub mniejsze / OK
b = not (p < q or p == q)  # p jest większe od q jeśli nie jest mniejsze ani równeC:\Users\Bronuś Gosz\Desktop\Lekcje Programowania\Untitled-1.py
c = (not (p < q or p > q))  # p jest równe q jeśli nie jest ani mniejsze ani większe
c = (not (p < q or p > q))  # p jest równe q jeśli nie jest ani mniejsze ani większe
d = not (p < q)  # p jest większe lub równe q jeśli nie jest mniejsze
e = not (p > q or p < q)  # p jest równe q, jeśli nie jest ani większe, ani mniejsze
    #Mam nadzieje ze jest dobrze  Lubie kremowki i wiedzmina pozdrawiam : )

# Również lubię :)
# Miałeś tutaj zrobione dziwne wcięcie przed tym zadaniem (było przesunięte w prawo). To co mówiłem
# w zadaniu wyżej - błąd nieuwagi.
# Nwm czemu w komentarzu do podpunktu B wkleiłeś ścieżkę pliku.
# Podobnie, podpunkt 3 jest powielony dwukrotnie.

# Jeżeli chodzi o poprawność podpunktów:
# W podpunkcie (e) logika się zgadza, ale miałeś użyć >= oraz <=. Tak było w treści zadania!


# Poza tym zadanie jest zrealizowane bardzo dobrze :)

# (+++), więc za lekcję 4 będzie odznaka ;D