# Q1
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius   
        
    def area(self):
        return math.pi * self.radius ** 2    
        
    def perimeter(self):
        return 2 * math.pi * self.radius

if __name__ == "__main__":
    r = float(input("Enter the radius of the circle: "))
    circle = Circle(r)
    print(f"Area: {circle.area():.2f}")
    print(f"Perimeter: {circle.perimeter():.2f}")


# Q2
from datetime import datetime
class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")
    
    def calculate_age(self):
        today = datetime.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age

if __name__ == "__main__":
    name = input("Enter name: ")
    country = input("Enter country: ")
    dob = input("Enter date of birth (YYYY-MM-DD): ")
    person = Person(name, country, dob)
    print(f"{person.name} from {person.country} is {person.calculate_age()} years old.")


# Q3
import math
class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self):
        return self.a + self.b + self.c

if __name__ == "__main__":
    circle = Circle(5)
    print(f"Circle -> Area: {circle.area():.2f}, Perimeter: {circle.perimeter():.2f}")
    
    square = Square(4)
    print(f"Square -> Area: {square.area():.2f}, Perimeter: {square.perimeter():.2f}")
    
    triangle = Triangle(3, 4, 5)
    print(f"Triangle -> Area: {triangle.area():.2f}, Perimeter: {triangle.perimeter():.2f}")


# Q4
class ShoppingCart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, item_name, price, quantity=1):
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'price': price, 'quantity': quantity}
        print(f"Added {quantity} x {item_name} to the cart.")
    
    def remove_item(self, item_name, quantity=1):
        if item_name in self.items:
            if self.items[item_name]['quantity'] > quantity:
                self.items[item_name]['quantity'] -= quantity
                print(f"Removed {quantity} x {item_name} from the cart.")
            else:
                del self.items[item_name]
                print(f"Removed {item_name} from the cart.")
        else:
            print(f"{item_name} is not in the cart.")
    
    def calculate_total(self):
        total = sum(details['price'] * details['quantity'] for details in self.items.values())
        return total
    
    def show_cart(self):
        if not self.items:
            print("The shopping cart is empty.")
        else:
            print("Shopping Cart:")
            for item, details in self.items.items():
                print(f"{item}: {details['quantity']} x ${details['price']:.2f}")
            print(f"Total: ${self.calculate_total():.2f}")


if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Apple", 1.5, 3)
    cart.add_item("Banana", 0.75, 2)
    cart.show_cart()
    cart.remove_item("Apple", 2)
    cart.show_cart()
    cart.remove_item("Banana")
    cart.show_cart()



# Q6
class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = {}
    
    def add_customer(self, customer_id, name, initial_balance=0):
        if customer_id in self.customers:
            print("Customer already exists.")
        else:
            self.customers[customer_id] = {'name': name, 'balance': initial_balance}
            print(f"Customer {name} added with balance ${initial_balance:.2f}.")
    
    def deposit(self, customer_id, amount):
        if customer_id in self.customers:
            self.customers[customer_id]['balance'] += amount
            print(f"Deposited ${amount:.2f} to {self.customers[customer_id]['name']}'s account.")
        else:
            print("Customer not found.")
    
    def withdraw(self, customer_id, amount):
        if customer_id in self.customers:
            if self.customers[customer_id]['balance'] >= amount:
                self.customers[customer_id]['balance'] -= amount
                print(f"Withdrew ${amount:.2f} from {self.customers[customer_id]['name']}'s account.")
            else:
                print("Insufficient balance.")
        else:
            print("Customer not found.")
    
    def get_balance(self, customer_id):
        if customer_id in self.customers:
            return self.customers[customer_id]['balance']
        else:
            print("Customer not found.")
            return None
    
    def show_customers(self):
        if not self.customers:
            print("No customers in the bank.")
        else:
            print("Customers:")
            for customer_id, details in self.customers.items():
                print(f"{details['name']} (ID: {customer_id}) - Balance: ${details['balance']:.2f}")

if __name__ == "__main__":
    bank = Bank("MyBank")
    bank.add_customer(101, "Alice", 500)
    bank.add_customer(102, "Bob", 1000)
    bank.deposit(101, 200)
    bank.withdraw(102, 300)
    bank.show_customers()


# Q7
class Vehicle:
    def __init__(self, name, max_speed, mileage, color="White"):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = color
        self.capacity = None

    def seat_capacity(self, capacity):
        self.capacity = capacity
        return f"Seating Capacity of {self.name} : {self.capacity}"
    
    def fair(self):
        self.seating_charge = self.capacity*100
        return self.capacity
    
    def display(self):
        print(f"Name    : {self.name}")
        print(f"Speed   : {self.max_speed}")
        print(f"Mileage : {self.mileage}")
        print(f"Color   : {self.color}")
class Bus(Vehicle):
    def seat_capacity(self, capacity=50):
        self.capacity = capacity
        return f"Seating Capacity of {self.name} : {capacity}"
    
    def fair(self, charge):
        self.seating_charge = self.capacity*100 + (self.capacity*10)
        return self.capacity  
s1 = Bus("Milton", 250, 88)
s1.seat_capacity()
s1.display()


    

        