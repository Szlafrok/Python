def list_purge(arr: list):
    i = 0
    while True:
        if not isinstance(arr[i], (int, float)): # (int, float, bool)
            arr.pop(i)
        else:
            i += 1

        if i >= len(arr): # mógłbyś to zrobić w warunku while'a, byłoby nieco bardziej przejrzyście ;)
            break
    
    arr.sort()
    return arr

lista = [4, 6, 2.5, 1,2, "zabawny", "tekst", True, False, (0, 0)]
print(list_purge(lista))
# Ciekawostka: np. krotki można sortować między sobą, podobnie jak listy

# Formalnie dobrze, choć zwróć uwagę, że True i False również przechodzą Twój test i są sortowalne!

# (5/5)