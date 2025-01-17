"""

                            ★ ZADANIE DLA CHĘTNYCH ★
                             nawet fajne mi wyszły :)

"""
# 1. Każde zadanie dodatkowe wykonane do końca lekcji daje bonus do zadań domowych!
# 2. Wykonane zadania możemy odsyłać na kamiennygigant@gmail.com
# 3. Zadania dodatkowe przyjmuję do 22:00 ;)
# 4. Robimy je TYLKO, jeżeli z zadaniem na lekcji jesteśmy na bieżąco i nie mamy co robić!
# 5. Odsyłając zadania napisz mi proszę w mailu, co sądzisz o poziomie trudności tych zadań,
#    o ich ilości i o samej koncepcji zadań dodatkowych w czasie lekcji ;)


"""
           ★ Zadanie 1 (+3 pkt)
"""
# Szablon:
VALUES = "0123456789abcdef"

def deci(num: str, syst: int) -> int:
    pass

# Proszę zaimplementować funkcję deci(num, syst), która przyjmuje jako argumenty:
# - stringa num, który przechowuje liczbę zapisaną w pewnym systemie
# - liczby naturalnej syst, która wskazuje na system, w którym zapisano liczbę num (np. 2 - system binarny, 8 - system ósemkowy).
# Argument syst spełnia warunek: (2 <= syst <= 16). Proszę napisać funkcję, która przełoży liczbę num z zadanego systemu na system dziesiętny.
# Przykładowo, dla wywołania:

wynik = deci("1100", 2)
print(f"Zadanie dodatkowe 1: Wynik = {wynik}")

# Funkcja powinna zwrócić do zmiennej wynik liczbę 12.
# PODPOWIEDZI: Skorzystaj z podanej stałej VALUES, aby ułatwić sobie wyznaczanie wyniku. 
#              Pamiętaj, że stringi można traktować jak listy znaków ;)



"""
           ★ Zadanie 2 (+2 pkt)
"""
# Szablon:
def sito(n: int) -> list:
    is_num_prime = [True] * n # Tablica przechowuje wartości logiczne, tak że is_num_prime[i] powinno zawierać True wtedy i tylko wtedy, gdy i jest pierwsze
    pass # Tu wpisz ciąg dalszy implementacji!

# Proszę zaimplementować funkcję pierwsze(n), która przyjmuje jako argument liczbę naturalną n, a następnie
# wyznacza i zwraca listę wszystkich liczb pierwszych na przedziale od 1 do n włącznie. Funkcja powinna
# korzystać z SITA ERASTOTENESA -> https://www.korepetycjezinformatyki.pl/sito-eratostenesa/

# Przykładowo, dla wywołania:

wynik = sito(16)
print(f"Zadanie dodatkowe 2: Wynik = {wynik}")

# W zmiennej wynik zostanie zawarta lista [2, 3, 5, 7, 11, 13].