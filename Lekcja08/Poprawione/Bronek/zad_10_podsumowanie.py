n = int(input("Podaj liczbę naturalną: "))

# (mniejszych od n) # ????
suma_dzielnikow = sum(i for i in range(1, n) if n % i == 0)

if suma_dzielnikow == n:
    print(f"{n} jest liczbą doskonałą.")
else:
    print(f"{n} nie jest liczbą doskonałą.")

# Bezbłędnie! + 3 pkt

# ---------------- PODSUMOWANIE ----------------

# Zadanie 1: 3.75 pkt
# Zadanie 2: 4 pkt - liczę do obowiązkowych
# Zadanie 3: 4 pkt - liczę do obowiązkowych
# Zadanie 4: 3.25 pkt
# Zadanie 5: 4 pkt - liczę do obowiązkowych
# Zadanie 6: 4 pkt - liczę do obowiązkowych

# Dodatkowe: -----------

# Zadanie 7: Rozwiązane zadanie 1: +2.5p / 2.5
# Zadanie 8: Rozwiązane zadanie 4: +1.5p / 1.5
# Zadanie 9: Bardzo ładne uzasadnienie :) +2 pkt
# Zadanie 10: Bardzo dobrze :D +3 pkt

# RAZEM:

# Obowiązkowe: 16 / 16
# Dodatkowe: + 8.5 pkt