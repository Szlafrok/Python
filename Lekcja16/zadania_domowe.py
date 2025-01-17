"""
                ZADANIE 1 (0-3)
"""

# Korzystając z przygotowanego w czasie lekcji projektu w pliku projekt.py
# proszę zaimplementować limit salda konta. Limit powinien być ustawiany za
# pomocą stałej:

LIMIT = 1200 # Przykładowa wartość

# Podczas wpłaty pieniędzy na konto saldo nie może przekroczyć limitu.
# Rozwiązanie proszę opatrzyć komentarzami i przesłać cały projekt ;)

# (Patryk, zrobiłeś to zadanie na lekcji i masz je już zaliczone - komplet punktów!)


"""
                ZADANIE 2 (0-4)
"""

# Dana jest funkcja, która pobiera i zwraca dane logowania:

def pobierz_pin() -> str: # Zwraca wprowadzony kod PIN w formie stringa
    kod_pin = input("Wprowadź PIN do karty: ")
    return kod_pin 

# Podobnie jak w zadaniu 1, proszę przyjąć, że obecna jest stała:

PIN = "1234" # Przykładowe dane

# Proszę przeprogramować projekt tak, aby przed przyznaniem dostępu
# do menu głównego pytał się użytkownika o kod PIN. Program powinien
# dopuszczać dwa błędy, przy trzecim powinien zakończyć działanie.
# Podanie poprawnego pinu przenosi nas do wyboru operacji.


"""
                ZADANIA DODATKOWE (+2 pkt)
"""

# a) (+ 0.5 p) Proszę przepisać zadanie 2 tak, aby dopuszczało N prób logowania zamiast
#              trzech. N powinno być określane w stałej, podobnie jak PIN i LIMIT

# b) (+ 1.5 p) Proszę zaimplementować piątą opcję wyboru dla użytkownika - historię
#              operacji na koncie. Każdy wpis w historii powinien zawierać informacje
#              o typie operacji (wpłata/wypłata), jej kwocie oraz saldzie po wykonanej
#              operacji. Można wykorzystać do pomocy poniższy skrypt:

historia = [
            (1, 50, 50),
            (2, 30, 20)
                        ] # Przykładowe dane

for wpis in historia:
    if wpis[0] == 1:
        print(f"Wpłata {wpis[1]} zł - obecne saldo {wpis[2]} zł.")
    else:
        print(f"Wypłata {wpis[1]} zł - obecne saldo {wpis[2]} zł.")