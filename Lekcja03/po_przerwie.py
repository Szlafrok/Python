
x = 0

x += 1 # dodawanie
x = x + 1

x -= 1
x = x - 1 # odejmowanie

x *= 2
x = x * 2 # mnożenie

x **= 3 #potęgowanie
x = x**3

x /= 2
x = x / 2 # dzielenie - ZMIENIA TYP NA FLOAT

x = 5

x //= 2
x = x//2 # dzielenie całkowitoliczbowe, ZWRACA INTA LUB FLOATA - NIE ZMIENIA TYPU

x = 5
x = int(x/2) # działa podobnie do dzielenia całkowitego, ALE ZWRACA ZAWSZE INTA

x = 136
x %= 10
x = x % 10



# Operacje na bool'ach

x = True + True + True + False # 3
x *= False # 3 * 0 == 0

#x = True // False # dzielenie przez 0 --> błąd
# Operacje na stringach

print("Witaj" + "Gigancie!")
print(3 * "Hip, hip! Hurra! ")

# FSTRING

imie = "Piotrek"
wiek = 20
obecny_rok = 2024
print("Cześć, jestem", imie, "i mam", wiek, "lat")

print(f"Jakiś tam tekst, a zmienne, które chcemy wstawić, dajemy w nawiasy klamrowe.")
print(f"O właśnie w taki sposób: {wiek}. A tu kolejna zmienna: {imie}")

print(f"Urodziłem się w roku {obecny_rok - wiek}")

print(f"Urodziłem się w roku {float(obecny_rok - wiek)}")
print(f"Urodziłem się w roku {bool(obecny_rok - wiek)}")

# FUNKCJE WBUDOWANE

print("Drukuje tekst w terminalu")
#input("Pyta się o dane i wkleja je do np. podanej zmiennej")

x = abs(-10) # to samo co |-10| - wartość bezwzględna, usuwa minus z liczby.
print(f"Przykład abs(): {x}")

x = min(2, 5, 7, -1, 10) # Zwraca najmniejszą liczbę z podanych
print(f"Przykład min(): {x}")

x = max(2, 5, 7, -1, 10) # Zwraca największą liczbę z podanych
print(f"Przykład max(): {x}")

x = round(4.5) # Zaokrągla podaną liczbę do najbliższej liczby całkowitej
print(f"Przykład round(): {x}")

x = len("abcdef") # Podaje długość ciągu znaków
print(f"Przykład len(): {x}")
