def ocena_liczby(liczba):
    if liczba > 0 :
        return "liczba jest dodatnia "
    elif liczba < 0:
        return "liczba jest ujemna"
    return "Liczba jest zerem"

liczba = float(input("podaj liczbe "))
wynik=ocena_liczby(liczba)
print(wynik)