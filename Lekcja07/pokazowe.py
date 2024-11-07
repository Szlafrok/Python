x = 5
#print("Liczba jest równa ", x)
x += 4**2 + 14//7
x = x + (4**2 + 14//7)

# -----------------------

wiek = 0 # Włądzimiesz Biały

while wiek < 80: # Co roku
    wiek += 1
    print(f"Włądzimiesz obchodzi dziś {wiek} urodziny!")
print("Włodek zmarzł wczorajszej nocy. Żona znalazła ciasto na kanapie. Pokój jego duszny.")


wiek = 32 # Przemó

while wiek < 65: # Co roku
    print(f"Przemó dostał dzisiaj na swoje {wiek} urodziny premię dwuletnią!")
    wiek += 2
print("idę w spanko")

i = 0
while i <= 10: # 11 razy
    print(f"Cześć Gigancie {i}")
    i += 1

# ZADANIE SAMODZIELNE 1

# Proszę rozwinąć powyższą pętlę tak, aby powitała Giganta 25 razy.

i = 0
while i < 25:
    print(f"Siemano Gigancie")
    i += 1


# ZADANIE SAMODZIELNE 2
# Proszę zaczytać od użytkownika liczbę i wypisać jakiś śmieszny napis dokładnie tyle razy, ile podana liczba.

i = 0
j = int(input("Podaj liczbę: "))

while i < j:
    print ("hej hej kup se klej")
    i += 1 # i = i + 1

while 1: # True
    # Pętla nieskończona
    pass

