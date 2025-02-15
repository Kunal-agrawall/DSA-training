# sum given two num
# a = 2
# b = 3
# c=a+b
# print(c)

# Using EVAl function, we can do the same work as we can do it using EXCEPTION HANDLING
# a = eval(input("Enter 1st num: "))
# b = eval(input("Enter 2nd num: "))
# c = a + b
# print("Sum of " + str(a) + " and " + str(b) + " is " + str(c))

# ////////////////////////////////////////////////////////////
'''
I am adding two variables which can be int, float, or string.
if I'm adding 10+10, then it should give 20 not 20.0
So we can implement it using EXCEPTION HANDLING
'''
# Take input from the user
input1 = input("Enter the first value: ")
input2 = input("Enter the second value: ")

# Try to convert them to float, otherwise treat them as strings
try:
    # Attempt to convert inputs to float first
    num1 = float(input1)
    num2 = float(input2)

    # If both are integers (no decimal part), convert the result to an integer
    if num1.is_integer() and num2.is_integer():
        num1 = int(num1)
        num2 = int(num2)
    
    # If both inputs are numbers, add them
    sum_result = num1 + num2
    print("The sum is:", sum_result)

except ValueError:
    # If the inputs cannot be converted to numbers, treat them as strings and concatenate
    sum_result = input1 + input2
    print("The concatenated result is:", sum_result)
