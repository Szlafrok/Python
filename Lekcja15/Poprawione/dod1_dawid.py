VALUES = "0123456789abcdef"

def deci(num: str, syst: int) -> int:
    result = 0
    power = len(num) - 1
    for i in num:
        value = VALUES.index(i)
        result += value * (syst ** power)
        power -= 1
    return result

#przykład
wynik = deci("1100", 3)
print(f"zadanie dodatkowe 1: wynik: {wynik}")

# Bardzo ładnie i zgrabnie!
# (+ 3.0 / 3.0)