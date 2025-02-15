'''Write a Python program to display the current date and time. 
Sample Output :
Current date and time : 2014-07-05 14:34:14  '''


# from datetime import datetime

# now = datetime.now()

# formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

# print("Current date and time : " + formatted_time)

# //////////////////////////////////////////////////////////////////

'''Write a Python program that calculates the area of a circle based on the radius entered by the user. Sample Output :
r = 1.1
Area = 3.8013271108436504'''

# radius = float(input("Enter the radius of the circle : "))
# area = 3.14 * radius ** 2
# print("Area =", area)

# //////////////////////////////////////////////////////////////////

# Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.

# first_name = input("Enter your first name : ")

# last_name = input("Enter your last name : ")

# print(last_name + " " + first_name)

# ///////////////////////////////////////////////////////////////////////////
# Write a Python program to display the first and last colors from the following list.

# color_list = ["Red","Green","White" ,"Black"]

# print(color_list[0])
# print(color_list[-1])

# ///////////////////////////////////////////////////////////////////////////

# Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.

# a = 5
# b = 5
# c = 5

# if a == b == c:
#     result = 3 * (a + b + c) 
# else:
#     result = a + b + c  

# print("Result:", result)

# ///////////////////////////////////////////////////////////////////////////

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

# ///////////////////////////////////////////////////////////////////////////

# Sort a list of tuples by the first element in each tuple.
# Sample List: [(5, 1), (2, 4), (3, 3), (1, 2)]

# Expected Output:
# [(1, 2), (2, 4), (3, 3), (5, 1)]
# Explanation: The tuples are sorted by the first element. The sorted list is: [(1, 2), (2, 4), (3, 3), (5, 1)].

# list = [(5, 1), (2, 4), (3, 3), (1, 2)]
# sorted_list = sorted(list, key=lambda x: x[0])
# print(sorted_list)

# ///////////////////////////////////////////////////////////////////

'''Sort a list of tuples by the sum of the elements in each tuple.
Sample List: [(1, 2), (2, 3), (3, 1), (4, 2)]

Expected Output:
[(1, 2), (3, 1), (4, 2), (2, 3)]
Explanation: The tuples are sorted based on the sum of their elements. Sum of elements in the tuples:

(1, 2) → 3
(2, 3) → 5
(3, 1) → 4
(4, 2) → 6
The sorted list by sum of elements: [(1, 2), (3, 1), (4, 2), (2, 3)].'''

# list = [(1, 2), (2, 3), (3, 1), (4, 2)]
# sorted_list = sorted(list, key=lambda x: sum(x))
# print(sorted_list)

# ///////////////////////////////////////////////////////////////////////////

'''Sort a list of tuples in reverse order based on the first element in each tuple.
Sample List: [(3, 4), (1, 2), (5, 1), (2, 3)]

Expected Output:

python
Copy
[(5, 1), (3, 4), (2, 3), (1, 2)]
Explanation: The tuples are sorted by the first element in reverse order: 5 > 3 > 2 > 1.
'''

# list = [(3, 4), (1, 2), (5, 1), (2, 3)]
# sorted_list = sorted(list, key=lambda x: x[0], reverse=True)
# print(sorted_list)

# ///////////////////////////////////////////////////////////////////////////

'''Group tuples by the first element in each tuple and sort the groups by the last element.
Sample List: [(2, 5), (1, 2), (2, 3), (1, 1), (2, 4)]

Expected Output:
[(1, 1), (1, 2), (2, 3), (2, 4), (2, 5)]
Explanation: First, the list is grouped by the first element (1 and 2), and then each group is sorted by the second element. The final result is [(1, 1), (1, 2), (2, 3), (2, 4), (2, 5)].
'''

# list = [(2, 5), (1, 2), (2, 3), (1, 1), (2, 4)]
# result = sorted(list, key=lambda x: (x[0], x[1]))
# print(result)

# ///////////////////////////////////////////////////////////////////////////

