int() # liczba całkowita

float() # liczba dziesiętna / zmiennoprzecinkowa

bool() # wartość logczina True/False

str() # tekst

 

# int -> str

# liczba zamienia się na tekst ale nia da się jej dodać gdyż obie liczby stają jednolitym tekstem

'''a = 50

b = 3

c = (str(a)+str(b))

print(c)

'''

 

# float -> str

# liczba zamienia się na tekst ale nia da się jej dodać gdyż obie liczby stają jednolitym tekstem

 

'''a = 41.3

b = 5.8

c = (str(a)+str(b))

print(c)

'''

 

# str -> bool

# wyskakuje "True" gdy nawiasach znajduje się słowo, gdy nie ma w nich żadnego znaku wyskakuje "False"

 

'''a = "test"

print(bool(a))

'''

 

'''a = ""

print(bool(a))

'''

 

# str -> int

# wyskakuje błąd, oprócz sytuacji gdy tekst zawiera tylko liczby

#(błąd jest również, gdy liczba jest prawidłowa, ale niecałkowita)
 

'''a = "test"

print(int(a))

'''

 

'''a = "1"

print(int(a))

'''

 

# str - > float

#wyskakuje błąd, oprócz sytuacji gdy tekst zawiera tylko liczby

 

'''a = "test"

print(float(a))

'''

 

'''a = "1"

print(float(a))

'''

# bool -> float

# gdy zmienna wynosi "True" wynikiem będzie 1.0, ale w przypadku "False" wynik wynosi 0.0

 

'''a = False

print(float(a))

'''

 

'''a = True

print(float(a))

'''

 

# bool -> int

# gdy zmienna wynosi "True" wynikiem będzie 1, ale w przypadku "False" wynik wynosi 0

 

'''a = False

print(int(a))

'''

 

'''a = True

print(int(a))

'''