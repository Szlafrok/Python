a = [1, 2, 3]
b = [4, 5, 6] # +

c = a + b # ++

c.pop(5)
c.pop(2) # ++

c.remove(max(c))
c.remove(min(c)) #++

c.append(7) # +

c.sort() #+

d = c.copy() # +

d.reverse() # +

for i in range(len(a)): # ++
    c[i] += 1

for i in range(len(b)): # ++
    d[i] -= 1

print(c)
print(d) # +

# (3/3) Bezbłędnie!