# Inheritance and type of Inheritance 

# Single level inheritance 
# class A:
#     def Adata(self):
#         print("Adata is method of class A")
        
# class B(A):
#     def Bdata(self):
#         print("Bdata is method of class B")
        
# obj = B()
# obj.Adata()
# obj.Bdata()

# ////////////////////////////////////////////////////////////

# Multi-level inheritance
# class A:
#     def Adata(self):
#         print("Adata is method of class A")
        
# class B(A):
#     def Bdata(self):
#         print("Bdata is method of class B")

# class C(B):
#     def Cdata(self):
#         print("Cdata is method of class C")
        
# class D(C):
#     def Ddata(self):
#         print("Ddata is method of class D")
        
# obj = D()
# obj.Adata()
# obj.Bdata()
# obj.Cdata()
# obj.Ddata() 

# ////////////////////////////////////////////////////////

# Multiple inheritance

# class A:
#     def Adata(self):
#         print("Adata is method of class A")
        
# class B:
#     def Bdata(self):
#         print("Bdata is method of class B")

# class C(A,B):
#     def Cdata(self):
#         print("Cdata is method of class C")
        
# obj = C()
# obj.Adata()
# obj.Bdata()
# obj.Cdata()

# ////////////////////////////////////////////////////////

# Hierarchical Inheritance

# class A:
#     def Adata(self):
#         print("Adata is method of class A")

# class B(A):
#     def Bdata(self):
#         print("Bdata is method of class B")

# class C(A):
#     def Cdata(self):
#         print("Cdata is method of class C")
        
# obj = C()
# obj.Adata()
# obj.Bdata() # error
# obj.Cdata()

# //////////////////////////////////////////////////////////////

# Hybrid Inheritance

# class A:
#     def Adata(self):
#         print("Adata is method of class A")

# class B(A):
#     def Bdata(self):
#         print("Bdata is method of class B")
        
# class C(A):
#     def Cdata(self):
#         print("Cdata is method of class C")
        
# class D(B,C):
#     def Ddata(self):
#         print("Ddata is method of class D")
        
# obj = D()
# obj.Adata()
# obj.Bdata()
# obj.Cdata()
# obj.Ddata()

# /////////////////////////////////////////////////////////////////

# Polymorphism 

# class father:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
        
#     def say_name(self):
#         print("Father name:", self.first_name, self.last_name)
        
#     def say_age(self):
#         print("Age:", self.age)
        

# class daughter(father):
#     def say_name(self):
#         print("Daughter name:", self.first_name, self.last_name)
        
# class son(father):
#     def say_name(self):
#         print("Son name:", self.first_name, self.last_name)
        
# obj = father("xyz", "upnaam", 1)
# obj.say_name()
# obj.say_age()

# obj1 = daughter("abc", "upnaam", 2)
# obj1.say_name()
# obj1.say_age()

# obj2 = son("pqr", "upnaam", 3)
# obj2.say_name()
# obj2.say_age()

# /////////////////////////////////////////////////////////////////

# Method Overloading

# class calculatesum:
#     def add(self, a, b):
#         return a + b
#     def add(self, a, b, c=0):
#         return a + b + c
    
# obj = calculatesum()
# print(obj.add(1, 2))  # TypeError: calculatesum.add() missing 1 required positional argument: 'c'
# print(obj.add(1, 2, 3)) 


# /////////////////////////////////////////////////////////////////

# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"
    
# class Bus(Vehicle):
#     def seating_capacity(self, capacity=50):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"
    
# obj = Bus()


# ////////////////////////////////////////////////////////////////////////////////

# Exception Handling

# print('radhe radhe')

# try:
#     printt('radhe radhe')
# except Exception as err: # Exception is a parent class of all exceptions and it's used to catch all exceptions. We use exception when we don't know the exception name
#     print(err)

# //////////////

# print('radhe radhe')

# try:
#     printt('radhe radhe')
# except NameError: # we use NameError because we know the exception name
#     print("Not correct")

# ///////////////////////////////////////
# a = int(input("X:"))
# b = int(input("Y:"))
# try:
#     print(a/b)
#     print('Hello, working fine')
# except Exception as err: # Arithmetic error
#     print(err)
#     print("I've done ex handling")

# ////////////////////////////////////
# a = int(input("X:"))
# b = int(input("Y:"))
# try:
#     c=a/b
#     print('Hello, working fine')
# except ArithmeticError:
#     print('Math error')
#     print("I've done ex handling")
# else:
#     print(c)
#     print("i am else method")

# /////////////////////////////////////////////////////////
a = int(input("X:"))
b = int(input("Y:"))
try:
    print(a/b)
    l = [1,2,3,4,5]
    print(l[10])
except Exception as err: 
    print(err)
    print("Method Execute")
    
except Exception as abc: 
    print(abc)
    print("2nd Method Execute")
    

print('Exit from error')