#1)zaimplementuj funkcję dodawanie :)
def dodac(a, b):
    print(a + b)
dodac(int(input("Podaj pierwszą liczbę:")), int(input("Podaj drugą liczbę:")))

# Zadanie poprawne, ale bardzo proste. Poza tym printuje wartość, nie zwraca jej wartości :(
# (1.5 / 3.0)

#2)

g = 0
def logowanie(popr_login, popr_haslo, n):
    if g <= n:
        login = input("Podaj login: ")
        haslo = input("Podaj hasło: ")
        if login == popr_login and haslo == popr_haslo:
            print("Zalogowano...")
        else:
            print("nuh uh")
    elif g > n:
        print("Za dużo prób.")
    g + 1

logowanie(popr_login = "MlodSlowRoku", popr_haslo = "sigma", n = 5)

# - Funkcja printuje wartość, nie zwraca wartości True ani False, a miała tak zrobić
# - Nie korzystasz w funkcji z pętli, a jest ona KONIECZNA, żeby umożliwić więcej niż jedną próbę!
# Poza tym pomysł generalnie dobry, ale te dwa błędy, zwłaszcza drugi, są dość poważne :[
# (1.5 / 3.0)

#3)
def cyfry(n):
    suma = 0
    for cyfra in str(n):
        suma += int(cyfra) # Ładna iteracja po stringu!
    print(suma)
cyfry(int(input("Podaj liczbę:")))

# Bardzo ładnie :) Jedyny minus jest taki, że nie zwracasz wartości, tylko ją printujesz.
# (1.5 / 2.0)