from math import sqrt
a = [x for x in range(1, 11)] # +
b = (x for x in range(11, 21)) # to stworzy Ci obiekt generatora, nie krotki! Trzeba zapisać to jako tuple(x for x in range(11, 21)) (+/-)
c = {x for x in range(21, 31)} # +

d = [sqrt(x) for x in a]
e = [sqrt(x) for x in b]
f = [sqrt(x) for x in c] # pierwiastki ok :)

print(d)
print(e)
print(f)

# (3.5 / 4.0), nieźle!