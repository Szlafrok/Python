val = 5
val *= 5
val += 5
val -= 3

#print(val)
print(val + 1)


taka_fajna_zmienna = 1 # snake case
takaFajnaZmienna = 1 # camel case
TakaFajnaZmienna = 1 # pascal case

str() # tekst
int() # liczba całkowita
bool() # wartość true / false
float() # liczba dziesięta / zmiennoprzecinkowa


x = input() # podstawia wpisane dane do zmiennej x JAKO STRING
s = type(x) # podaje typ danych tego, co wprowadzimy do tej funkcji
print(s)

# ZADANIE 1:

# Proszę podstawić do zmiennej x treść wypisaną w konsoli przez użytkownika.
# Proszę sprawić, że wpisane informacje będą typu LICZBY CAŁKOWITEJ (int)
# Proszę następnie podać za pomocą funkcji print() TYP DANYCH w zmiennej x.

# (b) Proszę dodać 5 do podanej zmiennej x
# (c)* Proszę podnieść x do potęgi 2.

# ROZWIĄZANIE
x = int(input("Podaj liczbę")) # pierwszy sposób, robi 2 pierwsze podpunkty

x = input("Podaj liczbę") # pierwszy podpunkt
x = int(x) # drugi sposób, drugi podpunkt

t = type(x)
print(t)

#podpunkt (b)
x += 5
# x = x + 5

#podpunkt (c)*
#x **= 2
#x = x * x
#x *= x
x = x**2

# PO PRZERWIE ----------------------------------------------------
# idziemy do pliku "po_przerwie.py"