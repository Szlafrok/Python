# Zadanie 1 (++)
print("Wpisz liczbe ułamkową")
a = float(input())
print("Wpisz liczbe ułamkową")
b = float(input())
print("Wpisz liczbe ułamkową")
c = float(input())
if a >= b and a >= c:
    print(f"Liczba a jest największa spośród podanych")
if b >= a and b >= c:
    print(f"Liczba b jest największa spośród podanych")
if c >= a and c >= b:
    print(f"Liczba c jest największa spośród podanych")

# - Może być kilka zmiennych o najwyższej wartości, dlatego >= zamiast >
# - Z tego samego powodu zastosowałbym tu 3 if-y, zamiast konstrukcji if-elif-elif.
# Jeżeli a = b = c, to wszystkie trzy będą największe.
# - Jeżeli chcemy trzymać się litery zadania co do joty, trzeba wskazać konkretnie zmienne,
# które mają największą wartość, a nie ich same wartości.
# Jeżeli natomiast chciałbyś podać tylko jedną z nich, to ostatni elif jest zbędny:
# możesz zastąpić go else-m. Jeżeli a nie jest największe i b nie jest największe,
# to c na pewno jest największe. Nie musisz już sprawdzać tego przypadku ;)


#Zadanie 2 (+++)
p = 123
q = 456
a = (p > q or p < q) # ok
b = not(p < q or p == q) # ok
c = not(not(p == q)) # ok
d = not(p < q) # ok
e = (not(p < q) and p <= q or not(p > q) and p >= q) # błędne
# W podpunkcie e miałeś wykorzystać tylko operatory >= oraz <=.
# Logicznie natomiast się to sprowadza do (p == q) ;)

# +5 plusów, czyli wpada odznaka :D