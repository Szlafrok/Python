def ambrozy(pierogi: list): # definiujemy funkcję ambrozy
    sumy = [] # tworzymy pustą listę na sumy cyfr każdego pieroga
    for pierog in pierogi: # iterujemy po każdym pierogu z listy
        suma = 0
        for numer in str(pierog): # sumujemy cyfry pieroga i dodajemy je do listy
            suma += int(numer)
        sumy.append(suma)
    sumy_copy = sumy.copy() # kopiujemy listę
    sumy.sort() # sortujemy listę
    if sumy[0] == sumy[1]: # sprawdzamy czy błędna suma pieroga jest na końcu listy
        niepoprawna_suma = sumy[len(sumy) - 1] # znajdujemy błędną sumę
    else: # jeżeli nie jest na końcu to musi być na początku
        niepoprawna_suma = sumy[0] # i znowu lokalizujemy niepoprawną sumę
    
    niepoprawny_pierog = sumy_copy.index(niepoprawna_suma) # sprawdzamy index pieroga w kopi listy sumy
    return pierogi[niepoprawny_pierog] # zwracamy nie poprawnego pieroga

pierogi = [15, 6, 24, 34, 42, 60] # testujemy nasz program
print(f"Niepoprawny pieróg to pieróg z numerem:{ambrozy(pierogi)}")


# Nie błędy, ale uwagi:
# - nie zaszkodzi dodać type hintingu zwracanej wartości
# - dobrze korzystasz z założeń - wiesz, że błędna suma jest tylko jedna
# - zamiast odwoływać się do sumy[len(sumy) - 1] możesz się odnieść do sumy[-1] ;)


# Bardzo ładnie! +0.25 za komentarze!

# (+2.25 / 2.00)