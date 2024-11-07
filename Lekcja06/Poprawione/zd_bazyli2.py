pol = int(input("Podaj ocene z polaka."))
mat = int(input("Podaj ocene z matmy."))
ang = int(input("Podaj ocene z angielskiego."))
geo = int(input("Podaj ocene z gegry."))
fiz = int(input("Podaj ocene z fizyki."))

zach = int(input("Podaj ocene z zachowania."))

x = pol + mat + ang + geo + fiz
y = x / 5

if  y >= 4.75 and zach >= 5:
    print("Będziesz miał czerwony pasek na świadectwie. ;>")
else:
    print("Nie dostajesz czerwonego paska. :<")

print(f"Twoja średni wyniosła {y}.")

# Bardzo ładnie :D

# 3.0 / 3.0