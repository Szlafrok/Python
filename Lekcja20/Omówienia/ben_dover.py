imie_1 = "jan"
nazwisko_1 = "adolf"
wiek_1 = 18

imie_2 = "gerald"
nazwisko_2 = "kremówka"
wiek_2 = 20

imie_3 = "kebab"
nazwisko_3 = "lubie"
wiek_3 = 18

imie_4 = "włodzimierz"
nazwisko_4 = "biały"
wiek_4 = 50

print("wybierz konto. posiadasz 4 konta")
x = int(input("Proszę wprowadzić tu liczbę: "))

#print(x, type(x))

if x == 1:
    if wiek_1 >= 18:
        print(f"{imie_1} {nazwisko_1} jest pełnoletni.")
    else:
        print(f"{imie_1} {nazwisko_1} nie jest pełnoletni.")
elif x == 2:
    if wiek_2 >= 18:
        print(f"{imie_2} {nazwisko_2} jest pełnoletni.")
    else:
        print(f"{imie_2} {nazwisko_2} nie jest pełnoletni.")
elif x == 3:
    if wiek_3 >= 18:
        print(f"{imie_3} {nazwisko_3} jest pełnoletni.")
    else:
        print(f"{imie_3} {nazwisko_3} nie jest pełnoletni.")
else:
    if wiek_4 >= 18:
        print(f"{imie_4} {nazwisko_4} jest pełnoletni.")
    else:
        print(f"{imie_4} {nazwisko_4} nie jest pełnoletni.")