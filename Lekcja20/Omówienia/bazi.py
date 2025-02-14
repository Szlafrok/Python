imie_1 = "Jan"
nazwisko_1 = "Kowalski"
wiek_1 = 16

imie_2 = "Włodek"
nazwisko_2 = "Bialutki"
wiek_2 = 18

imie_3 = "Listonosz"
nazwisko_3 = "Pat"
wiek_3 = 40

imie_4 = "Gwiazda"
nazwisko_4 = "Śmierci"
wiek_4 = 2

#print("Jan = tak , Włodek = tak , Listonosz = tak , Gwiazda = nie") # hardcode
print()
if wiek_1 >= 18:
    print(f"{imie_1} {nazwisko_1} jest pełnoletni")
else:
    print(f"{imie_1} {nazwisko_1} nie jest pełnoletni")

if wiek_2 >= 18:
    print(f"{imie_2} {nazwisko_2} jest pełnoletni")
else:
    print(f"{imie_2} {nazwisko_2} nie jest pełnoletni")

if wiek_3 >= 18:
    print(f"{imie_3} {nazwisko_3} jest pełnoletni")
else:
    print(f"{imie_3} {nazwisko_3} nie jest pełnoletni")

if wiek_4 >= 18:
    print(f"{imie_4} {nazwisko_4} jest pełnoletni")
else:
    print(f"{imie_4} {nazwisko_4} nie jest pełnoletni")
print()