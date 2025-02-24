# program to reverse a string without using [::-1] (question 1.)
"""def reverse_string(s):
    reversed_str = ""
    for i in s:
        reversed_str = i + reversed_str  # Adding characters in reverse order
    return reversed_str

# Taking input from user
string = input("Enter a string: ")
print("Reversed string:", reverse_string(string))
"""


# program to check if the given string is a palindrome . (question 2.)
"""def is_palindrome(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str  # Adding characters in reverse order
    return s == reversed_str

# Taking input from user
string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
# Another method

string = input("Etnter a string: ")
rev_string = string[::-1]
if string == rev_string:
    print("The string is a plaindrome.")
else:
    print("The string is not a plaindrome.")
"""

# program to calculate the factorial of a given number. (question 3.)
"""
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Taking input from user
num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")


# Another method

factorial = 1
num = int(input("Enter a number: "))#taking user input
for i in range(2, num+1):
    factorial = factorial * i
print(f"Factorail of {num} is {factorial} .")

"""

#program to implement binary search on a sorted array. (question 4.)
"""
arr = [1,3,5,7,9]
target = int(input("Enter the target element: "))

left, right = 0, len(arr) - 1
while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        print(f"Element found at index {mid}")
        break
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
else:
    print("Element not found")
"""

#program to find the second maximum element in the array. (question 5.)
"""
def second_maximum(arr):
    if len(arr) < 2:
        return "Array should have at least two elements"
    first, second = float('-inf'), float('-inf')
    for num in arr:
        if num > first:
            second, first = first, num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else "No second maximum found"

# Taking input from user
arr = list(map(int, input("Enter array elements separated by space: ").split()))
result = second_maximum(arr)
print("Second maximum element:", result)

arr = [10,20,4,80,45,99]   #careate array
arr.sort()    #sort the array
index = len(arr)-1 #get array indexes
second_max = arr[index- 1 ]   #store the second largest element
print("Second maximum element is : ", second_max) # pirnt the second largest element
"""

# program to generate the fibonacci sequence up to given number . (question 6.)
"""
def fibonacci(n):#function to get the sequence
    if n <= 0:
        return "Please enter a positive integer"
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

num = int(input("Enter the number of terms: ")) #take user input
print("Fibonacci sequence:", fibonacci(num))    #print the sequence


num = int(input("Enter the number of terms: ")) #take user input

if num <= 0:
    print("Please enter a positive integer")    # check for valid input
else:
    sequence = [0, 1]
    for i in range(2, num): #loop gooes that starts at 2 and gooes num
        sequence.append(sequence[ i-1] + sequence[i-2])
    print("Fibonacci sequence:", sequence[:num])
"""

# program to remove duplicates for a list. (question 7.)
"""
lst = [1,2,2,3,4,4,5]
lst = list(set(lst))
print(lst)
"""

# write a python program to check if a number is prime or not. (question 8.)
"""
num = int(input("Enter the number : "))
if num < 2:
    print(f"{num} is not a prime number.")
else:
    for i in range(2, num):
        if num%i == 0 and i != num:
            print(f"{num} is not prime number.")
            break
        elif i == num-1:
            print(f"{num} is a prime number.")
"""

# write a program to the digits of a given number. (question 9.)
"""
num = int(input("Enter a number: "))

# Calculating sum of digits
sum_of_digits = 0
while num > 0:
    sum_of_digits += num % 10  # Extract last digit and add to sum
    num //= 10  # Remove last digit

print("Sum of digits:", sum_of_digits)

# another method
def digit_sum(num):
    sum = 0
    while num:
        b = num % 10
        sum = sum + b
        num //= 10
    return sum
    
    
num = 1234
result = digit_sum(num)
print(result)
"""

#find the missing number in an array 
"""
arr = [1, 2, 3, 5, 6]
n = arr[-1]  # Last number in the range
expected_sum = n * (n + 1) // 2  # Sum of first n natural numbers
actual_sum = sum(arr)  # Sum of given numbers
missing_number = expected_sum - actual_sum
print(f"Missing number is {missing_number}")


#another method
# Find the missing number in an array 
arr = [1, 2, 3, 5, 6]
n = arr[-1]  # Last element of the sorted array

for i in range(1, n + 1):
    if i not in arr:
        print(f"Missing number is {i}")
        break
"""

