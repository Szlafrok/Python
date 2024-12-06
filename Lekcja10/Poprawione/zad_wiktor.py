#zadanie 1
def prostokat(a, b):
    pole = a * b
    print(pole)

# Przykład użycia:
prostokat(5, 3)  # Wynik: 15

# (1/1)

#zadanie 2

def join(lacznik, teksty):
    wynik = lacznik.join(teksty)
    print(wynik)

# Przykład użycia:
join("/", ["bardzo", "lubię", "ciastka"])  # Wynik: "bardzo/lubię/ciastka"
join("-", ["i have", "your food", "sir"])  # Wynik: "i have-your food-sir"
join("%", ["pojedynczy element"])          # Wynik: "pojedynczy element"

# (3/3)

# zadanie 3

def info(imie, wiek, wzrost):
    print(f"Hej, jestem {imie}, mam {wiek} lat i {wzrost*100:.0f}cm wzrostu")

# Przykład użycia:
info("Piotrek", 20, 1.80)  # Wynik: "Hej, jestem Piotrek, mam 20 lat i 180cm wzrostu"

# (2/2)

# Należy pamiętać, że wzrost jest podawany w metrach, ale wynik powinien być w centymetrach,
#  dlatego w kodzie zamieniamy jednostki. // Tak jest B) (+0.5 pkt)


# Bezbłędnie, brawo!