# OOPS Concept

# class person:
#     def __init__(self, name, age, weight, height):
#         self.name = name
#         self.age = age
#         self.weight = weight
#         self.height = height
        
# obj = person("Kunal", "21 years", "54 kg", "5ft 9inch")
# print(obj.name)
# print(obj.age)
# print(obj.weight)
# print(obj.height)

# class person:
#     def own_method(self, name, age, weight, height):
#         self.name = name
#         self.age = age
#         self.weight = weight
#         self.height = height
        
# obj = person()
# obj.own_method("Kunal", "21 years", "54 kg", "5ft 9inch")
# print(obj.name)
# print(obj.age)
# print(obj.weight)
# print(obj.height)

# ////////////////////////////////////////////////

# WAP to sum of two numbers using class and object
# class sum:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def sum(self):
#             return self.a + self.b

# x = int(input("Enter 1st num: "))
# y = int(input("Enter 2nd num: "))
# obj = sum(x, y)
# print(obj.sum())

# /////////////////////////////////////////

# WAP to create class and store student's data and calculate total marks and set label accordingly, using class and objects in python.
# All inputs are given by user and user will input each subject marks.
# label set:
#             below 50 is average
#             below 70 is good
#             above 90 is excellent
# Student data:
#             roll_number
#             std_name
#             std_age
#             std_contact_number
#             number of subjects = 5
#             std marks per subject which is input by user

# class student:
#     def __init__(self, roll_number, std_name, std_age, std_contact_number,number_of_subjects,std_marks):
#         self.roll_number = roll_number
#         self.std_name = std_name
#         self.std_age = std_age
#         self.std_contact_number = std_contact_number
#         self.number_of_subjects = number_of_subjects
#         self.std_marks = std_marks
#     def calculate_total_marks(self):
#         total = 0
#         for i in self.std_marks:
#             total += i
#         result = total/number_of_subjects
#         return result
#     def set_label(self):
#         result = self.calculate_total_marks()
#         if result < 50:
#             return "average"
#         elif result >50 and result < 70:
#             return "good"
#         elif result > 70 and result < 100:
#             return "excellent"
        
# roll_number = int(input("Enter roll number: "))
# std_name = input("Enter std name: ")
# std_age = int(input("Enter std age: "))
# std_contact_number = int(input("Enter std contact number: "))
# number_of_subjects = int(input("Enter no. of subjects: "))
# std_marks = []
# for i in range(number_of_subjects):
#     std_marks.append(int(input(f"Enter marks for subject {i+1}: ")))

# obj = student(roll_number, std_name, std_age, std_contact_number, number_of_subjects, std_marks)


# print("\nRoll no:", obj.roll_number, "\nName:" , obj.std_name, "\nAge:", obj.std_age, 
#       "\nContact no:", obj.std_contact_number, "\nLabel:", obj.set_label())
    
# ////////////////////////////////////////////////////////////////////////////////////////
# Print the sum of two numbers without using print() method

# def add(a,b):
#     return a+b

# ///////////////////////////////////////////////////////

# Lambda function 

# Add two nums using lambda function
# a = int(input("Enter 1st num: "))
# b = int(input("Enter 2nd num: "))
# res = lambda a,b:(a+b)
# print('Sum =',res(a,b))

# ///////////////////////////////////////////////////

'''
You are given a string str, you need to return True if  the words "cat" and "hat" appear same number of times in str, otherwise return False.
Note: str contains only lowercase English alphabets.

Example 1:

Input:
str = catinahat
Output:
True
Explanation:
cat and hat both are present
1 number of times.
'''
# def check(str):
#     return str.count('cat') == str.count('hat')

# print(check("catinahat"))
# print(check("dog in hat"))

# /////////////////////////////////////////////////////////////////////

class Student:
    def __init__(self, roll_number, std_name, std_age, std_contact_number, std_marks):
        self.roll_number = roll_number
        self.std_name = std_name
        self.std_age = std_age
        self.std_contact_number = std_contact_number
        self.std_marks = std_marks
        
    def calculate_total_marks(self):
        return sum(self.std_marks)

    def calculate_percentage(self):
        total_marks = self.calculate_total_marks()
        return total_marks / len(self.std_marks)

    def set_label(self):
        percentage = self.calculate_percentage()
        if percentage < 50:
            return "Average"
        elif 50 <= percentage < 70:
            return "Good"
        elif 70 <= percentage <= 100:
            return "Excellent"

def get_student_data():
    students = []
    for i in range(1, 6):
        print(f"\nEnter details for Student {i}:")
        roll_number = int(input("Enter roll number: "))
        std_name = input("Enter student name: ")
        std_age = int(input("Enter student age: "))
        std_contact_number = int(input("Enter student contact number: "))
        std_marks = [int(input(f"Enter marks for subject {j+1}: ")) for j in range(5)] 
        student = Student(roll_number, std_name, std_age, std_contact_number, std_marks)
        students.append(student)
    return students

def topper(students):
    topper = max(students, key=lambda student: student.calculate_total_marks())
    return topper

students = get_student_data()

for student in students:
    print(f"\nRoll no: {student.roll_number}")
    print(f"Name: {student.std_name}")
    print(f"Age: {student.std_age}")
    print(f"Contact no: {student.std_contact_number}")
    print(f"Total Marks: {student.calculate_total_marks()}")
    print(f"Percentage: {student.calculate_percentage():.2f}%")
    print(f"Label: {student.set_label()}")

topper = topper(students)
print(f"\nTopper: {topper.std_name} with {topper.calculate_total_marks()} marks.")
