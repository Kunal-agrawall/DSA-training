# import keyword

# print(keyword.kwlist)
# print(len(keyword.kwlist))
# help("keywords")

# //////////////////////////////////////////////

# a = 2 + 3j  # A complex number
# b = False      # A boolean value

# # Adding them
# result = a+b

# print(result)  # Output will be (3+3j)

# OPERATORS 
# a= 1
# b = 2
# print(a>b is a<b)

# a= 1
# b = 2.0
# print(a>b is a<b)

# a= 1
# b = 2
# print(a>b and a<b)

# a= 1
# b = 2
# print(a is b)

# a= 1
# b = 2.0
# print(a and b)


# a = 10
# b = 10.0
# print(id(a))
# print(id(b))

# a = 10
# b = 10
# print(id(a))
# print(id(b))

# ///////////////////////////////////////////////////////////////
# string palindrome

# abc = "radhe"
# left = 0
# right = len(abc) - 1

# is_palindrome = True
# while left < right:
#     if abc[left] != abc[right]:
#         is_palindrome = False
#         break
#     left += 1
#     right -= 1


# if is_palindrome:
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")

# Second method

# x = input("Enter a string: ")
# y = x[::-1]
# if y==x:
#     print("Palindrome")
# else:
#     print("Not palindrome")


# WAP to print string in forward and backward direction with space after every alphabet


# input_string = "radhe is a good boy"

# forward_output = ' '.join(input_string)
# print("Forward:", forward_output)

# backward_output = ' '.join(input_string[::-1])
# print("Backward:", backward_output)

# ///////////////////////////////////////
# Use method: upper, lower, capatilize

# a = "python Programming"
# print(a.upper())
# print(a.lower())
# print(a.capitalize())

a = "python is programming language" # "Python Is Programming Language"
b = "python is programming language" # "python Is Programming language"
print(a.title())

print(b.replace("is", "Is").replace("programming", "Programming"))


