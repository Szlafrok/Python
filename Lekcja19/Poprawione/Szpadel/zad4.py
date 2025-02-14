def przelicz(ciag: str) -> dict:
    znaki = {}

    for i in range(len(ciag)):
        if ciag[i] in znaki.keys(): # sprawdzamy czy znak już jest w znakach
            znaki[ciag[i]] += 1 # jeżeli jest dodajemy 1 do ilości jego wystapień
        else:
            znaki[ciag[i]] = 1 # w przeciwnym wypadku dodajemy nowy znak

    return znaki
# spacje to tez znaki więc ich nie usuwamy
zdanie = "testowe zdanie ze spacjami i 2 liczbami 2 ĄĄĄĄĄĄ" 
print(przelicz(zdanie))

# Bardzo ładne wykorzystanie słowników ;)

# 4/4 +1 za dodatkowe -> 5 pkt