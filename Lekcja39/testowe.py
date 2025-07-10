import numpy as np

arr = np.array([[-1, -2, -3], [4, 5, 6], [7, 8, 10]])

def print_array(arr):
    print(f"Tablica:\n{arr}")
    print(f"Pierwszy element tablicy: {arr[0]}")
    print(f"Pierwszy zagnieżdżony element: {arr[0][0]}")
    print(f"Typ obiektu: {type(arr)}")
    print(f"Rozmiar tablicy: {arr.shape}")


print_array(arr)