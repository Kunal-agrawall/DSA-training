import numpy as np
from numpy import array, arange

arr = array([[10,20,30],
                [40,50,60],
                [70,80,90],
                [100,110,120]])
print(arr)

print(type(arr))
print(arr.shape)
print(arr.ndim)
print()

a = arange(24)
print(a.reshape(3,4,2))