import numpy as np

'''
3. Write a function to find the k-th largest element in a given 1D NumPy array using NumPy functions.
'''

# def A(arr, k):
#     kth_largest = np.partition(arr, -k)[-k]
#     return kth_largest

# arr = np.array([12,3,5,7,19])
# print(A(arr, 2))  

# /////////////////////////////////////////////////////////////////////////////

'''
1. Given a square matrix, write a function to rotate the matrix by 90 degree clockwise in-place.
'''

# def rotate_matrix(a):
#     return np.rot90(a, -1)

# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(rotate_matrix(arr))
# //////////////////////////////////////////////////////////////////////////

'''
4. Write a function that takes a NumPy array and returns the count of each unique element in the array as a dictionary.
'''

# def count_unique(arr):
#     return {i: np.count_nonzero(arr == i) for i in arr}

# arr = np.array([1,2,2,3,4,4,4,5])
# print(count_unique(arr))

# //////////////////////////////////////////////////////////////////

'''
8. Write a function that returns the number of non-zero elements in a matrix A.
'''

# def non_zero(A):
#     return np.count_nonzero(A)

# A = np.array([[1,0,0], [2,3,0], [0,4,5]])
# print(non_zero(A))

# //////////////////////////////////////////////////////////////////////

'''
9. You are given an array arr that contains n-1 ditinct numbers in the range frthe om 1 to n.
One number is missing from array. Write a function to find the missing number.
'''

# def find_missing(arr):
#     n = len(arr) + 1
#     formula_sum = n * (n + 1) // 2
#     actual_sum = sum(arr)
#     return formula_sum - actual_sum

# arr = np.array([1,2,4,6,3,7,8])
# print(find_missing(arr))

# //////////////////////////////////////////////////////////////////

'''
10. Write a function that calculates the sum of diagonal elements of a square matrix.
'''

# def diagonal_sum(a):
#     return np.trace(a)

# arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
# print(diagonal_sum(arr))

# ////////////////////////////////////////////////////////////////////////////////////

''''
7. Implement matrix multiplication between two matrices A and B without using np.dot or np.matmul. Ensure that the
number of columns in A is equal to the number of rows in B.
''' 

# def matrix_multiply(a,b):
#     return a@b

# arr1 = np.array([[1,2], [3,4]])
# arr2 = np.array([[5,6], [7,8]])
# print(matrix_multiply(arr1, arr2))

# //////////////////////////////////////////////////////////////////////////////////////

'''
5. Given an array A with shape (m,n), write a function to reshape the array into a new shape (p,q),
such that p*q == m*n. If this is not possible, return None. 
'''

# def reshape(A, p, q):
#     if p*q != A.shape[0]*A.shape[1]:
#         return None
#     return A.reshape(p, q)

# arr = np.array([[1,2], [3,4]])
# print(reshape(arr,2,2))

# //////////////////////////////////////////////////////////////////////////////////////