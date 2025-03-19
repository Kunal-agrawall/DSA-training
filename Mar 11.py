# # Stack

# class Stack:
#     def __init__(self):
#         self.stack = []

#     def push(self, item):
#         self.stack.append(item)
    
#     def pop(self):
#         if not self.is_empty():
#             return self.stack.pop()
#         return "Stack is empty"
    
#     def peek(self):
#         if not self.is_empty():
#             return self.stack[-1]
#         return "Stack is empty"
    
#     def is_empty(self):
#         return len(self.stack) == 0
    
#     def size(self):
#         return len(self.stack)


# s = Stack()
# s.push(10)
# s.push(20)
# s.push(30)
# s.push(60)
# s.push(90)
# s.push(100)

# print(s.pop())  
# print(s.peek())  
# print(s.size()) 

# # /////////////////////////////////////////////////////////////////////

# Using list

# stack = []

# stack.append(10)
# stack.append(20)
# stack.append(30)

# print("Stack after pushing elements:", stack)

# top = stack.pop()
# print("Popped item:", top)
# print("Stack after popping an element:", stack)

# top = stack[-1]
# print("Top element:", top)

# if not stack:
#     print("Stack is empty")
# else:
#     print("Stack is not empty")

# //////////////////////////////////////////////////////////////
# from collections import deque

# stack = deque()
# stack.append(1)
# stack.append(2)
# print(stack.pop())  

# //////////////////////////////////////////////////////
'''
Write a function is_valid_parentheses(s: string) -> bool 
that returns True if input string is valid, and False otherwise.
'''
# def is_valid_parentheses(s: str) -> bool:
#     stack = []
    
#     for char in s:
#         if char in "({[":
#             stack.append(char)
#         else:
#             if not stack:
#                 return False
#             if (char == ")" and stack[-1] == "(") or \
#                (char == "]" and stack[-1] == "[") or \
#                (char == "}" and stack[-1] == "{"):
#                 stack.pop()
#             else:
#                 return False

#     return not stack

# from collections import deque

# def is_valid_parentheses(s):
#     stack = deque()
#     mapping = {')': '(', ']': '[', '}': '{'}

#     for char in s:
#         if char in mapping:
#             top_element = stack.pop()
#             if top_element!= mapping[char]:
#                 return 'false'   
#         else:
#             stack.append(char)
#     return 'true' if not stack else 'false'


# print(is_valid_parentheses("{[]}")) 
# print(is_valid_parentheses("([)]")) 
# print(is_valid_parentheses("[{}]")) 

# //////////////////////////////////////////////////////////////////
'''
Reverse a string using stack
Write a function reverse_string(s: str) -> str
that takes a string s as input and returns a new string with the characters reversed.

print(reverse_string("hello"))  # Output: "olleh"
print(reverse_string("world"))  # Output: "dlrow"
print(reverse_string("Python")) # Output: "nohtyP
'''

# def reverse_string(s: str) -> str:
#     stack = []
    
#     for char in s:
#         stack.append(char)
#     reversed_s = ""

#     while stack:
#         reversed_s += stack.pop()
#     return reversed_s

# print(reverse_string("hello"))  
# print(reverse_string("world"))  
# print(reverse_string("Python")) 

# ///////////////////////////////////////////////////////////////////////////////////////////////
#  Queue

# from collections import deque

# class Queue:
#     def __init__(self):
#         self.queue = deque()

#     def enqueue(self, data):
#         self.queue.append(data)

#     def dequeue(self):
#         if not self.is_empty():
#             return self.queue.popleft()
#         return "Queue is empty"
    
#     def is_empty(self):
#         return len(self.queue) == 0
    
#     def size(self):
#         return len(self.queue)
    
# q= Queue()
# q.enqueue(5)
# q.enqueue(15)
# print(q.dequeue())

# ///////////////////////////////////////////////////////////////////////////
# Customers are entering in a bank. Add 5 customers.
# They can avail any service either deposit or withdraw. Also get the entering time of the customers.

# from collections import deque
# import random
# import time

# class Customer:
#     def __init__(self, name, service_type):
#         self.name = name
#         self.service_type = service_type
#         self.entry_time = time.strftime('%H:%M:%S', time.localtime())

#     def __str__(self):
#         return f"{self.name} ({self.service_type}) - Entered at {self.entry_time}"

# class BankQueue:
#     def __init__(self):
#         self.customers = deque()

#     def add_customer(self, customer):
#         self.customers.append(customer)
#         print(f'{customer} entered the bank.')

#     def serve_customer(self):
#         if self.customers:
#             customer = self.customers.popleft()
#             print(f'Serving {customer.name} ({customer.service_type})...')
#             time.sleep(random.randint(1, 3))  
#             print(f'{customer.name} has completed the service and left the bank.')
#         else:
#             print('No customers in the queue.')

# if __name__ == "__main__":
#     bank_queue = BankQueue()

#     service_types = ["Deposit", "Withdrawal"]
#     for i in range(1, 6):
#         customer = Customer(f"Customer{i}", random.choice(service_types))
#         bank_queue.add_customer(customer)
#         time.sleep(1)

#     print("\n--- Serving Customers ---\n")
#     while bank_queue.customers:
#         bank_queue.serve_customer()


# ///////////////////////////////////////////////////////////////

from collections import deque
import time

class Customer:
    def __init__(self, name, service_type):
        self.name = name
        self.service_type = service_type
        self.entry_time = time.strftime('%H:%M:%S', time.localtime())

class BankQueue:
    def __init__(self):
        self.queue = deque()

    def add_customer(self, name, service_type):
        customer = Customer(name, service_type)
        self.queue.append(customer)
        print(f"{customer.name} ({customer.service_type}) entered at {customer.entry_time}.")

    def serve_customer(self):
        if self.queue:
            customer = self.queue.popleft()
            print(f"Serving {customer.name} ({customer.service_type})...")
            time.sleep(1)  
            print(f"{customer.name} has completed the service and left the bank.")
        else:
            print("No customers in the queue.")

bank = BankQueue()

bank.add_customer("Kunal", "Deposit")
bank.add_customer("Jatin", "Withdrawal")
bank.add_customer("Kuldeep", "Deposit")
bank.add_customer("Vishnu", "Withdrawal")
bank.add_customer("Abhishek", "Deposit")

print("\n--- Serving Customers ---\n")

while bank.queue:
    bank.serve_customer()
