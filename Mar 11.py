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


#  Queue

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        return "Queue is empty"
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
q= Queue()
q.enqueue(5)
q.enqueue(15)
print(q.dequeue())