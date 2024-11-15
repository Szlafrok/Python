def pierwszość(n): #definiowanie funkcji przyjmowanie zmiennej podanej potem jako n 
    if n < 3:      #3 jest najwięksą w pierwszym rzędie liczbą pierwszą (wie pan o co mi chodzi) // Liczba 2 również jest liczbą pierwszą
        return False #jeśli jest to program mówie NIE
    for i in range(2, int(n**0.5) + 1):  #kąkretne sprawdzanie piewszości, który musi być po dwa i przed pierwiastkiem kwadratowym danej liczby bądź nim być (ponieważ jakaś zasada)
        if n % i == 0: #jeśli jest złożona 
            return False # to wyżuca false
    return True #jak nie to True

def całosc(): #definiowanie całości
    try: #próba XD
        x = int(input("Wprowadź liczbę naturalną: ")) #definiowanie x
        if x < 0: #jeśli x mniejszy od 0 to nie jest liczbą pierwszą 
            print("NATURALNĄ!!!")
            return 

        if pierwszość(x):#jeśli pierwszość jest prawdziwa dla x
            print(f"{x} to liczba pierwsza.")
        elif x == 1: # jeśli x to 1 
            print("1 to 1 https://i.kym-cdn.com/entries/icons/facebook/000/032/244/cover.jpg") # XD
        else: # jesli ani to ani to
            print(f"{x} jest liczbą złożoną.")
    except ValueError: # w wybatku jakiegoś błedu dla pewności można to wpisać
        print("Co ty wpisałeś? wpisz normalną liczbę.")

if __name__ == "__main__": #jeśli plik zostanie włącony to ma wlączyć funkcję "całosc"
    całosc()

# Zaczytanie danych: 0.5 / 0.5
# Rozpatrzenie warunków szczególnych: 0.75 / 1.5 - 0 nie jest liczbą ani pierwszą, ani złożoną, podobnie jak 1. 2 jest liczbą pierwszą, dzieli się przez 1 i przez samą siebie!
# Weryfikacja pozostałych dzielników: 3.0 / 3.0 - tutaj nie mam zastrzeżeń :)

# (4.25 / 5.00) Zadanie rozwiązane ładnie, napisane pod wygodę użytkownika. Dobrze zdefiniowane funkcje i dobrze użyte, podobnie jak pętla "for".

# zadanie B
# ponieważ 4 , 6 itd dzielą się przez 2
# zadanie c obyło się bez sqrt

# Z zadań dodatkowych:
# - Ad A: Komentarze OK, tylko zwróć uwagę na literówki, typu "kąkretne", "w wybatku", "jeśli jest to program mówie NIE". Oczywiście to nie język polski, więc ciąć nie będę XD (+1 pkt / 1)
# - Ad B: Dałem komuś 1/2 za ten podpunkt, bo uzasadnił odpowiedź na bazie 1 przykładu. Co prawda wskazałeś dwa, nie powiedziałeś, że chodzi ogólnie o parzyste, ale mając 4 i 6 można sobie dopowiedzieć, że dalej są 8, 10, 12..., więc niech będzie. Ale chodziło mi o to, żeby wskazać konkretnie na liczby parzyste :P (+2 pkt / 2)
# - Ad C: Owszem, obyło się, zastosowałeś dobry zamiennik. Ale dokładnie o to mi chodziło, tak czy inaczej :D (+1 pkt / 1)

# Za zadania dodatkowe komplet, czyli 4 pkt na 4 możliwe. Gratki ;)