'''Sort a list of tuples by the length of each tuple.
Sample List: [(1, 2), (1, 2, 3), (4,), (2,)]

Expected Output:
[(4,), (2,), (1, 2), (1, 2, 3)]
Explanation: The tuples are sorted by their length: [(4,), (2,), (1, 2), (1, 2, 3)].
'''

# list = [(1, 2), (1, 2, 3), (4,), (2,)]
# sorted_list = sorted(list, key=len)
# print(sorted_list)

# ///////////////////////////////////////////////////////////////////////////

'''Sort a list of tuples by the first element, and in case of a tie, by the second element.
Sample List: [(1, 3), (1, 2), (2, 4), (2, 3)]

Expected Output:

[(1, 2), (1, 3), (2, 3), (2, 4)]
Explanation: The tuples are first sorted by the first element. If two tuples have the same first element, they are then sorted by the second element. The result is: [(1, 2), (1, 3), (2, 3), (2, 4)].
'''

# list = [(1, 3), (1, 2), (2, 4), (2, 3)]
# list.sort(key=lambda x: x[0])
# list.sort(key=lambda x: x[1])
# print(list)

# ///////////////////////////////////////////////////////////////////////////

'''Find the tuple with the maximum sum of elements from a list of tuples.
Sample List: [(1, 2), (3, 1), (5, 2), (4, 3)]

Expected Output:
(5, 2)
Explanation: The sum of the elements in the tuples:

(1, 2) → 3
(3, 1) → 4
(5, 2) → 7
(4, 3) → 7
The tuple with the maximum sum is (5, 2) or (4, 3) (since both have the same sum of 7). In case of a tie, the tuple that appears first is chosen.
'''

# list = [(1, 2), (3, 1), (5, 2), (4, 3)]
# max_sum = max(list, key=lambda x: sum(x))
# print(max_sum)

# ///////////////////////////////////////////////////////////////////////////

'''Find the tuple with the minimum first element in a list of tuples.
Sample List: [(4, 5), (2, 3), (1, 6), (3, 2)]

Expected Output:
(1, 6)
Explanation: The tuple with the minimum first element is (1, 6).
'''

# list = [(4, 5), (2, 3), (1, 6), (3, 2)]
# result = min(list, key=lambda x: x[0])
# print(result)

# ///////////////////////////////////////////////////////////////////////////

'''Sort a list of tuples by the second element, but if two second elements are equal, sort by the first element.
Sample List: [(3, 5), (1, 4), (2, 4), (4, 5)]

Expected Output:
[(1, 4), (2, 4), (3, 5), (4, 5)]
Explanation: The tuples are first sorted by the second element, and if the second elements are equal, they are sorted by the first element.
'''

# list = [(3, 5), (1, 4), (2, 4), (4, 5)]
# list.sort(key=lambda x: x[1])
# list.sort(key=lambda x: x[0])
# print(list)

# ///////////////////////////////////////////////////////////////////////////

''' Create a new list of tuples where each tuple contains the sum of the elements from the original list of tuples. Sort it in increasing order of the sum.
Sample List: [(1, 3), (2, 1), (4, 2), (3, 1)]

Expected Output:
[(2, 1), (3, 1), (1, 3), (4, 2)]
Explanation: First, calculate the sum of elements in each tuple:

(1, 3) → 4
(2, 1) → 3
(4, 2) → 6
(3, 1) → 4
After sorting by sum: [(2, 1), (3, 1), (1, 3), (4, 2)].
'''

# sample_list = [(1, 3), (2, 1), (4, 2), (3, 1)]
# sorted_list = sorted(sample_list, key=lambda x: sum(x))

# print(sorted_list)


# /////////////////////////////////////////////////////////////////

'''Merge Sorted Lists:
 Given two sorted lists, write a Python function to merge them into a single sorted list without using the sorted() function.'''

# def merge_lists(list1, list2):
#     merged_list = []
#     while list1 and list2:
#         merged_list.append((list1 if list1[0] < list2[0] else list2).pop(0))
#     return merged_list + list1 + list2

# list1 = [1, 3, 5]
# list2 = [2, 4, 6]
# result = merge_lists(list1, list2)
# print(result) 

# ///////////////////////////////////////////////////////////////////////////

