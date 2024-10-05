print('a ktora jest godzina')
godzina=float(input())
print(godzina)
godzina_do_polnocy= 23 - int(godzina) #brakowało mi tu tego INTa + dla większości przypadków podstawiamy 23
minuta_do_polnocy = 60 - int((godzina % 1) * 100)
print(f"za {godzina_do_polnocy} godzin i {minuta_do_polnocy} minut bedzie polnoc")

# nie rozpatruje przypadku szczególnego - godzina XX:00
# bardzo innowacyjne podejście, brawo!

####
print('a ktora jest godzina')
godzina=float(input())
godzina_do_polnocy= 23 - int(godzina)
minuta_do_polnocy = 23.60 - float(godzina)
print(f"za {godzina_do_polnocy} godzin i {minuta_do_polnocy} minut bedzie polnoc")