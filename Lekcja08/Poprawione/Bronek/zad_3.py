n = int(input("Podaj, ile liczb Fibonacciego wypisać: "))

a, b = 0, 1  # Pierwsze dwie liczby Fibonacciego
for _ in range(n):
    print(a, end=" ")  # Wypisujemy aktualną liczbę
    a, b = b, a + b  # Obliczamy następną liczbę