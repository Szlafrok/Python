from projekt import Stack
stack = Stack()
print("---------------------------")
def palindrom(s: str) -> bool:
    for c in s:
        stack.push(c)
    
    for c in s:
        if c != stack.pop():
            return False
        return True

print(palindrom("kajak"))
print(palindrom("halo"))
print(palindrom('radar'))

# Zadanie zrobione bezbłędnie i zgrabnie. Gratuluję :)

<<<<<<< HEAD
# (4/4)
=======
# ()
>>>>>>> d3bf0a4cad53c814661467a3e1fe74876e90de0b
