from random import randint

wylosowana = randint(1, 100000) # W randint() i lewa i prawa granica zakresu również są brane pod uwagę! (było od 1 do 100001)

próby = 0 # uważaj na polskie znaki w nazwach zmiennych!

while True:
    try:
        wybrana = int(input("Wprowadź liczbę od 1 do 100,000: "))
        
        if wybrana < 1 or wybrana > 100000:
            print("Liczba musi znajdować się w zakresie od 1 do 100,000")
            continue # Fajne! + 0.25p
        próby += 1
        if wybrana > wylosowana:
            print("Za dużo")
        elif wybrana < wylosowana:
            print("Za mało")
        else:
            print("Zgadłeś!")
            print(f"Liczba prób {próby}")
            break
    except ValueError:
        print("Zły typ danych, spróbuj ponownie")

# Rozwiązane bardzo ładnie i z eleganckimi zabezpieczeniami ;)

# Pytanie dodatkowe

# Najszybszym sposobem na znalezienie liczby jest:
# 1. Znajdź liczbę pomiędzy dwoma w zakresie
# 2. Gdy liczba okaże się za duża lub za mała eliminuje się drugą połowę liczb
# 3. Koniec! To takie proste 

# Tak, o to chodzi, ale zapomniałeś dopisać, że powtarzamy ten algorytm dla zarkesu,
# którego nie wyelminiowaliśmy :P
# Niemniej jednak gratuluję, to było trudne pytanie!


# 4 za zadanie + 0.25 bonus + 0.75 / 1 za odpowiedź na pytanie = 5 / 4 :D