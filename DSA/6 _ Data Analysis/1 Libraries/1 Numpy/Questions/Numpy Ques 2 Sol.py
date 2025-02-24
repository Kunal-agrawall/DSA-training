# Q1
import numpy as np
lst = [1,2,3,4,5,6,7]
tup = (1,2,3,4,5,6,7)
arr = np.array([lst, tup])
print(arr)

# Q2
a = np.empty((3,3)) # Empty array


# Q3
a = np.array([100+6j, 150+3j])
print(f"Real Part : {a.real}")
print(f"Imag Part : {a.imag}")


# Q4
a = np.array([1,2,3])
print(f"Size of array    : {a.size}")
print(f"Memory of 1 item : {a.nbytes//a.size}")
print(f"Memory of array  : {a.nbytes}")


# Q5
a = np.array([1,2,3,4,5,6])
b = np.array([5,6,7,8,9,0])
# print(c)
