# Niestety nie mam tu za bardzo warunków do nagrywania rozwiązań zadań - muszę to zrobić
# w formie takiego opisu. Mam jednak nadzieję, że rozwiązania, oprawione komentarzami, będą
# klarowne i zrozumiałe. W razie pytań proszę pisać ;)

# Zadanie 1 - Wasza inwencja twórcza

# Zadanie 2

def logowanie(popr_login, popr_haslo):
    login = input("Podaj login: ")
    haslo = input("Podaj hasło: ")
    if login == popr_login and haslo == popr_haslo:
        return True
    return False

def logowanie_nowe(popr_login, popr_haslo, n): # Przyjmuje dodatkowy argument n
    i = 0
    while i < n: # Wrzucamy poprzedni kod do pętli, która wykonuje się n razy
        login = input("Podaj login: ")
        haslo = input("Podaj hasło: ")
        if login == popr_login and haslo == popr_haslo:
            print("Prawidłowe logowanie!")
            return True # Jeżeli poprawnie się zalogowaliśmy, funkcja zakończy się w tym miejscu
        print(f"Błąd logowania. Pozostało Ci {n-i-1} podejść.") # -1 bierze się stąd, że jeszcze nie zwiększyliśmy indeksu.
        i += 1
    print("Wyczerpano próby! Computero Explodato") # Opuszczenie pętli oznacza, że i == n, czyli wyczerpaliśmy limit prób.
    return False

logowanie_nowe("Bitwa_o_sztandar", "epicgameplay_", 4)


# Zadanie 3

def cyfry(n):
    # Wzór wyznaczający ostatnią cyfrę w liczbie to n%10
    # Podstawienie obcinające ostatnią cyfrę w liczbie to n //= 10
    res = 0 # res od "result", przechowująca wynik funkcji
    while n > 0: # Dopóki n > 0, mamy w niej jakieś cyfry, które możemy brać pod uwagę. Zera nie liczą się do dodawania.
        res += n % 10 # Wyciągamy ostatnią cyfrę...
        n //= 10 # ... i obcinamy ją
    return res

print(cyfry(12345))

# Zadanie 4
# Wszyscy dostali za to komplet ;)



# Zadanie 5 (DLA MEGA AMBITNYCH)

# Będziemy przechodzili po kolejnych elementach otrzymanej listy. Aby sprawdzić, czy dana liczba może być elementem
# szukanego podciągu, musimy sprawdzić, czy jest pierwsza. Zatem:

import math # Robię to SPECJALNIE, zamiast "from math import sqrt" żebyście zobaczyli, jak się odwołuje do funkcji z modułu!

def is_prime(n): # Wyjaśnialiśmy optymalizację do funkcji sprawdzającej, czy liczba jest pierwsza na zajęciach!
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    d = 3
    s = math.sqrt(n) # !!!!!!!
    while d <= s:
        if n % d == 0:
            return False
        d += 2 # Pamiętamy, aby zwiększać indeks! O 2, bo liczby parzyste sprawdziliśmy, więc sprawdzamy nieparzyste: 3, 5, 7...
    return True # Jeżeli nie znaleźliśmy dzielników liczby to znaczy, że jest pierwsza

def ciag(liczby):
    seq_len = 0 # Tu przechowujemy aktualną długość ciągu
    max_len = 0 # Tu przechowujemy najdłuższy dotychczasowy ciąg

    for l in liczby: # Dla każdego elementu w liście liczby
        if is_prime(l): # Jeżeli pierwsza
            seq_len += 1 # Jeżeli poprzednia nie była pierwsza, to seq_len = 1. W przeciwnym razie po prostu dodajemy 1. Rezultat taki sam :P
            max_len = max(seq_len, max_len) # Jeżeli seq_len > max_len to max_len = seq_len. W przeciwnym razie bez zmian.
        else: # Jeżeli niepierwsza
            seq_len = 0

    return max_len

print(ciag([5, 3, 4, 6, 8, 2, 3, 11, 19, 10]))