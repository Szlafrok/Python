zero = ["0", "zero", "zera", "zerem", "nic"]
jeden = ["1", "jeden", "jedynka", "jedynkę", "jedynki", "jednego"]
dwa = ["2", "dwa", "dwójka", "dwójkę", "dwójki", "dwóch"]
trzy = ["3", "trzy", "trójka", "trójkę", "trójki", "trzech"]
cztery = ["4", "cztery", "czwórka", "czwórkę", "czwórki", "czterech"]
piec = ["5", "pięć", "piątka", "piątkę", "piątki", "pięciu"]
sześć = ["6", "sześć", "sześciu", "sześcioma", "sześciu"]
siedem = ["7", "siedem", "siedmiu", "siedmioma", "siedmiu"]
osiem = ["8", "osiem", "ośmiu", "ośmioma", "ośmiu"]
dziewięć = ["9", "dziewięć", "dziewięciu", "dziewięcioma", "dziewięciu"]
dziesięć = ["10", "dziesięć", "dziesięciu", "dziesięcioma", "dziesięciu"]
jedenaście = ["11", "jedenaście", "jedenastu", "jedenastoma", "jedenastu"]
dwanaście = ["12", "dwanaście", "dwunastu", "dwunastoma", "dwunastu"]
trzynaście = ["13", "trzynaście", "trzynastu", "trzynastoma", "trzynastu"]
czternaście = ["14", "czternaście", "czternastu", "czternastoma", "czternastu"]
piętnaście = ["15", "piętnaście", "piętnastu", "piętnastoma", "piętnastu"]
szesnaście = ["16", "szesnaście", "szesnastu", "szesnastoma", "szesnastu"]
siedemnaście = ["17", "siedemnaście", "siedemnastu", "siedemnastoma", "siedemnastu"]
osiemnaście = ["18", "osiemnaście", "osiemnastu", "osiemnastoma", "osiemnastu"]
dziewiętnaście = ["19", "dziewiętnaście", "dziewiętnastu", "dziewiętnastoma", "dziewiętnastu"]
dwadzieścia = ["20", "dwadzieścia", "dwadzieścia", "dwadzieścioma", "dwadzieścia"]
dodawanie = ["+", "dodawanie", "dodać", "plus", "sumowanie", "więcej", "dodaj"]
odejmowanie = ["-", "odejmowanie", "odjąć", "minus", "różnica", "mniej", "odejmij"]
mnozenie = ["*", "mnożenie", "pomnożyć", "razy", "iloczyn", "przemnóż"]
dzielenie = ["/", "dzielenie", "podzielić", "iloraz", "podziel"]

baza = [zero, jeden, dwa, trzy, cztery, piec,sześć, siedem, osiem, dziewięć, dziesięć, jedenaście, dwanaście, trzynaście, czternaście, piętnaście, szesnaście, siedemnaście, osiemnaście, dziewiętnaście, dwadzieścia, dodawanie, odejmowanie, mnozenie, dzielenie]

#--------------------------------------------


def przetlumacz_slowo(slowo: str) -> str:
    for baza_symbolu in baza:
        for elem in baza_symbolu:
            if slowo == elem:
                return baza_symbolu[0]
    return ""

def wynik_operacji(l1: int, l2: int, oper: str) -> float:
    if oper == "+":
        return l1 + l2
    elif oper == "-":
        return l1 - l2
    elif oper == "*":
        return l1 * l2
    else:
        return l1 / l2

def oblicz_z_tekstu(dzial: str) -> float:
    wynik = 0
    liczba = ""
    operacja = ""
    for znak in dzial:
        if znak.isdigit():
            liczba += znak
        else:
            operacja = znak
            wynik = int(liczba)
            liczba = ""
    liczba = int(liczba)
    return wynik_operacji(wynik, liczba, operacja) # brakowało tej linijki


dzialanie = ""
tekst = input("Proszę wprwadzić działanie:")

for slowo in tekst.split(" "):
    dzialanie += przetlumacz_slowo(slowo)

print(dzialanie)
print(oblicz_z_tekstu(dzialanie)) # dopisałem

# Zadanie dodatkowe zaliczone :)

# +2 pkt