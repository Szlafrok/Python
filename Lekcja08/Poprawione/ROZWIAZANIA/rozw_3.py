while True:
    n = float(input("Podaj liczbę: "))
    if n > 0 and n % 1 == 0:
        break
    print("Zła liczba! Podaj liczbę dodatnią!")

a = 0
b = 1

a, b = 0, 1

n = int(n)

for i in range(n):
    print(a, end = ' ')
    c = a + b
    a = b
    b = c