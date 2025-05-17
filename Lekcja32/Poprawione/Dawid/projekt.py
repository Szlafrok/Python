class Stack():
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None
    def peek (self):
        if not self.is_empty():
            return self.stack[-1]
        return None
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
stack = Stack()    

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())
print(stack.pop())

stack.push(5)
stack.push(6)
print(stack.pop())
print(stack.peek())
print(stack.pop())
print("--------------------------------------------")
class Queue():
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, item):
        self.queue.append(item)

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())
print(queue.dequeue())
print(queue.is_empty())
print(queue.dequeue())
print(queue.dequeue())
print("--------------------------------------------")









