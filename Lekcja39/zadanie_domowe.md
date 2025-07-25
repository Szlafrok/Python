## Tablice, kompilacje, interpretacje (5p)
### a) (3p)
Metoda `arr.transpose()` w NumPy zamienia miejscami osie tablicy. Najprościej: dla macierzy 2D zamienia wiersze z kolumnami.

Przykład:
```py
import numpy as np
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print("Oryginalna:")
print(arr)
print("\nTranspozycja:")
print(arr.transpose())

# Wyniki:       
# Oryginalna:   Transpozycja:
# [[1 2 3]      [[1 4]]
#  [4 5 6]]      [2 5]
#                [3 6]
```
Korzystając z tej funkcji, proszę napisać funkcję, która przyjmie jako argument tablicę kwadratową (o wymiarach n*n) NumPy, a następnie zwróci True, jeżeli ta tablica jest symetryczna względem przekątnej idącej od elementu (0, 0) do (n-1, n-1).


### b) (2p)
Proszę obejrzeć ten [filmik](https://youtu.be/e2cMJmK2Gyg) - przedstawia on edycję kodu w Scratchu. Proszę na jego podstawie określić - kod Scratcha jest **interpretowany** czy **kompilowany** i dlaczego?