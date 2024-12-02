def arytm(ciag):
    if len(ciag) < 1:
        print("Ciąg musi posiadać przynajminej jeden element")
        return False
        return print("Ciąg musi posiadać przynajminej jeden element")
    elif len(ciag) < 2:
        return True
        return print(True) 
    przeskok = ciag[1] - ciag[0]
    for i in range(len(ciag) - 1):
        if not przeskok == ciag[i + 1] - ciag[i]:
            return False
            return print(False)
    return True
    return print(True)

print(arytm([3,1,1]))

# Spoko, natomiast miałeś zwrócić konkretnie wartość :P
# Wstawiając printa do instrukcji return, zwracasz None,
# ponieważ print() zwraca None. Zapisałem poprawki w kodzie

# Nie usunąłem oryginalnych returnów, ponieważ się nie wykonają,
# a Ty będziesz miał porównanie. Stare returny nie wykonają się,
# ponieważ funkcja zwróci wartość i zakończy się, zanim do nich dotrze.

# Logicznie jednak zadanie jest zrobione bardzo ładnie, a zwracania jeszcze
# nie robiliśmy, więc się nie przyczepię. Gratuluję dobrego rozwiązania B)

# (+2 / 2)