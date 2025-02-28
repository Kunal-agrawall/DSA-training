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

Employee = namedtuple("Employee", ['name', 'age', 'department', 'salary'])
emp1 = Employee("Rahul", 30, "HR", 50000)
emp2 = Employee("Satyam", 28, "IT", 60000)
emp3  = Employee("Kunal", 21, "Finance", 70000)

print(emp1.name, emp1.department, emp1.salary)
print(emp2.name)
print(emp3.name,  emp3.age)

