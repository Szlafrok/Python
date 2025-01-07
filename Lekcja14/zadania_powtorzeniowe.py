def trojkat(a: float, h: float) -> float:
    pole = a*h/2
    return pole

p = trojkat(5, 10)
print(f"Pole trójkąta wynosi {p * 2}")


from random import randint

from random import randint


def losowe(n):
    powtorzenia = [0] * 30
    for _ in range(n):
        powtorzenia[randint(1, 30) - 1] += 1

    najw = max(powtorzenia)
    
    print(f"Najczęściej występująca liczba to {powtorzenia.index(najw) + 1}. Występuje {najw} razy")

losowe(100)