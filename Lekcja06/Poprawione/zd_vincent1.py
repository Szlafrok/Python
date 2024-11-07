PIN = "1545"
HASŁO = "bigos"

wprowadzony_pin = input("Wprowadź pin: ")

if wprowadzony_pin == PIN:
    wprowadzone_hasło = input("Wprowadź hasło: ")
    if wprowadzone_hasło == HASŁO: # uważaj na polskie znaki w nazwach! Program nie traktuje tego jako stałą tylko zmienną.
        print("Logowanie się powiodło.")
    else:
        print("Złe hasło")
else:
    print("Zły pin.")

# Bardzo dobrze! 3.0 / 3.0

'''hasło należy przechowywać w formacie tekstu, ponieważ gdy przechowamy je w formacie liczby zawsze będzie wyrzucać "zły pin",
jeżeli nie wstawimy inta przy inpucie pinu gdy to zrobimy i wpiszemy coś innego niż liczbę jako pin program nie wyżuci "zły pin" tylko error.'''

# Dobra opcja i ok uzasadnienie, choć nie o tym myślałem, zadając to pytanie.
# Korzystanie z tekstu umożliwia tworzenie pinów zaczynających się od 0, np. 0015

# Bonus: + 0.5 pkt / 0.5