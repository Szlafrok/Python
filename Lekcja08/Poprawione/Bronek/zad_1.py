# a) 0, 1, 2, 3, 4, 5, 6, 7
print(list(range(8))) # OK

# b) 5, 6, 7, 8, 9, 10, 11, 12
print(list(range(5, 13))) # OK

# c) -5, -4, -3
print(list(range(-5, -2))) # Brakuje Ci podania kroku! Trzeba dodać argument -1: range(-5, -2, -1)

# d) 2, 4, 6, 8, 10
print(list(range(2, 11, 2))) # OK

# e) 0, 5, 10, 15
print(list(range(0, 16, 5))) # OK

# f) -9, -6, -3, 0, 3
print(list(range(-9, 4, 3))) # OK

# g) -100, -25, 50, 125
print([-100, -25, 50, 125]) # O ty spryciarzu XD Niestety nie, trzeba było zrobić krok co 75, czyli range(-100, 126, 75)

# h) 5
print([5]) # Jak wyżej - trzeba było użyć range: range(5, 6)

# i) 1000, 999, 998, 997
print(list(range(1000, 996, -1))) # Tu już ładnie zrobiony krok ;) Jest OK

# (3.25 / 4.00) - liczę do dodatkowych!