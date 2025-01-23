zero = ["0", "zero", "zera", "zerem", "nic"]
jeden = ["1", "jeden", "jedynka", "jedynkę", "jedynki", "jednego"]
dwa = ["2", "dwa", "dwójka", "dwójkę", "dwójki", "dwóch"]
trzy = ["3", "trzy", "trójka", "trójkę", "trójki", "trzech"]
cztery = ["4", "cztery", "czwórka", "czwórkę", "czwórki", "czterech"]
piec = ["5", "pięć", "piątka", "piątkę", "piątki", "pięciu"]
szesc = ["6", "sześć", "szóstka", "szóstkę", "szóstki", "sześciu"]
siedem = ["7", "siedem", "siódemka", "siódemkę", "siódemki", "siedmiu"]
osiem = ["8", "osiem", "ósemka", "ósemkę", "ósemki", "ośmiu"]
dziewiec = ["9", "dziewięć", "dziewiątka", "dziewiątkę", "dziewiątki", "dziewięciu"]
dziesiec = ["10", "dziesięć", "dziesiątka", "dziesiątkę", "dziesiątki", "dziesięciu"]
jedenascie = ["11", "jedenaście", "jedenastka", "jedenastkę", "jedenastki", "jedenastu"]
dwanascie = ["12", "dwanaście", "dwunastka", "dwunastkę", "dwunastki", "dwunastu"]
trzynascie = ["13", "trzynaście", "trzynastka", "trzynastkę", "trzynastki", "trzynastu"]
czternascie = ["14", "czternaście", "czternastka", "czternastkę", "czternastki", "czternastu"]
pietnascie = ["15", "piętnaście", "piętnastka", "piętnastkę", "piętnastki", "piętnastu"]
szesnascie = ["16", "szesnaście", "szesnastka", "szesnastkę", "szesnastki", "szesnastu"]
siedemnascie = ["17", "siedemnaście", "siedemnastka", "siedemnastkę", "siedemnastki", "siedemnastu"]
osiemnascie = ["18", "osiemnaście", "osiemnastka", "osiemnastkę", "osiemnastki", "osiemnastu"]
dziewietnascie = ["19", "dziewiętnaście", "dziewiętnastka", "dziewiętnastkę", "dziewiętnastki", "dziewiętnastu"]
dwadziescia = ["20", "dwadzieścia", "dwudziestka", "dwudziestkę", "dwudziestki", "dwudziestu"]

dodawanie = ["+", "dodawanie", "dodać", "plus", "sumowanie", "więcej", "dodaj"]
odejmowanie = ["-", "odejmowanie", "odjąć", "minus", "różnica", "mniej", "odejmij"]
mnozenie = ["*", "mnożenie", "pomnożyć", "razy", "iloczyn", "przemnóż"]
dzielenie = ["/", "dzielenie", "podzielić", "iloraz", "podziel"]

baza = [zero, jeden, dwa, trzy, cztery, piec, szesc, siedem, osiem, 
        dziewiec, dziesiec, jedenascie, dwanascie, trzynascie, czternascie, 
        pietnascie, szesnascie, siedemnascie, osiemnascie, dziewietnascie, 
        dwadziescia, dodawanie, odejmowanie, mnozenie, dzielenie]

def przetlumacz_slowo(slowo: str) -> str:
    for baza_symbolu in baza:
        for symbol in baza_symbolu:
            if slowo == symbol:
                return baza_symbolu[0]
    return ""

def oblicz_wynik(l1: int, l2: int, oper: str) -> float:
    if oper == "+":
        return l1 + l2
    elif oper == "-":
        return l1 - l2
    elif oper == "*":
        return l1 * l2
    elif oper == "/":
        return l1 / l2
    return 0

def oblicz_z_tekstu(tekst: str) -> float:
    wynik = 0
    liczba = ""
    operacja = ""
    for znak in tekst:
        if znak.isdigit():
            liczba += znak
        else:
            operacja = znak
            wynik = int(liczba)
            liczba = ""

    if operacja == "": return int(liczba)
    return oblicz_wynik(wynik, int(liczba), operacja)


dzialanie = ""
tekst = input("Podaj treść działania: ")

for slowo in tekst.split(' '):
    #print(slowo)
    dzialanie += przetlumacz_slowo(slowo)

print(dzialanie)
print(oblicz_z_tekstu(dzialanie))