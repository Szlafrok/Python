def add(a, b):
    return a + b

def if_palindrom(word):
    return word == word[::-1]

def divide(a, b):
    try:
        print(a/b)
    except:
        print("Dzielenie przez 0")

def sort_strings_by_length(list_of_strings):
    list_of_strings.sort(key=len)
    return list_of_strings

def calculate_mean(list_of_int):
    try:
        return -1 if not len(list_of_int) else sum(list_of_int) /len(list_of_int)
    except:
        return -2