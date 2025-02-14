# Proszę napisać prostą aplikację konsolową, w której utworzymy 4 użytkowników
# i wypiszemy informacje na ich temat na ekranie

from Uzytkownik import Uzytkownik

user_1 = Uzytkownik()
user_2 = Uzytkownik()
user_3 = Uzytkownik()

user_1.imie = "Jan"
user_1.nazwisko = "Kowalski"
user_1.wiek = 32

user_2.imie = "Marcin"
user_2.nazwisko = "Najman"
user_2.wiek = 50

user_3.imie = "Pan"
user_3.nazwisko = "Paweł"
user_3.wiek = 17

user_1.wypisz_dane()
user_2.wypisz_dane()
user_3.wypisz_dane()

user_1.pelnoletni()
user_2.pelnoletni()
user_3.pelnoletni()

user_1.zmiana_wieku(15)
user_1.wypisz_dane()
# print(user_1.imie, user_1.nazwisko, user_1.wiek)
# print(user_2.imie, user_2.nazwisko, user_2.wiek)
# print(user_3.imie, user_3.nazwisko, user_3.wiek)

# imie_1 = "Jan"
# nazwisko_1 = "Kowalski"
# wiek_1 = 32

# imie_2 = "Tytus"
# nazwisko_2 = "Bomba"
# wiek_2 = 50

# imie_3 = "Jerzy"
# nazwisko_3 = "Kiler"
# wiek_3 = 15

# imie_4 = "Gwiazda"
# nazwisko_4 = "Śmierci"
# wiek_4 = 999

# if wiek_1 >= 18:
#     print(f"{imie_1} {nazwisko_1} jest pełnoletni")

# if wiek_2 >= 18:
#     print(f"{imie_2} {nazwisko_2} jest pełnoletni")

# if wiek_3 >= 18:
#     print(f"{imie_3} {nazwisko_3} jest pełnoletni")

# if wiek_4 >= 18:
#     print(f"{imie_4} {nazwisko_4} jest pełnoletni")


# Dla każdego użytkownika proszę napisać, czy jest pełnoletni