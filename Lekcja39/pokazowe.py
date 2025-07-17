import numpy as np
from numpy import random

arr = np.array([[-1, 2, -3], [4, 5, 6], [7, 8, 10]])

def print_array(arr):
    print(f"Tablica:\n{arr}")
    print(f"Pierwszy element tablicy: {arr[0]}")
    print(f"Pierwszy zagnieżdżony element: {arr[0][0]}")
    print(f"Typ obiektu: {type(arr)}")
    print(f"Rozmiar tablicy: {arr.shape}")

print_array(arr)

def shapeshifter(arr):
    print(arr.reshape(9,1))
    print(arr.reshape(1,9))
    print(arr.reshape(3,3))
    print(arr.reshape(1,-1))
    print(arr.reshape(-1,3))
    print("----------------")
    newarr = np.array_split(arr, 3)
    for a in newarr:
        print(a)

shapeshifter(arr)

def data_format():
    arr = np.array([[1.1, 2.2, 3.4], [5.6, 6.7, 7.8], [9.0, 10.1, 11.2]], dtype = "U") # string
    print(f"Format 1) \n{arr}")

    arr = np.array([[1.1, 2.2, 3.4], [5.6, 6.7, 7.8], [9.0, 10.1, 11.2]], dtype = "i") # int
    print(f"Format 2) \n{arr}")

    try:
        arr = np.array([[1.1, 2.2, 3.4], [5.6, "ratatuj", 7.8], [9.0, 10.1, 11.2]], dtype = "f") # float
        print(f"Format 3) \n{arr}")
    except Exception as e:
        print(e)
    
    arr = np.array([1, 2, 3, 4], dtype="f")
    print(arr)
    print(int(arr[0]))

data_format()

def sorted_array(arr):
    print(f"Tablica posorotwania: \n{np.sort(arr)}")

arr = np.array([[1, 2, 3], [4, 2, 2], [1, 3, 5]])
sorted_array(arr)


def generate_random_numbers():
    for i in range(10):
        print(random.randint(100))
    for i in range(10):
        print(random.rand())

generate_random_numbers()

def pick_random_numbers():
    print(random.rand(3, 4))
    print(random.choice([3, 5, 7, 9]))
    print(random.choice([3, 5, 7, 9], size=(3, 5)))

pick_random_numbers()

arr = np.array([1, 2, 3, 4, 5])
def shuffle_array(arr):
    print(f"[shuffle] Przed: {arr}")
    print(f"Tasowana: {random.shuffle(arr)}")
    print(f"Po tasowaniu: {arr}")

    print("-------------------")

    print(f"[permutation] Przed: {arr}")
    print(f"Tasowana: {random.permutation(arr)}")
    print(f"Po tasowaniu: {arr}")

shuffle_array(arr)



arr = np.array([1, 2, 3, 4, 5, 6])
print("-----------------")
print(f"Tablica: {arr}")

print(np.sum(arr))
print(np.min(arr))
print(np.max(arr))

# Średnia tablicy [1 2 3 4 5 6] wynosi 3.5
# np.mean(arr)

print(f"Średnia tablicy {arr} wynosi {np.mean(arr)}")