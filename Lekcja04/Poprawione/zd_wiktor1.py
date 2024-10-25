#zadanie 1

# Pobranie liczb od użytkownika
a = float(input("Podaj wartość dla a: "))
b = float(input("Podaj wartość dla b: "))
c = float(input("Podaj wartość dla c: "))

# Sprawdzanie, która liczba jest największa
if a >= b and a >= c:
    print("a jest największe spośród podanych.")
else:
    print("a nie jest największe spośród podanych.")

if b > a and b > c:
    print("b jest największe spośród podanych.")
else:
    print("b nie jest największe spośród podanych.")

if c > a and c > b:
    print("c jest największe spośród podanych.")
else:
    print("c nie jest największe spośród podanych.")

# Jeżeli kilka wartości jest największych sobie i równych sobie, wszystkie
# są największe. Dlatego dodaję znaki >= zamiast >.

# Poza tym zadanie zrobione bezbłędnie i ekstra plus za komentarze!

# (+++), bonus (+)