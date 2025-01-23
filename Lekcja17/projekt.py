zero = ["0", "zero", "zera", "zerem", "nic"]
jeden = ["1", "jeden", "jedynka", "jedynkę", "jedynki", "jednego"]
dwa = ["2", "dwa", "dwójka", "dwójkę", "dwójki", "dwóch"]
trzy = ["3", "trzy", "trójka", "trójkę", "trójki", "trzech"]
cztery = ["4", "cztery", "czwórka", "czwórkę", "czwórki", "czterech"]
piec = ["5", "pięć", "piątka", "piątkę", "piątki", "pięciu"]

dodawanie = ["+", "dodawanie", "dodać", "plus", "sumowanie", "więcej", "dodaj"]
odejmowanie = ["-", "odejmowanie", "odjąć", "minus", "różnica", "mniej", "odejmij"]
mnozenie = ["*", "mnożenie", "pomnożyć", "razy", "iloczyn", "przemnóż"]
dzielenie = ["/", "dzielenie", "podzielić", "iloraz", "podziel"]

baza = [zero, jeden, dwa, trzy, cztery, piec, dodawanie, odejmowanie, mnozenie, dzielenie]

# ----------------------------------


def przetlumacz_slowo(slowo: str) -> str:
    for baza_symbolu in baza:
        for elem in baza_symbolu:
            if slowo == elem:
                return baza_symbolu[0]
    return ""


def wynik_operacji(l1: int, l2: int, oper: str) -> float:
    if oper == "+":
        return l1 + l2

# zadanie do wykonania po tym zadaniu: za pomocą AI uzupełnić bazy wyrazów do liczby 20

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
    return wynik_operacji(wynik, liczba, operacja)
    

dzialanie = "" # Tu przechowujemy działanie
tekst = input("Proszę wprowadzić działanie: ")

for slowo in tekst.split(" "):
    dzialanie += przetlumacz_slowo(slowo)

print(dzialanie)



["piętnaście", "plus", "czternaście"]