'''Rotate List: 
Write a Python function that rotates a list to the right by k positions. 
(For example, [1, 2, 3, 4, 5] rotated by 2 positions becomes [4, 5, 1, 2, 3]).'''

# def rotate_list(nums, k):
#     k = k % len(nums)  # to handle the case where k is larger than the list size
#     return nums[-k:] + nums[:-k]

# # Example usage:
# nums = [1, 2, 3, 4, 5]
# k = 2
# rotated_list = rotate_list(nums, k)
# print(rotated_list)  # Output: [4, 5, 1, 2, 3]

# ///////////////////////////////////////////////////////////////////////////

'''Find the Longest Increasing Subsequence: Given a list of integers, 
write a Python function that returns the longest increasing subsequence.'''






# ///////////////////////////////////////////////////////////////////////////////////

'''Group Anagrams: 
Write a function that takes a list of strings and groups them into anagrams (i.e., strings that are anagrams of each other).'''

# def group_anagrams(strs):
#     anagram_dict = {}
#     for word in strs:
#         sorted_word = ''.join(sorted(word))
#         if sorted_word in anagram_dict:
#             anagram_dict[sorted_word].append(word)
#         else:
#             anagram_dict[sorted_word] = [word]
#     return list(anagram_dict.values())


# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# result = group_anagrams(strs)
# print(result)

# ///////////////////////////////////////////////////////////////////////////////////

'''Nested List Flattening: 
Write a Python program that flattens a nested list of lists into a single list (e.g., [[1, 2], [3, [4, 5]], 6] becomes [1, 2, 3, 4, 5, 6]).'''

# def flatten_list(nested_list):
#     flattened_list = []
#     for item in nested_list:
#         if isinstance(item, list):
#             flattened_list.extend(flatten_list(item))
#         else:
#             flattened_list.append(item)
#     return flattened_list

# nested_list = [[1, 2], [3, [4, 5]], 6]
# result = flatten_list(nested_list)
# print(result)

# ///////////////////////////////////////////////////////////////////////////////////

'''Tuple Comparison: 
Write a function that compares two tuples element by element and returns True if all elements are equal, otherwise False.'''

# def compare_tuples(tuple1, tuple2):
#     if len(tuple1) != len(tuple2):
#         return False
#     for i in range(len(tuple1)):
#         if tuple1[i] != tuple2[i]:
#             return False
#     return True

# tuple1 = (1, 2, 3)
# tuple2 = (1, 2, 3)
# result = compare_tuples(tuple1, tuple2)
# print(result)  # Output: True

# //////////////////////////////////////////////////////////////////

'''Find the Second Largest Element: 
Write a Python function that returns the second largest element in a tuple without converting it to a list.'''

# def second_largest(data):
#     largest, second = float('-inf'), float('-inf')
#     for num in data:
#         largest, second = (num, largest) if num > largest else (largest, max(second, num))
#     return second if second != float('-inf') else None

# print(second_largest((10, 5, 8, 3, 7, 19)))

# ///////////////////////////////////////////////////////////////////////////

'''Tuple to Dictionary: 
Write a function that takes a list of tuples where each tuple contains two elements (key, value), and converts them into a dictionary.'''

# def tuple_to_dict(tuples):
#     dictionary = {}
#     for key, value in tuples:
#         dictionary[key] = value
#     return dictionary

# tuples = [('apple', 10), ('banana', 20), ('cherry', 30)]
# result = tuple_to_dict(tuples)
# print(result) 

# /////////////////////////////////////////////////////////////////////////////////////////

'''Count Occurrences in Tuple: 
Given a tuple of elements, write a Python function that counts the frequency of each element using a dictionary and returns it.
'''

# def count_occurrences(tuple):
    # occurrences = {}
    # for element in tuple:
    #     if element in occurrences:
    #         occurrences[element] += 1
    #     else:
    #         occurrences[element] = 1
    # return occurrences

# tuple = (1, 2, 3, 2, 4, 3, 2)
# result = count_occurrences(tuple)
# print(result)  # Output: {1: 1, 2: 3, 3: 2, 4: 1}

