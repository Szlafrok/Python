from math import sqrt

def nwd(a: int, b: int) -> int: # (2/2)
    while b != 0:
        a, b = b, a % b  # Algorytm Euklidesa // B)
    return a

def nww(a: int, b: int) -> int: # (2/2)
    return abs(a * b) // nwd(a, b)  # Wzór na NWW // Sprytnie, nie pamiętałem tego wzoru!

print(nwd(12, 15))  #  3
print(nww(12, 15))  #  60

# Bardzo zwięźle zrobiony kod, jednocześnie zrozumiały i czytelny. Brawo!