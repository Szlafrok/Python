lista = [0, 2, 4, 6, 8]

lista = []
for i in range(5000):
    lista.append(i)

#print(lista)

# [WYRAŻENIE dla ELEMENTU z OBIEKTU jeżeli spełniony WARUNEK]

# [EXPR for ELEM in ITER if COND]

from pprint import pprint

"""
WAŻNE: JAK TO WIDZI PYTHON?
1. Python bierze ITERATOR oraz OBIEKT, po którym będziemy iterować
2. Python sprawdza, czy WARUNEK jest spełniony przez wybrany element z obiektu
3. Jeżeli tak, Python wstawia wartość wyrażenia dla tego elementu do listy (np. x - 5 jak poniżej)

"""



lista = [x - 5 for x in range(10) if x > 5]
print(lista)

lista = [x**2 for x in range(1, 21) if x % 2 == 0]
print(lista)


kwadraty = tuple(i**2 for i in range(10)) # samo wyrażenie listowe w nawiasach daje nam generator, musimy wstawić go do tuple() aby uzyskać krotkę
print(f" krotka) {kwadraty}")

kwadraty = {i**2 for i in range(10)}
print(f"  zbiór) {kwadraty}")

kwadraty = {i:i**2 for i in range(10)}
print(kwadraty)

### Zadanie 4

sequence = "HELLO@123world!456"

lista = [c for c in sequence if not(c.isalpha())] # c.isalpha() -> True jeżeli c zawiera tylko i wyłącznie litery (tu: 1 znak, czyli max. 1 litera)

sequence = "".join(lista)
print(sequence)




try: # TEEF: Try, Except, Else, Finally
    # Fragment kodu który sprawdzamy pod kątem wyjątków
    print(5 / 0)
except Exception as e:
    # Wykryto wyjątek
    print(e)
else:
    # Nie wykryto wyjątku
    print("OK")
finally:
    # Wykonuje się w następnej kolejności, niezależnie od obecności wyjątków
    print("pies spawacz")


def parzyste(a, b):
    try: 
        if a % 2 == 1 or b % 2 == 1:
            raise Exception("Podane argumenty nie są parzyste!") # Podnosimy błąd samodzielnie!
    except Exception as e:
        print(e) # Printujemy opis błędu
        return None

    return a + b
    
print(parzyste(5, 10))

print("----------------------------")

def podziel(zdanie):
    try:
        if not zdanie[0].isupper():
            raise Exception("Zdanie musie zaczynać się wielką literą!")
        elif not zdanie[-1] in ["!", "?", "."]: # badamy ostatni znak zdania
            raise Exception("Zdanie musi kończyć się poprawnym znakiem interpunkcyjnym")
    except Exception as e:
        print(e)
    else:
        print(zdanie.split(" ")) # Dzieli stringa, argument tej metody jest podzielnikiem (czyli tu dzielimy wg spacji)
    finally:
        print("Koniec programu!")

podziel("Ala ma kota!")
podziel("hesia ma kebaba!")