# //////////////////////////////////////////////////////////////////

'''Find Symmetric Difference: 
Write a Python function that takes two sets and returns their symmetric difference (elements that are in one set or the other, but not both).
'''

# def symmetric_difference(set1, set2):
    # return set1.symmetric_difference(set2)

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# result = symmetric_difference(set1, set2)
# print(result)  

# //////////////////////////////////////////////////////////////////

'''Set Operations on Multiple Sets: 
Given multiple sets, write a Python program to find the union, intersection, and difference for all the sets.
'''
# def set_operations(*sets):
#     union_set = set.union(*sets)
#     intersection_set = set.intersection(*sets)
#     difference_set = set.difference(*sets)
    
#     return union_set, intersection_set, difference_set

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# set3 = {4, 6, 7, 8}

# union_result, intersection_result, difference_result = set_operations(set1, set2, set3)

# print("Union:", union_result)
# print("Intersection:", intersection_result)
# print("Difference:", difference_result)

# //////////////////////////////////////////////////////////////////////////////////////////////////

'''Check for Subset and Superset: 
Write a Python function that takes two sets and checks if one is a subset or superset of the other.
'''

# def is_subset_or_superset(set1, set2):
    # return set1.issubset(set2) or set1.issuperset(set2)

# set1 = {1, 2, 3, 4}
# set2 = {1, 2, 3}
# result = is_subset_or_superset(set1, set2)
# print(result) 

# ////////////////////////////////////////////////////////////////////////////////////

'''Set of Frozensets: 
Create a set that contains frozensets. Perform set operations (e.g., union, intersection) on it.
'''

# set_of_frozensets = {frozenset({1, 2, 3}), frozenset({3, 4, 5}), frozenset({5, 6, 7})}
# union_result = set().union(*set_of_frozensets)
# intersection_result = set_of_frozensets.pop()  

# for fs in set_of_frozensets:
#     intersection_result = intersection_result.intersection(fs)

# print("Set of Frozensets:", set_of_frozensets)
# print("Union:", union_result)
# print("Intersection:", intersection_result)

# ////////////////////////////////////////////////////////////////////////////////////

'''Remove Elements from List and Set: 
Given a list and a set, write a function that removes the elements from the list that exist in the set, without modifying the original set.
'''

# def remove_elements(lst, s):
#     lst_without_s = [x for x in lst if x not in s]
#     return lst_without_s

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# s = {3, 4, 5, 6, 7, 8}
# result = remove_elements(lst, s)
# print("List:", result)

# ////////////////////////////////////////////////////////////////////////////////////

'''Find the Intersection of a List of Tuples: 
Given a list of tuples (each tuple has two elements), write a Python function to find the intersection of the first elements of all the tuples and return the result as a set.'''

# def find_intersection(tuples):
    # intersection = set(tuples[0])
    # for t in tuples[1:]:
    #     intersection &= set(t)
    # return intersection

# tuples = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
# result = find_intersection(tuples)
# print("Intersection:", result)  # Output: {2, 3, 4, 5}

# ////////////////////////////////////////////////////////////////////////////////

'''Merge List of Sets:
Write a function that takes a list of sets and merges them into one set, removing any duplicate elements.'''

# def merge_sets(sets):
    # return set().union(*sets)

# sets = [{1, 2, 3}, {3, 4, 5}, {5, 6, 7}]
# result = merge_sets(sets)
# print("Merged Set:", result ) 

# /////////////////////////////////////////////////////////

'''List and Tuple Frequency: 
Given a list and a tuple, write a Python program to count how many times the elements from the tuple appear in the list.'''

# def count_frequency(lst, tup):
    # freq = {}
    # for element in tup:
    #     if element in lst:
    #         freq[element] = lst.count(element)
    # return freq

# lst = [1, 2, 3, 2, 4, 3, 2]
# tup = (2, 3)
# result = count_frequency(lst, tup)
# print("Frequency:", result)

# ////////////////////////////////////////////////////////////////////////////////

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

# ///////////////////////////////////////////////////////////////////////////