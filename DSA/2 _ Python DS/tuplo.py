# a = 91,2,3,4,5,7,6,8,9,0

# b = a.__getitem__(2)
# print(b)

# b = a.__sizeof__()
# print(b)

# b = a.count(2)
# print(b)

# b = a.__add__((10,20))
# print(b)

# b = a.index(0)
# print(b)

# b = a.__contains__(91)
# print(b)

# b = a.__len__()
# print(b)


# Get 4th from last
a = 91,2,3,4,5,7,6,8,9,0
b = a[-4]
print(b)  


# Replace last value of each tuple
a = [(10,20,30),(40,50,60),(70,80,90)]
for i in range(len(a)):
    a[i] = a[i][0], a[i][1], 100
    
print(a)


# Remove empty tuples
a = [(), (), ("",), ('a','b')]
print([i for i in a if i!=()])