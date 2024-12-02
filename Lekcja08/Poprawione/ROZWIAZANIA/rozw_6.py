h = int(input("Ho ho ho! Podaj liczbę!"))

for i in range(h):
    print(f"{" " * (h - 1 - i)}{"* " * (i+1)}")