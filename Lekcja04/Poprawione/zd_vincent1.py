a = float(input("Wprowadź 1 liczbę: "))
b = float(input("Wprowadź 2 liczbę: "))
c = float(input("Wprowadź 3 liczbę: "))

if a == b == c:
    print("Wszystkie liczby są równe.")
else:
    if a == b and c < a:
        print("1 i 2 liczba są największe.")
    elif a == c and b < a:
        print("1 i 3 liczba są największe.")
    elif b == c and a < b:
        print("2 i 3 liczba są największe.")
    else:
        if a > b and a > c:
            print("1 liczba jest największa.")
        elif b > a and b > c:
            print("2 liczba jest największa.")
        elif c > a and c > b:
            print("3 liczba jest największa.")
        else: 
            print("Wprowadź liczby ponownie.")

# (+++)

# Bardzo rozbudowane sprawdzenie. W sumie fajnie, że jak już robiłeś tą
# metodą, to zrobiłeś widoczny podział, dzięki temu kod jest czytelny.

# Dało się to zrobić dużo prościej, ale byłoby to kosztem tak jasnej informacji
# ze strony kodu - czyli ładnego opisania, które zmienne mają największą wartość.
# Nie przyczepię się, ale na przyszłość zalecałbym jednak upraszczanie kodu ;)