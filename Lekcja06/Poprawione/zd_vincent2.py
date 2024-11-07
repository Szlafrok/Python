ocena_zachowanie = float(input("Wprowadź ocenę z zachowania: "))
ocena_matematyka = float(input("Wprowadź ocenę z matematyki: "))
ocena_jezyk_polski = float(input("Wprowadź ocenę z języka polskiego: "))
ocena_jezyk_angielski = float(input("Wprowadź ocenę z języka angielskiego: "))
ocena_geografia = float(input("Wprowadź ocenę z geografi: "))
ocena_fizyka = float(input("Wprowadź ocenę z fizyki: "))

średnia = (ocena_matematyka + ocena_fizyka + ocena_jezyk_angielski + ocena_jezyk_polski + ocena_geografia) / 5 

if ocena_zachowanie >= 5 and średnia >= 4.75:
    pasek = "Dostajesz czerwony pasek."
else:
    pasek = "Niestety niedostajesz czerwonego paska."

print(f"Twoja średnia to {średnia} .")
print(pasek)

# Bardzo ładnie :>

# 3.0 / 3.0