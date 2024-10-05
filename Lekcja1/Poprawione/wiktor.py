print('ktora jest godzina')
godzina=input()
print('ktora jest minuta')
minuta = input()
godzina_do_polnocy= 23 - int(godzina) 
minuta_do_polnocy= 60 - int(minuta)

if minuta_do_polnocy == 60: # Przypadek szczególny
    minuta_do_polnocy = 0
    godzina_do_polnocy += 1

print(f"za {godzina_do_polnocy} godzina i {minuta_do_polnocy} minut bedzie polnoc")

# kiedy będą listy i tablice sprawdzić
# po pobieżnym przejrzeniu do przodu nie widać w najbliższym czasie

# POPRAWKI:
# linijka 6: wykorzystuje zmienną godzina zamiast minuta
# nie działa dla 60 minut

# poza tym ok