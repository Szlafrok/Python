# int -> str
#### Liczba zostanie normalnie przepisana na tekst. Brak wyjątków.

# float -> str
#### Liczba zostanie normalnie przepisana na tekst. Brak wyjątków.

# str -> bool
#### Staje się True. Wyjątkiem jest podanie pustego stringa "", wówczas False.

# str -> int
#### Zamienia podaną liczbę na całkowitą. Wyrzuca błąd, jeżeli podana 
#### liczba jako tekst jest niepoprawna. Nie akceptuje liczb dziesiętnych.

# str - > float
#### Jak wyżej, ale akceptuje liczby dziesiętne

# bool -> float
#### True -> 1.0, False -> 0.0

# bool -> int
#### True -> 1, False -> 0

print(str(456))
print(type(str(45.6)))
print(bool("tekst"))
print(bool(""))

print(int("-12"))

print(int(True))

print(float(False))