dzielniki = []

while True:
    try:
        liczba = int(input("Wprowadź liczbę naturalną: "))
        if liczba > 1:  # liczba musi być większa od 1, ponieważ liczby doskonałe są zdefiniowane tylko dla liczb większych od 1
            break
        else:
            print("Liczba musi być większa od 1, spróbuj ponownie")
    except ValueError:
        print("Zły typ danych, spróbuj ponownie")
        
for i in range(1, liczba): # Ciekawostka - jest szybsze rozwiązanie. Pokażę Ci w funkcji poniżej:
    if liczba % i == 0:
        dzielniki.append(i)
    
if sum(dzielniki) == liczba:
    print("Ta liczba jest doskonała")
else:
    print("Ta liczba nie jest doskonała")

from math import sqrt

def usprawnienie(liczba):
    s = sqrt(liczba)
    for i in range(1, s+1):
        if liczba % i == 0:
            dzielniki.append(i)
            dzielniki.append(liczba//i) # Nie musimy trzymać kolejności w liście, skoro i tak jest nam potrzebna tylko do sumy

# Bardzo ładnie :) +3 / 3

# ------- PODSUMOWANIE -------

# Zadania 1-6 liczę możliwie najbardziej na korzyść dla Was

# ZAD 1: 4.5  / 4       Obowiązkowe A
# ZAD 2: 5    / 4       Obowiązkowe B
# ZAD 3: 3.25 / 4       Zad dod - 8
# ZAD 4: 4    / 4       Obowiązkowe C
# ZAD 5: 4    / 4       Obowiązkowe D
# ZAD 6: 3.75 / 4       Zad dod - 7

# Dodatkowe:

# ZAD 7:  +2.5 / 2.5
# ZAD 8:  +1.5 / 1.5
# ZAD 9:  +2   / 2
# ZAD 10: +3   / 3

# Razem:
#   Obowiązkowe: 17.5 / 16.0
#   Dodatkowe:   +9 pkt

# Gratulacje :D