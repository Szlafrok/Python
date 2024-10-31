znak = input("podaj znak działania")
 

if not(znak == "-" or znak == "+" or znak == "*" or znak == "/" or znak == "//" or znak == "%"):
    print("coś ci się pomyliło")
else:
    a = float(input("podaj liczbę a"))
    b = float(input("podaj liczbę b"))

    if b == 0 and znak in ('%', '//', '/'): # Brakowało mi tej weryfikacji. Zrobiłem to w krotkach ;)
        print("Nie wolno dzielić przez 0!")
        exit()

    if znak == "-":
        print(a - b)
    elif znak == "+":
        print(a + b)
    elif znak == "*":
        print(a * b)
    elif znak == "%": # miało być modulo, nie potęgownaie
        print(a % b)
    elif znak == "/":
        print(a / b)
    else:
        print(a // b)

    # 2 / 3


# Razem 5/6

 
