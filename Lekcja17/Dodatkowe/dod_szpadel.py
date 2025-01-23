zero = ["0", "zero", "zera", "zerem", "nic"]
jeden = ["1", "jeden", "jedynka", "jedynkę", "jedynki", "jednego"]
dwa = ["2", "dwa", "dwójka", "dwójkę", "dwójki", "dwóch"]
trzy = ["3", "trzy", "trójka", "trójkę", "trójki", "trzech"]
cztery = ["4", "cztery", "czwórka", "czwórkę", "czwórki", "czterech"]
piec = ["5", "pięć", "piątka", "piątkę", "piątki", "pięciu"]
szesc = ["6", "sześć", "szóstka", "szóstce", "szóstką"]
siedem = ["7", "siedem", "siódemka", "siódemce", "siódemką"]
osiem = ["8", "osiem", "ósemka", "ósemce", "ósemką"]
dziewiec = ["9", "dziewięć", "dziewiątka", "dziewiątce", "dziewiątką"]
dziesiec = ["10", "dziesięć", "dziesiątka", "dziesiątce", "dziesiątką"]
jedenascie = ["11", "jedenaście", "jedenastka", "jedenastce", "jedenastką"]
dwanascie = ["12", "dwanaście", "dwunastka", "dwunastce", "dwunastką"]
trzynascie = ["13", "trzynaście", "trzynastka", "trzynastce", "trzynastką"]
czternascie = ["14", "czternaście", "czternastka", "czternastce", "czternastką"]
pietnascie = ["15", "piętnaście", "piętnastka", "piętnastce", "piętnastką"]
szesnascie = ["16", "szesnaście", "szesnastka", "szesnastce", "szesnastką"]
siedemnascie = ["17", "siedemnaście", "siedemnasta", "siedemnastej", "siedemnastką"]
osiemnascie = ["18", "osiemnaście", "osiemnasta", "osiemnastej", "osiemnastką"]
dziewietnascie = ["19", "dziewiętnaście", "dziewiętnasta", "dziewiętnastej", "dziewiętnastką"]
dwadziescia = ["20", "dwadzieścia", "dwudziestka", "dwudziestce", "dwudziestką"]


dodawanie = ["+", "dodawanie", "dodać", "plus", "sumowanie", "więcej", "dodaj"]
odejmowanie = ["-", "odejmowanie", "odjąć", "minus", "różnica", "mniej", "odejmij"]
mnozenie = ["*", "mnożenie", "pomnożyć", "razy", "iloczyn", "przemnóż"]
dzielenie = ["/", "dzielenie", "podzielić", "iloraz", "podziel"]

baza = [zero, jeden, dwa, trzy, cztery, piec,
        szesc, siedem, osiem, dziewiec, dziesiec,
        jedenascie, dwanascie, trzynascie, czternascie, pietnascie,
        szesnascie, siedemnascie, osiemnascie, dziewietnascie, dwadziescia,
        dodawanie, odejmowanie, mnozenie, dzielenie]

# ------------------------------------------


def przetlumacz_slowo(slowo: str) -> str:
    for baza_symbolu in baza:
        for elem in baza_symbolu:
            if elem == slowo:
                return baza_symbolu[0]
    return ""

def wynik_operacji(li: int, l2: int, oper: str) -> float:
    if oper == "+":
        return li + l2
    elif oper == "-":
        return li - l2
    elif oper == "*":
        return li * l2
    elif oper == "/":
        return li / l2

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
    print(wynik_operacji(wynik, liczba, operacja))

while True:
    dzialanie = "" # Tutaj przechowujemy nasze działanie
    tekst = input("Proszę wprowadzić działanie: ")

    if tekst == "Koniec":
        print("Zamykanie aplikacji ...")
        exit()

    for slowo in tekst.split(" "):
        dzialanie += przetlumacz_slowo(slowo)
    print(dzialanie)
    oblicz_z_tekstu(dzialanie)


# Oba zadania zaliczone :)

# +4 pkt