PIN = 1885
HASLO = "BERLIN"
pin = input("Podaj swój numer pin:")
haslo = input("Podaj swoje hasło:")
if haslo == HASLO and pin == PIN:
    print("Dostęp przyznany")
else:
    print("too bad")

# Porównując stringa do inta nigdy nie uzyskasz prawdy. W stałej PIN masz inta, a w zmiennej pin input wrzuci Ci stringa.
# Poza tym wg zadania miałeś spytać najpierw o pin i w razie poprawności dopiero wtedy o hasło. Zgaduję, że to po prostu błąd nieuwagi, a na to trzeba uważać :P

# Poza tym w porządku :]

# 1.75 / 3.00