'''
lista = [1,2,3,4,5,6,7,8,9,10]

kwadraty = [i**2 for i in lista]
print(kwadraty)

kwadraty = tuple(i**2 for i in lista)
print(kwadraty)

kwadraty = {i**2 for i in lista}
print(kwadraty)

kwadraty = {i:i**2 for i in lista}
print(kwadraty)



podwojenia = [2*i for i in range(10)]
print(podwojenia)


kwadraty = [i**2 for i in lista if i%2 == 0]
print(kwadraty)


panstwa = ["Polska", "Niemcy", "Francja", "Hiszpania"]
stolice = ["Warszawa", "Berlin", "Paryz", "Madryt"]

informacje = [f"{stolica} to stolica kraju: {panstwo}" for panstwo,stolica in zip(panstwa, stolice)]
for info in informacje:
    print(info)

#Utworz liste zawierajaca tylko slowa bedace palindromami
slowa = ["ala", "kot", "pies", "kamilslimak", "zebra", "madam", "Adam"]
palindromy = [slowo for slowo in slowa if slowo == slowo[::-1]]
print(palindromy)

#Utworz liste zawierajaca tylko krotki, ktore moglyby zawierac dlugosci bokow trojkata
trojkaty = [(1, 3, 5), (2, 2, 3), (3, 1, 8), (3, 4, 5)]
poprawne_trojkaty = [trojkat for trojkat in trojkaty if 2 * max(trojkat) < sum(trojkat)]
print(poprawne_trojkaty)

#Na podstawie listy temperatur w stopniach Fahrenhaita wygeneruj liste z stopniami Celcjusza
stopnie_fahrenheit = [32, 68, 104, 140]
stopnie_celcius = [(temp - 32) * 5/9 for temp in stopnie_fahrenheit]
print(stopnie_celcius)

#Z podanego ciagu znakow usun wszystkie znaki niebedace cyframi lub literami
string = "hello@123world!456"
alphabets = [char for char in string if char.isalpha()]
print(''.join(alphabets))
'''
#Wyjątki
def dzielenie_i_mnozenie(a,b):
    try:
        a/b
    except Exception as e:
        print(e)
    else:
        print(f"Wynik dzielenia {a} / {b} = {a/b}")
    finally:
        print(f"Wynik mnozenia {a} * {b} = {a*b}")

dzielenie_i_mnozenie(5,2)
dzielenie_i_mnozenie(0,2)
dzielenie_i_mnozenie(5,0)


def dodawanie(a,b):
    try:
        a+b
    except Exception as e:
        print("Typy nie sa zgodne")
    else:
        print(f"Wynik dodawania {a} + {b} = {a+b}")

dodawanie("5",5)
dodawanie(5,5)
dodawanie("5","5")

def parzyste(a,b):
    try:
        if a % 2 == 1 or b % 2 == 1:
            raise Exception ("To nie sa liczby parzyste")
    except Exception as e:
        print(e)
    else:
        print(a+b)
parzyste(1,3)
parzyste(2,4)


def zdanie_na_wyrazy(zdanie):
    try:
        if not zdanie[0].isupper():
            raise Exception ("Zdanie musi zaczynac sie wielka litera")
        elif zdanie[-1] not in [".","?","!"]:
            raise Exception ("Zdanie musi konczyc sie znakiem interpunkcyjnym")
    except Exception as e:
        print(e)
    else:
        print(zdanie.split(" "))
    finally:
        print("Koniec programu")

zdanie_na_wyrazy("Ala ma kota.")