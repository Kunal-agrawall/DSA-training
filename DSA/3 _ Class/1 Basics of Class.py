# Using Constructor
class person1:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
    
    def display(self):
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
        print(f"Weight : {self.weight}kg")
        print(f"Height : {self.height}ft")

Van = person1("Vanshika", "20", "100", "5.2")
Van.display()
print()


# Our own Initializer
class person2:
    def self_initializer(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
    
    def display(self):
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
        print(f"Weight : {self.weight}kg")
        print(f"Height : {self.height}ft")


Jan = person2()
Jan.self_initializer("Jatin", "22", "58", "5.8")
Jan.display()