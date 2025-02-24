import numpy as np

a = np.array([1,3,5])
b = np.array([[1,2,3], [4,5,6]], dtype='int')
c = b.T
d = np.zeros((3,4)) # Row, Column
e = np.full((3,3), 4, dtype='int')
f = np.random.random((2,2))
g = np.linspace(0,5,9)
h = np.arange(0,30,2)

print("Array 1D:\n", a, '\n_____________________\n')
print("Array 2D:\n", b, '\n_____________________\n')
print("Array Transpose:\n", c, '\n_____________________\n')
print("Array Zeroes:\n", d, '\n_____________________\n')
print("Array Full:\n", e, '\n_____________________\n')
print("Array Random:\n", f, '\n_____________________\n')
print("Array Linespace:\n", g, '\n_____________________\n')
print("Array Arange:\n", h, '\n_____________________\n')

print("\nUnary Operations:")
a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print(f"Largest element      : {a.max()}")
print(f"Largest row-wise     : {a.max(axis=1)}")
print(f"Smallest column-wise : {a.min(axis=0)}")
print(f"Sum of all array     : {a.sum()}")
print(f"Commulative sum each for row : \n{a.cumsum(axis=1)}")