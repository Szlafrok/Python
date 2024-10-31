warunek = 5 > 0

if warunek:
    print("OK! :D")
elif warunek:
    pass
elif warunek:
    pass
else:
    pass


if 5 == 5:
    print(1)
    print(2)
    print(3)
else:
    print(4)

if "kebab" == 'pizza' and not len('sphagetti') == 9 and 'sushi' == "su" + "shi":
    print("amogus")

if "kebab" == 'pizza' and (not len('sphagetti')) == 9 and 'sushi' == "su" + "shi":
    print("amogus")

x = 5 * 5 * 5
x = (5 * 5) * 5

if 5 == 0 and 1 // 0 == 1:
    print("Było blisko")

if 5 == 5 or 1 % 0 == 1:
    print("podlasie")

if (1 == 0 and 1/0) or 0 or 1//0:
    print("HAHAHA")

# # bool(10) == True

if "Pol" in "Polska":
    print("*daje kciuka w górę*")

if "a" in "waka waka eh eh it is time for AFRICA":
    print("jupi")

if "A" in "waka waka eh eh it is time for AFRICA":
    print("jupi")

piosenka = "waka waka eh eh it is time for AFRICA"

if "w" in piosenka or "W" in piosenka:
    print("it is time for AZKABAN")

if "AFRICA" in piosenka:
    print("Senegal wbił nam gola")


# -------- ZADANIE SAMODZIELNE 1 ---------
# Proszę sprawdzić, czy podany przez użytkownika tekst zawiera jeden
# z ciągów znaków: "abc", "tygrysek", "marchewka"

# Proszę sprawdzić to w jednym IFie

ciag = input("Proszę podać ciąg znaków: ")

if "abc" in ciag or "tygrysek" in ciag or "marchewka" in ciag:
    print("Zawiera przynajmniej jedno słowo z podanych")

if "abc" in ciag and "tygrysek" in ciag and "marchewka" in ciag:
    print("Zawiera każde słowo z podanych")

# Proszę sprawdzić, czy tekst zawiera WSZYSTKIE TRZY z tych ciągów znaków.
# Proszę się zastanowić jaka jest MINIMALNA długość ciągu zawierającego wszystkie te słowa. - odp. 19: ciąg "tygrysekmarchewkabc"

# ----------- ZADANIE SAMODZIELNE 2 ----------------

LOGIN = "missclick"
HASLO = "kaczkawizardWOLOLO"

wpr_login = input("Podaj login: ")
wpr_haslo = input("Podaj hasło: ")

if wpr_login == LOGIN and wpr_haslo == HASLO:
    print("Gratuluje, zostajesz Miss Wenezueli")
elif wpr_haslo != HASLO: #*
    print("Złe hasło")
else:
    print("nah, i'd win")

# Proszę napisać program, który poprosi użytkownika o dane logowania, a następnie
# zweryfikuje poprawność logowania i określi, czy dane są poprawne, czy nie.


# Wojtek - krotki
print (("abc", "marchewka", "tygrysek") in ["element", "a", "abc", ("abc", "marchewka", "tygrysek"), "tygrysek", "krzysio", "marcinek"])
["abc", "marchewka", "tygrysek"][2] = "ą" # działa

try: 
    ("abc", "marchewka", "tygrysek")[2] = "ą" # działa
except:
    print("Zostanie wyrzucony błąd")

# Co się tyczy try / except: Podczas naszego omawiania tej konstrukcji nie
# wzięliśmy pod uwagę, że korzystając z "try" MUSI pojawić się "except" -
# program musi wiedzieć co zrobić, jeśli otrzyma błąd.