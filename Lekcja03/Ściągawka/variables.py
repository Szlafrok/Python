# Ściągawka od Gigantów ;)

a = 10
b = 7
print(+a) # jednoargumentowy operator pozytywny, wynik 10 (tak naprawdę nic nie robi, istnieje tylko ze względu na kompletność)
print(a + b) # dwuargumentowy operator dodawania, wynik 17
print(-a) # jednoargumentowy operator negacji, wynik -10
print(a - b) # dwuargumentowy operator odejmowania, wynik 3
print(a * b) # operator mnożenia, wynik 70
print(a / b) # operator dzielenia, wynik 1.4285714285...
print(10 / 1) # operator dzielenia ZAWSZE zwraca wartość typu float, nawet gdy liczby są przez siebie podzielne, wynik 10.0
print(a % b) # operator dzielenia modulo, zwraca resztę z dzielenia pierwszej liczby przez drugą, wynik 3
print(a // b) # operator dzielenia całkowitoliczbowego, zwraca dzielenie pierwszej liczby przez drugą, zaokrąglonego do w dół do liczby całkowitej, wynik 1
print(3 ** 2) # operator potęgowania, wynik 9

a = 3
b = 4
# jak zwiększyć a o 2? Można tak:
a = a + 2
print(a) # a = 5
# a można szybciej
a += 2 # to samo co a = a + 2, tylko krócej
print(a) # a = 7
# to samo działa dla innych operatorów
a -= 5 # tak samo jak a = a - 5
print(a) # a = 2
b *= a # tak samo jak b = b * a
print(b) # b = 8
b /= 2 # tak samo jak b = b / 2
print(b) # b = 4.0
a %= 2 # to samo co a = a % 2
print(a) # a = 0
a = 7
a //= 2 # to samo co a = a // 2
print(a) # a = 3
b **= a # to samo co b = b ** a
print(b) # b = 64.0

print(True + True) # 2
print(False + True) # 1
print(False + False) # 0
print(3*True) # 3

# dodawanie stringów łączy je w jeden string (do stringa możemy dodawać tylko stringa)
print('Witaj ' + 'Gigancie!') # 'Witaj Gigancie!'
# możemy mnożyć string przez int (i na odwrót), tworzy wiele kopii naszego stringa
print(3 * 'test ') # 'test test test '
print('test ' * 3) # 'test test test '
tekst = 'tekst'
nowy_tekst = 'nowy '
nowy_tekst += tekst
print(nowy_tekst) # 'nowy tekst'

n = 10
m = 25
print('Wynik mnożenia', n, 'przez', m, 'to', n*m)
# ale jest to nieporęczne, lepiej użyć fstringów
print(f'Wynik dodawania {n} i {m} to {n+m}')

# MATEMATYCZNE
print(abs(-10)) # wartość bezwzględna z liczby, tutaj 10
print(max(1, 2, 3, 2, 8, -5)) # największa wartość ze wszystkich podanych jako argumenty, tutaj 8
print(min(1, 2, 3, 2, 8, -5)) # najmniejsza wartość ze wszystkich podanych jako argumenty, tutaj -5
print(round(3.5644)) # zaokrąglenie liczby, tutaj 4

# ITEROWALNE
print(len('Hello World!')) # zwraca długość obiektu - dla stringa jest to ilość znaków, tutaj 12
