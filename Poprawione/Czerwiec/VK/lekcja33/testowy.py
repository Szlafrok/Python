from random import randint

def wylosuj_liczbe(zakres):
    return randint(zakres[0], zakres[1])

zakres = [0, 1000]
print(wylosuj_liczbe(zakres))

# To plik eksperymentalny?