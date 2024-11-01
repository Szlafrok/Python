# ------ ZADANIE PRZYKŁADOWE ------

# Proszę napisać matematyczny pomocnik do trójkątów, który:

# >>>>>> (a) Oceni, czy trójkąt o wskazanych bokach może powstać

# Trójkąt może powstać, jeżeli jego najdłuższy bok jest krótszy, niż suma długości jego pozostałych boków.

a = float(input("Podaj bok a: "))
b = float(input("Podaj bok b: "))
c = float(input("Podaj bok c: "))

# SPOSÓB 1 - SPRYTNY

zd_a_razem = a + b + c # Sumuję wszystkie boki trójkąta
zd_a_razem -= max(a, b, c) # Odejmuję największy bok - wówczas wartością tej zmiennej będzie suma pozostałych boków

if max(a, b, c) >= zd_a_razem: # Jeżeli najdłuższy z boków >= suma pozostałych dwóch boków, to
    print("Trójkąt o tych bokach nie istnieje!") # ten trójkąt nie ma prawa istnieć
else: # W przeciwnym razie
    print("Trójkąt prawidłowy :)") # Ten trójkąt jest prawidłowy!

# SPOSÓB 2 - SIŁOWY

if a >= b and a >= c: # Dla największego boku "a":
    if a >= b + c: 
        print("Błąd")
    else:
        print("OK")
elif b >= a and b >= c: # UWAGA! Stosuję ELIF. Mógłbym użyć IFa, ale jeżeli rozważę już jeden największy bok, to nie potrzebuję robić tego ponownie.
    if b >= a + c:
        print("Błąd!")
    else:
        print("OK")
else: # Jeżeli b nie jest największy i a nie jest największy, to c jest największy
    if c >= a + b:
        print("Błąd")
    else:
        print("OK")

# >>>>>> (b) Proszę określić, czy podany trójkąt jest równoboczny, równoramienny, czy różnoboczny. Można założyć, że jest prawidłowy.

if a == b or b == c or a == c:
    if a == b == c: # Jeżeli dwa boki są sobie równe to możemy już z pewnością powiedzieć, że jest równoramienny - ale może też być równoboczny.
        print("Równoboczny")
    else:
        print("Równoramienny")
else: # Jeżeli żadne dwa boki nie są sobie równe
    print("Różnoboczny")

# >>>>>> (c) Proszę określić, czy podany trójkąt jest prostokątny

# Zastosujemy dwa twierdzenia (uwaga, trochę matematyki):
# Dla a, b - krótszych boków trójkąta i c - najdłuższego boku trójkąta
# (1) Twierdzenie Pitagorasa: Jeżeli trójkąt jest prostokątny, to spełnione jest: a**2 + b**2 == c**2
# (2) Odwrotne twierdzenie Pitagorasa: Jeżeli zachodzi a**2 + b**2 == c**2, to trójkąt jest prostokątny

# W logice zachodzi zależność: Jeżeli ze zdania A wynika zdanie B oraz ze zdania B wynika zdanie A, to 
# zdanie A jest prawdziwe WTEDY I TYLKO WTEDY, gdy zdanie B jest prawdziwe. Oba są prawdą, lub oba są fałszem.

# Wnioskujemy, że trójkąt jest prostokątny WTEDY I TYLKO WTEDY, gdy a**2 + b**2 == c**2.

# Uwaga: Nie musimy sprawdzać, który bok jest najdłuższy. Ta równość może zajść i tak tylko w jednym z podanych przypadków.
warunek = False
if a**2 == b**2 + c**2 or b**2 == c**2 + a**2 or c**2 == a**2 + b**2:
    print("Trójkąt jest prostokątny")
else:
    print("Trójkąt jest ostrokątny")