# Napisz funkcję, która otrzymuje 3 parametry:
# - proporcje_szerokosc
# - proporcje_wysokosc
# - piksele_szerokosc

# Funkcja otrzymuje oczekiwane proporcje ekranu (np. 16:9, 4:3) oraz piksele_szerokosc.
# Zadaniem funkcji jest obliczyć ile pikseli powinna mieć wysokość, aby proporcje ekranu
# były poprawne. Zwracana liczba powinna być liczbą całkowitą
# 16:9 -> 1920 x 1080
# 16:9 -> 1280 x 720
# 4:3 -> 1920 x 1440

def wymiar(proporcje_szerokosc, proporcje_wysokosc, piksele_szerokosc):
    
    res = piksele_szerokosc / proporcje_szerokosc * proporcje_wysokosc # wysokość w pikselach
    return res


w = wymiar(16, 9, 32)
print(w)
w = wymiar(4, 3, 1920)
print(w)

# 16:9 -> 32:18

