
a = int(input("podaj numer miesiąca"))
if a > 0 and a < 13:
    if a == 1 or a == 2:
        print("to będzie 150$")
    elif a == 3 or a == 4:
        print("to będzie 199$")
    elif a == 5 or a == 6:
        print("to będzie 249$")
    elif a >= 7 and a <= 9:
        print("to będzie 299$")
    elif a == 10:
        print("to będzie 249$")
    else:
        print("to będzie 199$")
else:
    print("zły numer")

# OK! 3/3