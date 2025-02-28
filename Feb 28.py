# Frozen Set

# fs = frozenset([1,2,3,4,5])
# print(fs)

# fs1 = frozenset([1,2,3,4])
# fs2 = frozenset([3,4,5,6])

# # union 
# print(fs1 | fs2)

# # Intersection
# print(fs1 & fs2)

# # Difference
# print(fs1 - fs2)

# # Symmetric Difference
# print(fs1 ^ fs2)


#  Using frozenset as a dictionary key

# my_dict = {frozenset([1,2,3]): "frozenset example"}
# print(my_dict[frozenset([1,2,3])])
# print(my_dict)

# //////////////////////////////////////////////////////////////////////////

# Specialized Collections 
# 1.	Named Tuple

from collections import namedtuple

# Person = namedtuple("Person", ['name', 'age'])
# p = Person("John", 30)
# print(p.name, p.age)

# Employee = namedtuple("Employee", ['name', 'age', 'department', 'salary'])
# emp1 = Employee("Rahul", 30, "HR", 50000)
# emp2 = Employee("Satyam", 28, "IT", 60000)
# emp3  = Employee("Kunal", 21, "Finance", 70000)

# print(emp1.name, emp1.department, emp1.salary)
# print(emp2.name)
# print(emp3.name,  emp3.age)

# # using _asdict() to convert into a dictionary
# print(emp1._asdict())

# #  updating valus using _replace()

# emp1_updated = emp1._replace(salary = 25000)
# print(emp1_updated.salary)

# /////////////////////////////////////////////////////////////////////////////
# 2. Default Dictionary

from collections import defaultdict

# dd = defaultdict(int)
# dd['apple'] +=2
# print(dd['apple']) # Output: 2 
# print(dd['banana']) # Output: 0 (default value)
# print(dd['orange']) # Output: 0 (default value)
# print(dd)

# Counting word occurrences in a sentence

# word_count = defaultdict(int)

# sentence = "apple banana apple apple orange banana apple mango orange" 

# #  Split sentence into words and count occurrences

# for word in sentence.split():
#     word_count[word] += 1

# print(dict(word_count))

# //////////////////////////////////////////////////////////////////////////

# 3. OrderedDict

from collections import OrderedDict

# od = OrderedDict()
# od['a'] = 1
# od['c'] = 3
# od['b'] = 2

# print(od) # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])

import matplotlib.pyplot as plt

# Write a  Python program to draw a line with suitable label in the x axis, y axis and a title.

# x = [1,2,3,4,5]
# y = [1,2,3,4,5]

# plt.plot(x,y)

# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Line Plot')
# plt.show()

# Write a Python program to draw a line using given axis values with suitable label in the x axis , y axis and a title.

# x = [1,2,3,4,5]
# y = [11,55,2,3,4]

# plt.plot(x,y)

# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Line Plot')
# plt.show()

# Write a Python program to draw a line using given axis values taken from a text file, with suitable label in the x axis, y axis and a title.
# Test Data:
# test.txt
# 1 2
# 2 4
# 3 1

# x, y = [], []

# with open('test.txt', 'r') as file:
#     for line in file:
#         a, b = map(int, line.split())
#         x.append(a)
#         y.append(b)

# plt.plot(x, y)
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Line Plot')
# plt.show()

# Write a Python program to draw line charts of the financial data of Alphabet Inc. between October 3, 2016 to October 7, 2016.
# Sample Financial data (fdata.csv):
# Date,Open,High,Low,Close
# 10-03-16,774.25,776.065002,769.5,772.559998
# 10-04-16,776.030029,778.710022,772.890015,776.429993
# 10-05-16,779.309998,782.070007,775.650024,776.469971
# 10-06-16,779,780.47998,775.539978,776.859985
# 10-07-16,779.659973,779.659973,770.75,775.080017

# use sep, parse_Date, index column


# Write a Python program to plot two or more lines on same plot with suitable legends of each line.

# x1 = [1,2,3,4,5]
# y1 = [4,8,4,6,4]
# x2 = [1,2,3,4,5]
# y2 = [2,3,4,5,6]
# plt.plot(x1, y1, label='Line 1')
# plt.plot(x2, y2, label='Line 2')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Line Plot')
# plt.legend()
# plt.show()

# Write a Python program to plot two or more lines with legends, different widths and colors.

# x1 = [1,2,3,4,5]
# y1 = [1,8,4,6,4]
# x2 = [1,2,3,4,5]
# y2 = [2,3,9,5,6]
# plt.plot(x1, y1, label='Line 1', color='blue', lw=2)
# plt.plot(x2, y2, label='Line 2', color='red', lw=3)
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Line Plot')
# plt.legend()
# plt.show()

# Write a Python program to plot two or more lines with different styles.

# x1 = [1,2,3,4,5]
# y1 = [1,8,4,6,4]
# x2 = [1,2,3,4,5]
# y2 = [2,3,9,5,6]
# plt.plot(x1, y1, label='Line 1', color='blue', lw=2, ls='--')
# plt.plot(x2, y2, label='Line 2', color='red', lw=3, ls='-.')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Line Plot')
# plt.legend()
# plt.show()

# Write a Python program to display the current axis limits values and set new axis values.

# x = [1, 2, 3, 4, 5]
# y = [10, 20, 15, 25, 30]
# plt.plot(x, y)
# plt.xlim(1, 8)
# plt.ylim(5, 30)
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Axis Limits Example")
# plt.show()

