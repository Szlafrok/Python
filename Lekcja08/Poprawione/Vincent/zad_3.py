while True:
    try:
        ilosc_elementow = int(input("Wprowadź ilość elementów z ciągu Fibonacciego: "))
        if ilosc_elementow > 0:
            break
        else:
            print("Ilosc elementów musi byc większa od 0")
    except ValueError:
        print("Zły typ danych, spróbuj ponownie")

fib = [0, 1]

for i in range(2, ilosc_elementow): # Usunąłem +1, dostawaliśmy o 1 element ciągu zbyt wiele :P Ale podejście bardzo ładne!
    fib.append(fib[-1] + fib[-2])

for j in fib:
    if j == fib[-1]: # UWAGA! Notatka na dole
        print(j)
    else:
        print(j, end=", ")


# Twój warunek nie rozpatruje przypadku szczególnego! Dla ilości elementów == 3: 

#   fib = [0, 1, 1]

# Kiedy porównujesz fib[1] z fib[-1] (czyli fib[1] z fib[2]), warunek aktywuje się przedwcześnie!
# Jest to jedyny przypadek, gdzie dwa sąsiadujące elementy tego ciągu są sobie równe.

# Pomysł w gruncie rzeczy dobry, ale zawiera drobne błędy :P


# Odczyt liczby i badanie poprawności: 1 / 1
# Poprawne wyznaczenie elementów ciągu: 1.5 / 1.5
# Poprawna liczba powtórzeń: 0.75 / 1.5

# -> 3.25 / 4