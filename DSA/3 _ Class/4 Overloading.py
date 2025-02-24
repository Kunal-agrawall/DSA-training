# Overloading is not possible in Python.
# Beacuse Python uses Interpreter, not Compiler
# So we will either use keyword arg, default arg or variable length arg

class Calc:
    # def add(self, a,b):
    #     return a+b
    # def add(a,b,c) 
    # Cause error
    
    def add(self, a,b,c=0):
        return a+b+c