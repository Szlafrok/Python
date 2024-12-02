n = int(input("Podaj liczbę: "))

i = 1
suma = 0

while(i < n):
    if n % i == 0:
        print(f"dzielnik {i} - obecna suma = {suma} + {i} = {suma+i}")
        suma += i
    i += 1

if suma == n:
    print("Liczba jest doskonała")
else:
    print("Liczba nie jest doskonała")