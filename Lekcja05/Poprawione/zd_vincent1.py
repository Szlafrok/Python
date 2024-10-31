numer_miesiąca = int(input("Wprowadź numer miesiąca: "))

if numer_miesiąca in [1, 2]:
    print("Koszt atrakcji w tym miesiącu wynosi $150.")
elif numer_miesiąca in [3, 4, 11, 12]:
    print("Koszt atrakcji w tym miesiącu wynosi $199.")
elif numer_miesiąca in [5, 6, 10]:
    print("Koszt atrakcji w tym miesiącu wynosi $249.")
elif numer_miesiąca in [7, 8, 9]:
    print("Koszt atrakcji w tym miesiącu wynosi $299.")
else:
    print("Nieprawidłowy numer miesiąca, wprowadź numer miesiąca od 1 do 12.")

# Bezbłędnie :>
# 3 / 3 plusów