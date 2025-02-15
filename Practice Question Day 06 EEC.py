'''Write a Python program to create a class representing a Circle. 
Include methods to calculate its area and perimeter.'''

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def calculate_area(self):
#         return 3.14 * self.radius ** 2
#     def calculate_perimeter(self):
#         return 2 * 3.14 * self.radius
    
# circle = Circle(5)
# area = circle.calculate_area()
# perimeter = circle.calculate_perimeter()
# print("Area:", area)
# print("Perimeter:", perimeter)

# ///////////////////////////////////////////////////////////////////////////

'''Write a Python program to create a person class. Include attributes like name, country and date of birth. 
Implement a method'' to determine the person's age'''

# class Person:
#     def __init__(self, name, country, date_of_birth):
#         self.name = name
#         self.country = country
#         self.date_of_birth = date_of_birth
#     def calculate_age(self):
#         from datetime import datetime
#         today = datetime.now()
#         birth_date = datetime.strptime(self.date_of_birth, '%Y-%m-%d')
#         age = today.year - birth_date.year
#         if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
#             age -= 1
#         return age
    
# person = Person("Kunal", "India", "2004-05-23")
# age = person.calculate_age()
# print(f"Name: {person.name}")
# print(f"Country: {person.country}")
# print(f"Date of Birth: {person.date_of_birth}")
# print(f"Age: {age}")

# ///////////////////////////////////////////////////////////////////////////

'''Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. 
Implement subclasses for different shapes like circle, triangle, and square.
'''
# class Shape:
#     def area(self):
#         pass
    
#     def perimeter(self):
#         pass

# class Circle(Shape):
#     def __init__(self, r): self.r = r
#     def area(self): return (22/7) * self.r ** 2
#     def perimeter(self): return 2 * (22/7) * self.r

# class Square(Shape):
#     def __init__(self, s): self.s = s
#     def area(self): return self.s ** 2
#     def perimeter(self): return 4 * self.s

# class Triangle(Shape):
#     def __init__(self, a, b, c): self.a, self.b, self.c = a, b, c
#     def area(self): s = (self.a + self.b + self.c) / 2; return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
#     def perimeter(self): return self.a + self.b + self.c

# # Example usage
# for shape in [Circle(5), Square(4), Triangle(3, 4, 5)]:
#     print(f"{shape.__class__.__name__}: Area = {shape.area():.2f}, Perimeter = {shape.perimeter():.2f}")

# ///////////////////////////////////////////////////////////////////////////

'''Write a Python program to create a class representing a shopping cart. 
Include methods for adding and removing items, and calculating the total price.'''

# class ShoppingCart:
#     def __init__(self):
#         self.items = {}
    
#     def add_item(self, name, price, quantity=1):
#         if name in self.items:
#             self.items[name]['quantity'] += quantity
#         else:
#             self.items[name] = {'price': price, 'quantity': quantity}
    
#     def remove_item(self, name, quantity=1):
#         if name in self.items:
#             if self.items[name]['quantity'] > quantity:
#                 self.items[name]['quantity'] -= quantity
#             else:
#                 del self.items[name]
    
#     def total_price(self):
#         return sum(item['price'] * item['quantity'] for item in self.items.values())

#     def show_cart(self):
#         if not self.items:
#             return "The cart is empty."
#         return '\n'.join(f"{name}: {data['quantity']} x ${data['price']}" for name, data in self.items.items())

# # Example usage
# cart = ShoppingCart()
# cart.add_item("Apple", 1.5, 3)
# cart.add_item("Banana", 0.75, 2)
# cart.remove_item("Apple", 1)
# print(cart.show_cart())
# print(f"Total Price: ${cart.total_price():.2f}")

# ///////////////////////////////////////////////////////////////////////////

'''Write a Python program to create a class representing a bank. 
Include methods for managing customer accounts and transactions.'''

# class Bank:
#     def __init__(self): self.accounts = {}
#     def create_account(self, name, balance=0):
#         if name in self.accounts: return "Account exists."
#         self.accounts[name] = balance
#         return f"Account created for {name}."
#     def deposit(self, name, amount):
#         if name not in self.accounts: return "Account not found."
#         self.accounts[name] += amount
#         return f"Deposited ${amount} to {name}."
#     def withdraw(self, name, amount):
#         if name not in self.accounts: return "Account not found."
#         if self.accounts[name] < amount: return "Insufficient balance."
#         self.accounts[name] -= amount
#         return f"Withdrew ${amount} from {name}."
#     def get_balance(self, name):
#         return f"{name}'s balance: ${self.accounts.get(name, 'Account not found.')}"

# # Example usage
# bank = Bank()
# print(bank.create_account("Kunal", 1000))
# print(bank.deposit("Kunal", 500))
# print(bank.withdraw("Kunal", 200))
# print(bank.get_balance("Kunal"))