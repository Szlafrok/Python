spacja = " " # zaznacz to jako stałą!
SPACJA = " "

while True:
    try: 
        wysokosc = int(input("Podaj wysokość choinki/piramidy: "))
        if wysokosc < 2:
            # print("Wysokość choinki/piramidy musi być większa od 1: ") 
            # A dlaczego nie może być 1?
            print("*")
            exit()
            continue
        break
    except ValueError:
        print("Zły typ danych, spróbuj ponownie")

for i in range(1, wysokosc + 1):
    spacje = wysokosc - i
    gwiazdki = i
    print(f"{spacja * spacje}{'* ' * gwiazdki}") # Robisz to troszkę niekonsekwentnie - spację dajesz do stałej, a gwiazdki jako surowy string?

# Zadanie zrobione ładnie, mam tylko tą uwagę w 20 linijce i pojedynczy przypadek szczególny :P

# Poza tym jest super ;)

# Wczytanie danych 0.25 / 0.5
# Warunki końca i początku pętli 0.5 / 0.5
# Symetria 1 / 1
# Pętla i matematyka stringów 2 / 2

# 3.75 / 4