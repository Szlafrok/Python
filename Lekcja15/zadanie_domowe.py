# ŁĄCZNY WYNIK: 10 pkt
# Termin wykonania: 16.01.2025, godz. 18:25
# Możecie (i powinniście) korzystać z implementacji, które dotychczas pojawiły się na lekcjach. 
# Programiści w pracy również często korzystają z utworzonych wcześniej rozwiązań! Powodzenia!!! ;)


"""
            Zadanie 1 (1 pkt + 1 pkt za komentarze i opis)
"""

# Szablon: 

def not_prime(n: int) -> bool:
    pass

# Proszę zaimplementować funkcję not_prime(n), która przyjmuje jako argument liczbę naturalną n i
# zwraca True, jeżeli liczba jest złożona, lub False, jeżeli liczba jest pierwsza. Przykładowo, dla wywołania:

wynik = not_prime(2)
print(f"Zadanie domowe 1: Wynik = {wynik}")

# Do zmiennej wynik zostanie zwrócona wartość False.




"""
            Zadanie 2 (2 pkt + 1 pkt za komentarze i opis)
"""

# Szablon:
def trojeczka(n: int) -> str:
    pass

# Proszę zaimplementować funkcję trojeczka(n), która przyjmuje jako argument liczbę naturalną n zapisaną w
# systemie dziesiętnym i zwraca tę liczbę w systemie trójkowym. Przykładowo, dla wywołania:

wynik = trojeczka(15)
print(f"Zadanie domowe 2: Wynik = {wynik}")

# Otrzymanym wynikiem będzie "122" (bo 2*1 + 2*3 + 1*9 = 2 + 6 + 9 = 17)




"""
            Zadanie 3.1 (3.5 pkt + 1.5 pkt za komentarze i opis)
"""

# >>> SZABLON:
def cwaniak(wyrazy: list) -> int:
    n = len(wyrazy) # Długość listy wyrazy - liczba słów
    cwane = [False] * n # Określa, które wyrazy są cwane
    pass # Tu proszę wpisać dalszy ciąg funkcji!

# >>> TREŚĆ
# W liście wyrazy zawarta jest pewna liczba słów zapisanych w formacie stringa. Dane słowo jest cwane, jeżeli w tej liście znajduje się słowo
# zapisane w odwrotnej kolejności liter. Przykładowo, wyraz "majster" jest cwane, jeżeli na tej liście znajduje się wyraz "retsjam".
# Palindromy są cwane i mogą łączyć się same ze sobą!

# Proszę zaimplementować funkcję cwaniak(wyrazy), która przyjmuje jako argument listę wyrazy i zwraca liczbę CWANYCH słów z tej listy.


# >>> PRZYKŁAD - dla wywołania:
wynik = cwaniak(["kot", "kot", "pies", "pies", "owocowo", "tok"])
print(f"Zadanie domowe 3.1: Wynik = {wynik}")

# do zmiennej wynik zostanie zwrócona liczba 4. Uzasadnienie:

# cwaniak[0] == "kot". Odwróceniem tego wyrazu jest "tok", a "tok" jest obecne na tej liście. "kot" jest cwany! (1)
# cwaniak[1] == "kot". Odwróceniem tego wyrazu jest "tok", a "tok" jest obecne na tej liście. "kot" jest cwany! (2)
# cwaniak[2] == "pies". Odwróceniem tego wyrazu jest "seip", a "seip" nie ma na tej liście. "pies" NIE jest cwany!
# cwaniak[3] == "pies". Odwróceniem tego wyrazu jest "seip", a "seip" nie ma na tej liście. "pies" NIE jest cwany!
# cwaniak[4] == "owocowo". Odwróceniem tego wyrazu jest "owocowo", a "owocowo" jest obecne na tej liście. "owocowo" jest cwane! (3)
# cwaniak[5] == "tok". Odwróceniem tego wyrazu jest "kot", a "kot" jest obecne na tej liście. "tok" jest cwany! (4)


# >>> WSKAZÓWKI:
# 1. Proszę skorzystać z implementacji z lekcji, która sprawdza, czy wyraz jest palindromem. Przyda się ;)
# 2. Warto będzie skorzystać z pętli for, a nawet dwóch.
# 3. Oznaczaj cwane wyrazy jako True w liście "cwane"!

"""
            Zadanie 3.2 (+1 pkt) (Z gwiazdką! ★)
"""

# Proszę określić i uzasadnić, czy wynikami zwracanymi przez funkcję z zadania 3 mogą być:

# a) 0?
# b) 1?