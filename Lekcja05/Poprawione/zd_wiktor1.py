# Pobieramy numer miesiąca od użytkownika
miesiac = input("Podaj numer miesiąca (1-12): ")

# Sprawdzamy, czy użytkownik podał prawidłowy numer miesiąca
if not miesiac.isdigit() or int(miesiac) < 1 or int(miesiac) > 12:
    print("Błędny numer miesiąca! Podaj liczbę od 1 do 12.")
else:
    miesiac = int(miesiac)
    if miesiac in [1, 2]:
        koszt = 150
    elif miesiac in [3, 4]:
        koszt = 199
    elif miesiac in [5, 6]:
        koszt = 249
    elif miesiac in [7, 8, 9]:
        koszt = 299
    elif miesiac == 10:
        koszt = 249
    else:  # miesiące 11 i 12
        koszt = 199

    print(f"Koszt atrakcji turystycznej wynosi: ${koszt}")

# Bardzo ładnie! Dodam tylko, że mogłeś uprościć podawanie ceny, np. dla października jest taka sama, jak dla maja i czerwca.
# 3/3