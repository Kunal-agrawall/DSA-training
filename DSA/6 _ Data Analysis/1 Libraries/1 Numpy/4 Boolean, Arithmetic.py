import numpy as np

arr = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]
                ])

# Boolean Ops
cond = arr>5
temp = arr[cond]
print(temp)


# Arithmetic Ops
arr += 5
arr -= 4
arr *= 1
print((arr*2)//4)