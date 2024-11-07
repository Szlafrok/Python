#a)
PIN = int(2077) # Niepotrzebnie robisz inta z inta
HASŁO = "MalyGigantPl" # unikaj polskich znaków, zauważ po kolorze, że VS Code nie traktuje tego jako stałą!

odpp = int(input("Podaj czterocyfrowy numer PIN:")) # oki :>
odph = input("Podaj hasło:")

if PIN == odpp and HASŁO == odph: # Wg zadania trzeba było najpierw sprawdzić PIN i dopiero jeżeli się zgadza, pytać o hasło - błąd nieuwagi :P
    print("Pomyślnie zalogowano :>")
else:
    print("Odmowa dostępu.")

# 2.5 / 3.0



# ---------------------------

#b) PIN musi być w tym kodzie w formacie int ponieważ jest 
# napisane w nawiasach przed którymi stoi int. Gdyby zrobić
# w stringu trzeba by było zrobić tak jak hasło ;>.

# Niestety nie o to chodzi, korzystanie ze stringów przy kodzie PIN w tej
# sytuacji ma większą odporność - wówczas możliwe jest zapisanie PINu zaczynającego
# się od zer, np. 00015

# Tym razem niestety bez premii za gwiazdkę :[