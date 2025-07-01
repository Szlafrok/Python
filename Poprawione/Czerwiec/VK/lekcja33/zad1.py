def zgaduj_liczbe(zakres):
    liczby = []
    for i in range(zakres):
        liczby.append(i)

    zgadnieto = False
    while not zgadnieto: # bdb użycie flagi
        n = len(liczby)
        liczba = liczby[n // 2]
        print(f"Zgaduję że to liczba: {liczba}")
        czy_zgadnieto = input("Za mało/za dużo/tak: ").lower()
        if czy_zgadnieto not in ("za mało", "za dużo", "tak"):
            print("Nie ma takiego wyboru, spróbuj ponownie.")
            continue
        
        if czy_zgadnieto == "za mało":
            liczby = liczby[n // 2:]
        elif czy_zgadnieto == "za dużo":
            liczby = liczby[:n // 2 + 1]
        else:
            print("Zgadłem!!!")
            zgadnieto = True

zgaduj_liczbe(1000)

# Rozumiesz ideę sortowania binarnego, jednak warto tu napomknąć o złożoności czasowej Twojego rozwiązania.
# Złożoność czasowa O(x) oznacza, że Twój program wykonuje co najwyżej jakąś skończoną wielokrotność x operacji.
# Przykładowo, sortowanie przez wybór jest algorytmem w złożoności O(n^2), ponieważ ponieważ dla każdej z n pozycji 
# w tablicy przeszukuje (w najgorszym wypadku) pozostałe n elementów w celu znalezienia najmniejszego. To oznacza, 
# że całkowita liczba porównań rośnie proporcjonalnie do kwadratu liczby elementów — np. dla 1000 elementów może 
# to być nawet około miliona operacji.

# Wyszukiwanie liniowe w ten sposób ma złożoność O(n), gdzie n to długość przeszukiwanej listy.
# Wyszukiwanie binarne ma złożoność O(log n), która jest lepsza od złożoności O(n), ale ma dodatkowy warunek -
# - lista, po której się porusza, musi być posortowana.

# https://www.matemaks.pl/logarytmy.html

# Wyszukiwanie binarne jest O(log n), ponieważ wykonuje maksymalnie log₂n operacji: np. dla n = 1000 wykonuje
# 10 przeszukań. Jeżeli wykorzystujesz mechanizm slicingu, każdy z nich w celu odpowiedniego ucięcia listy wykonuje
# do n operacji. Z tego powodu złożoność Twojego rozwiązania to O(n log n), co jest złożonością gorszą niż O(log n).

# Kiedy korzystamy z wyszukiwania binarnego, praktycznie zawsze operujemy na indeksach, aniżeli całych przedziałach
# - zamiast ciąć listę zawężamy przedział, który przeszukujemy, i robimy to za pomocą indeksów.
# Będę wstawiał na GitHuba omówienie tych zadań, tam pokażę taką implementację. W razie pytań będę też do dyspozycji
# po kolejnych zajęciach.

# Samo zadanie jest zrobione poprawnie, także masz maksymalny wynik (4/4), ale pamiętaj o tym następnym razem,
# gdy będziesz chciał wykorzystać wyszukiwanie binarne ;)