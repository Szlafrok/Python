#1)
x = int(input("Podaj liczbę naturalną:"))#wczytuję liczbę od jakiegoś ziomka   0,5 / 0,5
if x <= -1:
    print("Błąd liczba minusowa.")#żeby ktoś nie podał liczby minusowej
elif x < 2:
    print("To nie jest ani liczba pierwsza ani liczba złożona.")#liczby 0 i 1 to nie są ani liczby pierwsze ani liczby złożone # 0.75 / 1.00
elif x % 2 and x % 3 and x % 5 and x % 7: # Za weryfikację dzielników 0.5 / 3.0, + bonus 0.5 za sprytny pomysł!
    print("To jest liczba pierwsza.")#liczby pierwsze są niepodzielne przez żadne liczby (OPRÓCZ 1 I SIEBIE SAMEJ, ale nie utnę Ci już za to punktu)
else:
    print("To jest liczba złożona.")#wszystkie inne liczby są złożone
exit()

# Wczytanie liczby i rozpatrzenie przypadków szczególnych OK, oprócz dwójki. Co jeżeli x == 2? 
# Bardzo sprytny pomysł ze zrobieniem warunków z x % dzielnik, ale nie sprawdzasz pozostałych liczb pierwszych!
# Należy to zrobić za pomocą pętli. Co zrobisz, jeżeli otrzymasz np. 121, czyli kwadrat 11? Albo 323, iloczyn 17 i 19?

# Sprytny pomysł z warunkami w elifie, muszę przyznać :)

# 0.5 + 0.75 + 0.5 (+ bonus 0.5) = (2.25 pkt / 5.00) za to zadanie


# Komentarze: (+1 pkt / 1)

#B)
#nie trzeba ponieważ jeśli liczba jest podzielna przez np 4 to jest 
#podzielna przez 2 bo 4 jest podzielne przez 2

# Uzasadnienie ograniczone do przykładu. Ja wiem i Ty wiesz, ale trzeba to jeszcze napisać!
# Chodziło ogólnie o liczby dodatnie parzyste! Nie bierzesz pod uwagę 6, 8, 10, 12, itd. (+1 pkt / 2)

#C)
x = int(input("Podaj liczbę naturalną:"))#wczytuję liczbę od jakiegoś ziomka
if x <= -1:
    print("Błąd liczba minusowa.")#żeby ktoś nie podał liczby minusowej
elif x < 2:
    print("To nie jest ani liczba pierwsza ani liczba złożona.")#liczby 0 i 1 to nie są ani liczby pierwsze ani liczby złożone
elif x % sqrt(4) and x % sqrt(9) and x % sqrt(25) and x % (49):
    print("To jest liczba pierwsza.")#liczby pierwsze są niepodzielne przez żadne liczby
else:
    print("To jest liczba złożona.")#wszystkie inne liczby są złóżone
exit()

# Niestety, nie jest to usprawnienie. Niczego to nie zmienia, poza tym nie dałeś sqrt przed (49). (+0 pkt / 1)



# Razem za bonusy: 1 + 1 + 0 = (+2 pkt)