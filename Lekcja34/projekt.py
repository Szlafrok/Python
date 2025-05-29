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

