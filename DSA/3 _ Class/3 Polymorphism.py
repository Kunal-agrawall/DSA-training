class Father:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_name(self):
        print(f"Father Name : {self.name}")
    
    def say_age(self):
        print(f"Father Age  : {self.age}")

class Son(Father):
    def say_name(self):
        print(f"Son Name : {self.name}")
    
    def say_age(self):
        print(f"Son Age  : {self.age}")

class Daughter(Father):
    def say_name(self):
        print(f"Daughter Name : {self.name}")
    
    def say_age(self):
        print(f"Daughter Age  : {self.age}")

father = Father("Ramswaroop", "55")
son = Son("Vivek", "30")
daughter = Daughter("Prachi Moti", "28")

father.say_name()
father.say_age()

son.say_name()
son.say_age()

daughter.say_name()
daughter.say_age()