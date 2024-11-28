
"""

                            ★ ZADANIA DLA CHĘTNYCH ★


"""
# 1. Każde zadanie dodatkowe wykonane do końca lekcji daje bonus do zadań domowych!
# 2. Wykonane zadania możemy odsyłać na kamiennygigant@gmail.com
# 3. Zadania dodatkowe przyjmuję do 21:00 ;)
# 4. Robimy je TYLKO, jeżeli z zadaniem na lekcji jesteśmy na bieżąco i nie mamy co robić!
# 5. Odsyłając zadania napisz mi proszę w mailu, co sądzisz o poziomie trudności tych zadań,
#    o ich ilości i o samej koncepcji zadań dodatkowych w czasie lekcji ;)


# ---------- Zadanie 1. (+2 pkt) -----------

# Ciąg arytmetyczny to taki ciąg liczb, że pomiędzy dwoma sąsiednimi elementami jest zawsze
# taka sama różnica. Przykładowo:

# Ciąg [2, 4, 6, 8, 10] jest ciągiem arytmetycznym.
# Ciąg [2, 6, 4, 8, 10] NIE jest ciągiem arytmetycznym.

# Proszę napisać funkcję arytm(ciag), która przyjmuje jako argument listę liczb całkowitych i zwraca:
# >>> True, jeżeli ciąg jest arytmetyczny
# >>> False, jeżeli ciąg nie jest arytmetyczny.

# Przykład: Dla podanych wywołań otrzymamy:

# arytm([-1, 5, 11, 17, 23]) -> True (różnica == 6)
# arytm([5, 4, 3, 2, 1]) -> True (różnica == -1)
# arytm([5, 5, 5, 5]) -> True (różnica == 0)
# arytm([7, 8, 7, 6]) -> False (różnica nie jest stała)

# Szablon:

def arytm(ciag):
    pass

# Uwaga: ciąg musi zawierać przynajmniej JEDEN element!

# ---------- Zadanie 2. (+2 pkt) -----------

# Proszę napisać funkcję, która przyjmuje jako argument liczbę naturalną n i zwraca:
# -> True, jeżeli liczba jest pierwsza
# -> False, w przeciwnym razie.

# Szablon:

def is_prime(n):
    pass

# --- SPRAWDZARKA ---

def check(zad):
    if zad == 1:
        x = []
        print("Wpisz 'stop', aby przerwać wpisywanie liczb.")
        odp = ""
        while True:
            odp = input("Wprowadź element ciągu: ")
            if odp == "stop": 
                break
            x.append(int(odp))
        print("Ciąg jest arytmetyczny" if arytm(x) else "Ciąg nie jest arytmetyczny")
    else:
        x = int(input("Podaj liczbę: "))
        print("Liczba jest pierwsza" if is_prime(x) else "Liczba nie jest pierwsza")

check(2) # Wprowadź numer zadania i uruchom program, aby przetestować swoje rozwiązanie.


# POWODZENIA!!!!