def unikaty(arr: list):
    i = 0
    while True:
        if arr[i] in arr[:i]:
            arr.pop(i)
        else:
            i += 1
        
        if i >= len(arr): # podobna uwaga jak w zad 1 z L35 ;)
            break
    return arr

arr = [9, 6, 7, 5, 4, 9, 4, 4, 2, 3, 1, 2]
print(unikaty(arr))

# (3/3) +1 pkt za zachowanie kolejności. Nieźle :)