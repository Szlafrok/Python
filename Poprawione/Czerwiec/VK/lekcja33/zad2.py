def find_max(arr):
    n = len(arr)
    res = arr[0]
    for i in range(1, n):
        if arr[i] > res:
            res = arr[i]
    return res

def selection_sort(arr):
    n = len(arr)
    low = 0
    high = n - 1

    while low < high:
        max_liczba = find_max(arr[low:high + 1])
        index_max_liczba = arr[low:high + 1].index(max_liczba) + low 
        
        arr[index_max_liczba], arr[high] = arr[high], arr[index_max_liczba]
        high -= 1
    return arr

arr = [5, 6, 10, 3, 2, 1, 8, 1, 5, 7]
print(selection_sort(arr))

# (4/4), bezbłędnie zrobione, ale zauważyłem tu pewną ciekawą rzecz w linijce 16 w związku z Twoim rozwiązaniem - 
# chciałbym ją z Tobą krótko omówić przy okazji następnych zajęć, dobrze? :)