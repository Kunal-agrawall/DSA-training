import numpy as np

# Q1
a = [12.23, 13.32, 100, 36.32]
arr = np.array(a)

# Q2
arr = np.arange(2,11).reshape(3,3)

# Q3
arr = np.zeros((10))
arr[5] = 11


# Q4
arr = np.array([1,2,3,4,5,6])
arr = arr[::-1]


# Q5
arr = np.array([1,2,3,4,5,6])
arr = np.array(arr, dtype='float')

# Q6
arr = np.ones((5,5))
a[0] = 0
print(arr)
