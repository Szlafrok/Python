# ---------- PRZYKŁAD 1 ------------

"""
Bierzesz udział w pierwszej fazie turnieju e-sportowego.
O przejściu dalej decyduje liczba wygranych meczów oraz zdobytych odznaczeń
MVP (Most Valuable Player). Aby przejść dalej należy zdobyć minimum 10
wygranych oraz mieć ich więcej niż przegranych lub zdobyć 7 odznaczeń MVP.
Liczbę meczy wygranych, przegranych oraz liczbę odznaczeń MVP należy odczytać
od użytkownika na początku programu.
"""

# Rozwiązanie:
mvp = int(input("Podaj liczbę zdobytych odznaczeń MVP: "))
wygrane = int(input("Podaj liczbę wygranych meczy: "))
przegrane = int(input("Podaj liczbę przegranych meczy: "))

if mvp >= 7 or wygrane >= 10 and wygrane > przegrane: # Pamiętamy o kolejności działań na operatorach logicznych!
    # Gdybyśmy zapisali to z nawiasami, wyglądałoby to tak: (mvp >= 7) or (wygrane >= 10 and wygrane > przegrane)
    print("Kwalifikujesz się! Gratulacje!")
else:
    print("Odpadasz! Przykro mi!")

# --------- PRZYKŁAD 2 ----------
"""
Proszę zaimplementować prosty kalkulator. Program powinien zapytać
o znak działania (dodawanie: +, odejmowanie: -). Następnie wprowadzamy
2 liczby i wykonujemy działanie na nich.
"""
operacja = input("Wybierz operację: ")

if not (operacja == "+" or operacja == "-"):
    print("Nieprawidłowe działanie!")
    exit() # Funkcja exit() kończy działanie kodu - przerywa go całkowicie.

liczba_1 = float(input("Wprowadź liczbę 1: "))
liczba_2 = float(input("Wprowadź liczbę 2: "))

if operacja == "+": # Nie musimy już rozpatrywać innych przypadków, bo program wypluje błąd, jeżeli podamy coś innego niż "+" lub "-".
    print(f"Wynik działania to {liczba_1 + liczba_2}")
else:
    print(f"Wynik działania to {liczba_1 - liczba_2}")