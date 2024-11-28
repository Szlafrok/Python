import random

# Losowanie liczby
tajemnicza_liczba = random.randint(1, 100000)
liczba_prob = 0

while True:
    odpowiedz_uzytkownika = int(input("Zgadnij liczbę: "))
    liczba_prob += 1
    if odpowiedz_uzytkownika < tajemnicza_liczba:
        print("Za mała!")
    elif odpowiedz_uzytkownika > tajemnicza_liczba:
        print("Za duża!")
    else:
        print(f"Brawo! Zgadłeś w {liczba_prob} próbach.")
        break

# Bezbłędnie!