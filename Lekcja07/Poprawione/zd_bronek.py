#Importujemy funkcję sqrt() z biblioteki math, aby móc obliczyć pierwiastek z liczby
from math import sqrt

#Wczytujemy liczbę od użytkownika i przekształcamy ją na typ całkowity (int)
liczba = int(input("Podaj liczbę naturalną: "))

#Sprawdzamy, czy liczba jest mniejsza niż 2, ponieważ tylko liczby większe od 1 mogą być pierwsze lub złożone
if liczba < 2:
    print("Liczba nie jest ani liczbą pierwszą, ani liczbą złożoną.")
    exit()  # Kończymy program

#Zakładamy, że liczba jest pierwsza i będziemy to sprawdzać
czy_pierwsza = True

#Sprawdzamy podzielność liczby przez dzielniki od 2 do pierwiastka z liczby.
#Optymalizacja: nie musimy sprawdzać wszystkich dzielników do liczby-1.
#Wystarczy sprawdzić dzielniki do pierwiastka z liczby, ponieważ jeżeli liczba ma dzielnik większy od pierwiastka,
#to mniejszy dzielnik również musi istnieć i będzie mniejszy lub równy pierwiastkowi z liczby.
for i in range(2, int(sqrt(liczba)) + 1):
    if liczba % i == 0:
        czy_pierwsza = False  # Jeśli liczba jest podzielna przez i, to nie jest liczbą pierwszą
        break  # Możemy zakończyć sprawdzanie, ponieważ wiemy już, że liczba nie jest pierwsza

#Wyświetlamy odpowiedni wynik na podstawie wartości zmiennej czy_pierwsza
if czy_pierwsza:
    print("Liczba jest liczbą pierwszą.")
else:
    print("Liczba jest liczbą złożoną.")

#Kończymy działanie programu
exit()

# Zaczytanie liczby, sprawdzenie przypadków szczególnych i 
# Zadanie rozwiązane BEZBŁĘDNIE! Brawo ;) (5.0 / 5.0)

# Z dodatkowych:
# Komentarze: +1 pkt
# Uzasadnienie z pierwiastkiem OK: +1 pkt
