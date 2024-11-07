m = int(input("Wpisz swoją ocenę z matematyki:"))
jp = int(input("Wpisz swoją ocenę z języka polskiego:"))
ja = int(input("Wpisz swoją ocenę z języka angielskiego:"))
f = int(input("Wpisz swoją ocenę z fizyka:"))
g = int(input("Wpisz swoją ocenę z geografii:"))
z = int(input("Wpisz swoją ocenę z zachowania:"))
s = float((m + jp + ja + f + g)/5) # Nie musisz robić z tego floata, domyślnie to już będzie floatem
if s>= 4.75 and z >= 5:
    print(f"PASEK o średniej {s}")
else:
    print("Przegryw") # Wg treści zadania musisz zawsze podać średnią, a tu tego brakuje :P Ale nie utnę już niczego za to, to drobna rzecz.

# 3.0 / 3.0