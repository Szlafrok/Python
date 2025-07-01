import math

lista = [x for x in range(1, 11)] # 1p
print(lista)
pierwiastek_lista = [math.sqrt(x) for x in lista]
print(pierwiastek_lista)
pierwiastki_zaokraglone = [round(math.sqrt(x), 2) for x in pierwiastek_lista] # ok
print(pierwiastki_zaokraglone)

krotka = tuple(x for x in range(11, 21)) # 1p
print(krotka)
pierwiastek_krotka = [math.sqrt(x) for x in krotka]
print(pierwiastek_krotka)
pierwiastki_zaokraglone = [round(math.sqrt(x), 2) for x in pierwiastek_krotka] # ok
print(pierwiastki_zaokraglone)

zbior = {x for x in range(21, 31)} # 1p
print(zbior)
pierwiastek_zbior = [math.sqrt(x) for x in zbior]
print(pierwiastek_zbior)
pierwiastki_zaokraglone = [round(math.sqrt(x), 2) for x in pierwiastek_zbior] # ok
print(pierwiastki_zaokraglone)

zakres = range(31,41) # Poprawiłem polecenie już po tym, jak zrobiłeś to zadanie, ale dobrze się dostosowałeś :)
print(zakres)
pierwiastek_zakres = [math.sqrt(x) for x in zakres]
print(pierwiastek_zakres)
pierwiastki_zaokraglone = [round(math.sqrt(x), 2) for x in pierwiastek_zakres] # +0.25 pkt
print(pierwiastki_zaokraglone)

# 1a (3p / 3p)
# 1b (1p / 1p) (+0.25 bonus)

# Bardzo ładnie!