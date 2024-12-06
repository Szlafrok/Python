"""
    Może są to 4 zadania, ale naprawdę, nie są one takie długie :P

    Termin wykonania: Niedziela 15 grudnia

    Gwoli przypomnienia, bo myślę, że warto o tym napomknąć:

    NIE MUSICIE robić wszystkich zadań! Każde jedno zadanie, które wykonacie, liczy się!
    Zawsze to jest ten krok do przodu, który robicie, żeby być LEPSZYMI PROGRAMISTAMI!

    Pamiętajcie, że robicie to przede wszystkim dla siebie. Ja też tu jestem po to, żeby
    Was czegoś nauczyć - jeżeli nie macie wszystkich zadań lub napisaliście je źle, również
    możecie mi je wysłać i ja powiem Wam, co trzeba poprawić.

    Możecie mnie też poprosić, żebym nie wstawiał Waszych rozwiązań do GitHuba - zastosuję się do tego!

    Powodzenia!!!

"""
# ZADANIE 1 (bazowo 3 pkt, można zdobyć maksymalnie 5 pkt)

# Proszę zaproponować zadanie programistyczne, które wymaga do zaimplementowania funkcji,
# a następnie je rozwiązać. Można korzystać z rzeczy, których nie było na zajęciach, ale 
# proszę nie przesadzać ;)


# ZADANIE 2 (3 pkt)

# Dana jest funkcja logowanie(popr_login, popr_haslo), która przyjmuje jako argumenty oczekiwany login oraz
# oczekiwane hasło. Funkcja pyta użytkownika o dane logowania, a następnie zwraca True, jeżeli dane są zgodne,
# lub False, jeżeli nie są zgodne.

def logowanie(popr_login, popr_haslo):
    login = input("Podaj login: ")
    haslo = input("Podaj hasło: ")
    if login == popr_login and haslo == popr_haslo:
        return True
    return False

# Proszę przepisać tę funkcję tak, aby przyjmowała dodatkowo argument n, gdzie n to liczba całkowita dodatnia, 
# która wyraża liczbę dopuszczalnych prób logowania. Funkcja powinna zwrócić True, jeżeli użytkownik zaloguje 
# się poprawnie, lub False, jeżeli przekroczy dopuszczalną liczbę logowań.


# ZADANIE 3 (2 pkt)
# Proszę napisać funkcję cyfry(n), która przyjmuje liczbę naturalną n i zwraca sumę jej cyfr.
# Przykładowo: Wywołanie cyfry(1235) zwraca 1 + 2 + 3 + 5 = 11


# ZADANIE 4 (2 pkt)
# Proszę przesłać mi na emaila pseudonim, który od teraz ma się pokazywać zamiast Twojego imienia i nazwiska ;)







# (*) ZADANIE 5 (UWAGA! dla bardzo ambitnych!!!) (+5 pkt)

# Dana jest lista liczby, która składa się z liczb naturalnych. Podciąg pierwszy to taki ciąg liczb, który
# składa się z kolejnych elementów listy liczby i wszystkie jego elementy są liczbami pierwszymi. Przykładowo:

# Lista liczby [4, 6, 7, 2, 8, 120, 3, 10, 7, 11, 19, 23] zawiera podciągi pierwsze:

# -> dwuelementowy podciąg pierwszy [7, 2]
# -> jednoelementowy podciąg pierwszy [3]
# -> czteroelementowy podciąg pierwszy [7, 11, 19, 23]

# Proszę napisać funkcję ciag(), która znajduje i zwraca długość najdłuższego podciągu pierwszego. Dla tego
# przykładu odpowiedź to 4.
# Wskazówka: Warto zaimplementować sobie funkcję is_prime(n), która określa, czy dana liczba jest pierwsza.

# Szablon:

liczby = [4, 6, 7, 2, 8, 120, 3, 10, 7, 11, 19, 23]

def ciag():
    pass