def skaner_hasla():
    try:
        haslo = input("Wprowadź hasło: ")
        if not any(znak.isupper() for znak in haslo):
            raise Exception("Error: Brak dużej litery!")
        elif not any(znak.islower() for znak in haslo):
            raise Exception("Error: Brak małej litery!")
        elif not any(znak.isdigit() for znak in haslo):
            raise Exception("Error: Brak cyfry!")
        elif not any(not znak.isalnum() for znak in haslo):
            raise Exception("Error: Brak znaku specjalnego!")
        elif 12 > len(haslo):
            raise Exception("Error: Za mało znaków (min. 12)!")
        
    except Exception as e:
        print(e)
    
    else:
        print("Twoje hasło jest bardzo mocne.")
    
    finally:
        print("Weryfikacja hasła zakończona. ")

skaner_hasla()

# Zadanie i dodatek są bardzo zgrabnie i czytelnie zrobione, super ;) (4/4) (+1) (+0.5 za trik z any()!)
# Użyłeś tutaj ciekawej funkcji - any(). Użyłeś jej znakomicie, jest to również coś, czego nie poruszaliśmy na
# naszych zajęciach. Podobnie jak z zadaniem 2 z lekcji 33, chciałbym z Tobą ją krótko omówić. Przy okazji, czy znasz może
# funkcję all(), która jest poniekąd siostrzaną funkcją any()?