lista = [0, 2, 4, 6, 8]

lista = []
for i in range(5000):
    lista.append(i)

#print(lista)

# [WYRAŻENIE dla ELEMENTU z OBIEKTU jeżeli spełniony WARUNEK]

# [EXPR for ELEM in ITER if COND]

from pprint import pprint


lista = [x - 5 for x in range(10) if x > 5]
print(lista)

lista = [x**2 for x in range(1, 21) if x % 2 == 0]
print(lista)


kwadraty = tuple(i**2 for i in range(10))
print(f" krotka) {kwadraty}")

kwadraty = {i**2 for i in range(10)}
print(f"  zbiór) {kwadraty}")

kwadraty = {i:i**2 for i in range(10)}
print(kwadraty)

### Zadanie 4

sequence = "HELLO@123world!456"

lista = [c for c in sequence if not(c.isalpha())]

sequence = "".join(lista)
print(sequence)




try: # TEEF
    # Fragment kodu który sprawdzamy pod kątem wyjątków
    print(5 / 0)
except Exception as e:
    # Wykryto wyjątek
    print(e)
else:
    # Nie wykryto wyjątku
    print("OK")
finally:
    # Wykonuje się w następnej kolejności
    print("pies spawacz")


def parzyste(a, b):
    try:
        if a % 2 == 1 or b % 2 == 1:
            raise Exception("Podane argumenty nie są parzyste!")
    except Exception as e:
        print(e)
        return None

    return a + b
    
print(parzyste(5, 10))

print("----------------------------")

def podziel(zdanie):
    try:
        if not zdanie[0].isupper():
            raise Exception("Zdanie musie zaczynać się wielką literą!")
        elif not zdanie[-1] in ["!", "?", "."]:
            raise Exception("Zdanie musi kończyć się poprawnym znakiem interpunkcyjnym")
    except Exception as e:
        print(e)
    else:
        print(zdanie.split(" "))
    finally:
        print("Koniec programu!")

podziel("Ala ma kota!")
podziel("hesia ma kebaba!")