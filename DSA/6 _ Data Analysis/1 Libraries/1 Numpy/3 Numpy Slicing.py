import numpy as np

arr = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]
                ])

print(arr.shape)
print()

'''    arr[slice-row, slice-column]   '''

print(':3, ::3 -')
temp = arr[:3, ::3]
print(temp)
print()

print('1:3:1, 1:2:2 -')
temp = arr[1:3:1, 1:2:2]
print(temp)
print()

print('1:3:1, ::3 -')
temp = arr[1:3:1, ::3]
print(temp)
print()

print('::1, ::2 -')
temp = arr[::1, ::2]
print(temp)
print()

print('1:4:2, ::1 -')
temp = arr[1:4:2, ::1]
print(temp)
print()

print('1:2:1, ::2 -')
temp = arr[1:2:1, ::2]
print(temp)
print()

print('2:4:1, ::2 -')
temp = arr[2:4:1, ::2]
print(temp)
print()