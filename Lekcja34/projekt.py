import json
from pprint import pprint
file_path = "Lekcja34/"

gra = {
    "tytul": "Maluch Simulator",
    "rok_wydania":"-50",
    "wydawca":"Valve ale POLSKA GUROM spułka zoo",
    "gatunek":"Karcianka"
}


#file = open(f"{file_path}spis.json", "r")
with open(f"{file_path}spis.json", "r") as file:
    spis_gier = json.load(file)
spis_gier["spis_gier"].append(gra)

pprint(spis_gier)

with open(f"{file_path}nowy_spis.json", "w") as file:
    json.dump(spis_gier, file, indent = 4, sort_keys = True)

dane_dodatkowe = {
    "czas_powstawania":"20 minut",
    "wartosc_rynkowa":"3,50 jeny"
}

lepsza_gra = gra | dane_dodatkowe
gorsza_gra = {**gra, **dane_dodatkowe}
pprint(gorsza_gra)
pprint(lepsza_gra)


fib_dict = {0:0, 1:1}

def fibonacci(n):
    if n in fib_dict:
        return fib_dict[n]
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        fib_dict[n] = result
        return result
    
fibonacci(20)
for item in fib_dict.items():
    print(item)