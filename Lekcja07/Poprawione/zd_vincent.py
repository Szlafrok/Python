from math import sqrt # pobranie funkcji sqrt z modułu math

while True: # ta pętla kończy się dopiero gdy użytkownik wprowadzi poprawne dane
    try:
        liczba = int(input("Wprowadź liczbę naturalną: ")) # dzięki tej funkcji możemy uzyskać informacje od użytkownika 
        if liczba > 0: break # jeżeli wprowadzimy poprawne dane przerwiemy pętle
    except ValueError: # gdy wystapi error zamiast błędu wyrzuci wiadomość poniżej
        print("Zła wartość, wprowadź liczbę naturalną") 

wynik = 0

if liczba > 1:  # ten if sprawdza czy liczba która wprowadziliśmy jest większa niż jeden
    for dzielnik in range(2, int(sqrt(liczba)) + 1): # ta pętla sprawdza każdy dzielnik tej liczby
        if dzielnik != liczba:
            if liczba % dzielnik == 0.0:
                wynik += 1
        else:
            continue
    if wynik > 0: # ten if sprawdza czy liczba ma inne dzielniki (nelicząc samej siebie i jeden) na podstawie poprzedniej pętli for 
        print("Ta liczba jest złożona")
    else:
        print("Ta liczba jest pierwsza")
else: 
    print("Ta liczba nie jest ani złożona ani pierwsza") # jeżeli liczba okaże się niebyć większa od jeden program wyprintuje to zdanie
exit() # to polecenie zamyka program

