def min_val(L: list) -> list:
    min_3 = []
    for _ in range(3):
        min_3.append(float(min(L)))
        L.remove(float(min(L)))
    return min_3

def max_val(L: list) -> list:
    max_3 = []
    for _ in range(3):
        max_3.append(float(max(L)))
        L.remove(float(max(L)))
    return max_3

e = [7, 9, 85, 3, 5, 44]

print(max_val(e))
print(min_val(e))

# Po co robisz z tego floaty?

# Poza tym sprytne podejście :)

# 3/3 + 1 za dodatkowe -> 4 pkt :)