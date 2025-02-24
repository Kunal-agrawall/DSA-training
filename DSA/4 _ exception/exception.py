# 1
a = 10
b = 0
try:
    z = a/b
    print(z)
except (NameError,ArithmeticError) as err:
    print(err)
    print("Exception Executed")
else:
    print(z)
    print("Else Executed")
print()


# 2
try:
    z = 5/0
    print("Jatin")
except NameError as e:
    print("Body 1")
except ArithmeticError as c:
    print("Body 2")

