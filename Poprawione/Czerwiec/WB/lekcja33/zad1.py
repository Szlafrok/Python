def zgadywanie():
    dol = 1
    gora = 1000
    proby = 0

    while True:
        strzal = (dol + gora) // 2
        proby += 1
        print("Czy to:", strzal)
        odp = input("Odpowiedz ('za mało', 'za dużo', 'tak'): ").strip().lower()

        if odp == "tak":
            print("Zgadłem w", proby, "próbach!")
            break
        elif odp == "za mało":
            dol = strzal + 1
        elif odp == "za dużo":
            gora = strzal - 1
        else:
            print("Nie rozumiem odpowiedzi, wpisz jeszcze raz.")

zgadywanie() # Bardzo ładnie :) (4 / 4)
# Jedna uwaga do linijki 8 - zwiększasz liczbę prób nawet jeżeli użytkownik poda nieznaną
# przez system odpowiedź. Nie zmniejszę Ci wyniku, bo nie jest to istotna część zadania,
# ale może Ci to zakrzywić wyniki, jeżeli będziesz chciał eksperymentować na tym algorytmie
# i sprawdzać liczbę podejść dla konkretnych liczb ;)

# bonus 
'''
Program używa wyszukiwania binarnego, więc liczba prób zależy od log₂(1000).
Najwięcej prób potrzeba, gdy liczba jest w środku, np. 512.
Wynik: maksymalnie 10 prób, bo 2¹⁰ = 1024.
'''

# Poprawnie pokazałeś, w skąd wziąłęś liczbę strzałów i podałeś przykład liczby, której
# odgadnięcie przez ten algorytm faktycznie wymaga 10 podejść. Jeżeli jednak wybierzesz liczbę
# idealnie w środku - tu 500 - zostanie ona odgadnięta dość szybko, ponieważ program wyceluje
# właśnie w nią, na tym polega wyszukiwanie binarne.

# Jeżeli chcesz mieć pewność, że programowi zajmie to długo, musisz "schować się" tuż pod granicą
# lub liczbą, o której wiesz że program spróbuje ją odgadnąć. Przykładowo:

# Do 1000 będziemy musieli się zbliżać w 10 ruchach, bo leży na skraju, czyli najdalej od środka.
# 1 podobnie, choć fakt że wykorzystujemy dzielenie całkowite (które zaokrągla strzały w dół) może
# potencjalnie zmienić ten wynik o 1 próbę.

# Po podziale na pół program strzeli w 500. Jeżeli odpowiedzią jest 499 lub 501, również leżymy
# na skraju przedziału, w którym będzie odgadywał program!
# Spośród 499 i 501 bezpieczniejszą opcją jest 499, z tych samych powodów dla których 1000 jest 
# bezpieczniejsze niż 1.


# Bonus za zadanie: (+1.0 / 1.5). Nieźle ;)