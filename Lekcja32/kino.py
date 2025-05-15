"""
Proszę utworzyć klasę Customer, która w konstruktorze będzie przyjmowała do zmiennych
self.name i self.order odpowiednio imię i zamówienie klienta.

Proszę utworzyć klasę CinemaQueue, która:
- w konstruktorze utworzy kolejkę do zmiennej self.queue
- w metodzie is_empty zwróci informację True/False, zależnie czy kolejka jest pusta
- w metodzie add_customer doda klienta do kolejki. Metoda powinna przyjmować klienta 
jako argument.
- w metodzie remove_customer, o ile kolejka nie jest pusta, zwróci pierwszego klienta 
w kolejce i usunie go z tej kolejki
- w metodzie next_customer_order, o ile kolejka nie jest pusta, podejrzy zamówienie 
pierwszego klienta i zwróci je

"""
from pokazowe import *

class Customer():
    def __init__(self, name, order):
        self.name = name
        self.order = order

class CinemaQueue():
    def __init__(self):
        self.queue = Queue()

    def is_empty(self):
        return self.queue.is_empty()
    
    def add_customer(self, customer):
        self.queue.enqueue(customer)

    def remove_customer(self):
        if not self.is_empty():
            customer = self.queue.dequeue()
            print(customer.name, customer.order)
            return customer
        
    def next_customer_order(self):
        if not self.is_empty():
            next_customer = self.queue.peek()
            return next_customer.order
        
        
    