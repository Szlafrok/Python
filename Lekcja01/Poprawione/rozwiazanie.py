print("Podaj obecną godzinę")
godzina = int(input())

print("Podaj obecną minutę")
minuta = int(input())

if minuta == 0: # Przypadek szczególny - mamy równą godzinę
    godzina = 24 - godzina
    print("Do północy pozostało", godzina, "godzin i 0 minut.")
else:
    godzina = 23 - godzina
    minuta = 60 - minuta
    print("Do północy pozostało", godzina, "godzin i", minuta, "minut.")