zmienna = 5
tekst = "abrakadabra"

a = 1
b = 2
c = 3

print(a + b) # 3
print(b - a) # 1
print(b * c) # 6
print(c / b) # 1.5
print(c // b) # 1
print(c % b) # 1
print(c ** b) # 9

tekst = "5"
zmienna = int(tekst)

int() # liczba całkowita
float() # liczba zmiennoprzecinkowa
str() # tekst
bool() # True / False

print(b > c) # False
print(c > b) # True
print(c >= b) # True
print(c == b) # False
print(c != b) # True

print(not c == b) # True
print(not c != b) # False

# Operator logiczny "and" spaja co najmniej 2 warunki i jest spełniony wtedy i tylko wtedy, gdy WSZYSTKIE złączone nim warunki są spełnione.
# Operator logiczny "or" spaja co najmniej 2 warunki i jest spełniony wtedy i tylko wtedy, gdy PRZYNAJMNIEJ JEDEN spośród złączonych nim warunków jest spełniony.