# Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).

# nums = [i for i in range(1500, 2701) if i % 7 == 0 and i % 5 == 0]

# print(nums)

# ///////////////////////////////////////////////////////////////////////////

'''Write a Python program to guess a number between 1 and 9.
Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, 
user will get a "Well guessed!" message, and the program will exit.
'''
# import random

# num = random.randint(1, 9)

# while int(input("Guess a number between 1 and 9: ")) != num:
#     print("Try again!")

# print("Well guessed!")

# ///////////////////////////////////////////////////////////////////////////

'''Write a Python program that prints each item and its corresponding type from the following list.
Sample List : datalist = [1452, 11.23, 1+2j, True, 'gauravwebsite', (0, -1), [5, 12], {"class":'V', "section":'A'}]'''


# datalist = [1452, 11.23, 1+2j, True, 'gauravwebsite', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]

# for a in datalist:
#     print(f"Item: {a}, Type: {type(a)}")

# ///////////////////////////////////////////////////////////////////////////

'''Write a Python program that iterates the integers from 1 to 50. 
For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". 
For numbers that are multiples of three and five, print "FizzBuzz".

Sample Output :
fizzbuzz
1
2
fizz
4
buzz'''

# for a in range(1, 51):
#     if a % 3 == 0 and a % 5 == 0:
#         print("FizzBuzz")
#     elif a % 3 == 0:
#         print("Fizz")
#     elif a % 5 == 0:
#         print("Buzz")
#     else:
#         print(a)

# ///////////////////////////////////////////////////////////////////////////

'''Write a Python program that accepts a sequence of comma separated 4 digit binary numbers as its input. 
The program will print the numbers that are divisible by 5 in a comma separated sequence.
Sample Data : 0100,0011,1010,1001,1100,1001
Expected Output : 1010'''

# binary = input("Enter comma-separated 4-digit binary numbers: ").split(',')

# divisible_by_5 = [i for i in binary if int(i, 2) % 5 == 0]

# print(",".join(divisible_by_5))

# ///////////////////////////////////////////////////////////////////////////

'''Write a Python program that accepts a string and calculates the number of digits and letters.
Sample Data : Python 3.2
Expected Output :
Letters 6
Digits 2'''

# text = input("Enter a string: ")

# letters = sum(c.isalpha() for c in text)
# digits = sum(c.isdigit() for c in text)

# print(f"Letters {letters}")
# print(f"Digits {digits}")

# ///////////////////////////////////////////////////////////////////////////

'''Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. 
The numbers obtained should be printed in a comma-separated sequence.'''

# for i in range(100, 401):
#     a = str(i) 
#     if '1' in a or '3' in a or '5' in a or '7' in a or '9' in a:  
#         continue
#     print(i, end=",")

# ///////////////////////////////////////////////////////////////////////////

'''Write a Python program to calculate a dog's age in dog years.
Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
Expected Output:
Input a dog's age in human years: 15'''

# human_years = int(input("Input a dog's age in human years: "))

# if human_years <= 2:
#     dog_years = human_years * 10.5
# else:
#     dog_years = 2 * 10.5 + (human_years - 2) * 4

# print(f"The dog's age in dog years is {dog_years}")

# ///////////////////////////////////////////////////////////////////////////

'''Write a Python program to convert a month name to a number of days.
Expected Output:
List of months: January, February, March, April, May, June, July, August
, September, October, November, December
Input the name of Month: February
No. of days: 28/29 days'''

# month = input("Enter month name: ").strip().capitalize()

# if month in {"January", "March", "May", "July", "August", "October", "December"}:
#     print("31 days")
# elif month in {"April", "June", "September", "November"}:
#     print("30 days")
# elif month == "February":
#     print("28/29 days")
# else:
#     print("Invalid month name")

# 2nd method

# month_days = {
#     "January": "31 days",
#     "February": "28/29 days",
#     "March": "31 days",
#     "April": "30 days",
#     "May": "31 days",
#     "June": "30 days",
#     "July": "31 days",
#     "August": "31 days",
#     "September": "30 days",
#     "October": "31 days",
#     "November": "30 days",
#     "December": "31 days"
# }

# print("List of months:", ", ".join(month_days.keys()))

# month = input("Input the name of Month: ").strip().capitalize()

# print(f"No. of days: {month_days.get(month, 'Invalid month name')}")

# ///////////////////////////////////////////////////////////////////////////
'''
Write a Python program to check the validity of passwords input by users. 
Validation : 
 
 At least 1 letter between [a-z] and 1 letter between [A-Z]. 
 At least 1 number between [0-9]. 
 At least 1 character from [$#@]. 
 Minimum length 6 characters. 
 Maximum 
  length 16 characters.
'''

# password = input("Enter a password: ")

# if len(password) < 6 or len(password) > 16:
#     print("Password length should be between 6 and 16 characters.")
#     exit()

# has_lowercase = False

# has_uppercase = False

# has_number = False

# has_special_char = False

# for char in password:
#     if char.islower():
#         has_lowercase = True
#     elif char.isupper():
#         has_uppercase = True
#     elif char.isdigit():
#         has_number = True
#     elif char in "$#@":
#         has_special_char = True

# if not has_lowercase:
#     print("Password should contain at least one lowercase letter.")
#     exit()

# if not has_uppercase:
#     print("Password should contain at least one uppercase letter.")
#     exit()

# if not has_number:
#     print("Password should contain at least one number.")
#     exit()

# if not has_special_char:
#     print("Password should contain at least one special character ($#@).")
#     exit()

# SECOND METHOD 
# password = input("Enter a password: ")

# if not (6 <= len(password) <= 16):
#     exit(print("Password length should be between 6 and 16 characters."))

# conditions = [
#     any(c.islower() for c in password) or exit(print("Password should contain at least one lowercase letter.")),
#     any(c.isupper() for c in password) or exit(print("Password should contain at least one uppercase letter.")),
#     any(c.isdigit() for c in password) or exit(print("Password should contain at least one number.")),
#     any(c in "$#@" for c in password) or exit(print("Password should contain at least one special character ($#@)."))
# ]

# ///////////////////////////////////////////////////////////////////////////