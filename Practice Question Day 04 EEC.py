# Write a Python function to find the maximum of three numbers.

# def find_max(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else:
#         return c
    
# print(find_max(5, 10, 3))  # Output: 10
# print(find_max(15, 20, 10))  # Output: 20
# print(find_max(7, 7, 7))    # Output: 7

# SECOND METHOD
# def maximum_of_three(a, b, c):
#     return max(a, b, c)

# # Example usage
# print(maximum_of_three(10, 20, 30))  # Output: 30

# ///////////////////////////////////////////////////////////////////////////

'''Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20
'''

# def sum_num(n):
#     total = 0
#     for i in n:
#         total += i
#     return total

# print(sum_num((8, 2, 3, 0, 7)))  # Output: 20

# SECOND METHOD
# def sum_of_list(numbers):
#     return sum(numbers)

# # Example usage
# sample_list = [8, 2, 3, 0, 7]
# print(sum_of_list(sample_list))  # Output: 20

# ///////////////////////////////////////////////////////////////////////////

'''Write a Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336'''

# def multiply_num(n):
#     result = 1
#     for i in n:
#         result *= i
#     return result

# print(multiply_num((8, 2, 3, -1, 7)))  # Output: -336

# ///////////////////////////////////////////////////////////////////////////

'''Write a Python function that takes a list and returns a new list with distinct elements from the first list.
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]'''

# def unique_list(n):
#     return list(set(n))

# print(unique_list([1,2,3,3,3,3,4,5]))  # Output: [1, 2, 3, 4, 5]

# ///////////////////////////////////////////////////////////////////////////

'''Write a Python program to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]'''

# def print_even_numbers(n):
#     for i in n:
#         if i % 2 == 0:
#             print(i)

# print_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])  # Output: 2 4 6 8

# SECOND METHOD

# def even_numbers(lst):
#     return [num for num in lst if num % 2 == 0]

# ///////////////////////////////////////////////////////////////////////////

'''Write a Python function to check whether a number is "Perfect" or not.
According to Wikipedia : In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors, 
that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum). 
Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself).
Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. 
Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. 
The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.'''

# def is_perfect(n):
#     sum= 0
#     for i in range(1, n):
#         if n % i == 0:
#             sum += i
#     return sum == n

# print(is_perfect(6))  # Output: True

# SECOND METHOD

# def is_perfect_number(num):
#     divisors = [i for i in range(1, num) if num % i == 0]
#     if sum(divisors) == num:
#         return True
#     return False

# # Example usage
# print(is_perfect_number(6))  # Output: True (6 is a perfect number)
# print(is_perfect_number(28)) # Output: True (28 is a perfect number)
# print(is_perfect_number(10)) # Output: False (10 is not a perfect number)

# ///////////////////////////////////////////////////////////////////////////

'''Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow'''

# def sort_words(n):
    # words = n.split('-')
    # words.sort()
    # return '-'.join(words)

# print(sort_words('green-red-yellow-black-white'))  # Output: black-green-red-white-yellow

# ///////////////////////////////////////////////////////////////////////////

'''Write a Python program that invokes a function after a specified period of time.
Sample Output:
Square root after specific milliseconds:
4.0
10.0
158.42979517754858
'''

# import time
# import math

# def print_square_root():
#     print(math.sqrt(16))  # Square root of 16 is 4.0

# def delayed_function():
#     time.sleep(2)  # Delay for 2 seconds
#     print_square_root()

# # Example usage
# delayed_function()  # Output after 2 seconds: 4.0
# # You can adjust the time.sleep() parameter to control the delay.
