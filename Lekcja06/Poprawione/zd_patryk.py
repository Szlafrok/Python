PIN = 1545
HASLO = "M4K4R3NA_"

pi = int(input("Podaj PIN"))
ho = input("Podaj hasło")

if PIN == int(pi) and ho == HASLO: # Wg zadania trzeba było najpierw sprawdzić PIN i dopiero jeżeli się zgadza, pytać o hasło - błąd nieuwagi :P
    print("Gratuluje dostałeś się do systemu")
else: 
    print("Nie poprawne dane logowania.")

# 2.5 / 3.0


#Zadanie 2



 
# język polski, język angielski, geografię i fizykę matematykę

print("Witaj Leopodzie!!")

jp = int(input("Podaj swoją ocenę z języka polskiego."))

ja = int(input("Teraz z języka angielskiego."))

geo = int(input("Z geografii."))

fiz = int(input("Z fizyki."))

ma = int(input("I na koniec z matematyki."))

zach = int(input("Zachowanie jeszcze poproszę. ")) # Brakowało

tt = jp + ja + geo + fiz + ma 

tt /= 5

if  tt >= 4.75 and zach >= 5: # brakowało warunku z zachowaniem
    print("Gratuluje Leopodzie zdobyłeś świadectwo z paskiem.:)")
else:
    print("Niestety ale nie udało ci się zdobyć paska.:(")
print(f"Średnia: {tt}")

# Brakowało weryfikacji zachowania oraz podania średniej na koniec - zgaduję, że błąd nieuwagi. Poza tym spoko ;)

# 2.0 / 3.0