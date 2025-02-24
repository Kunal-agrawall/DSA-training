a = [2,3,54,44.5,11.2,23]

# Inbuilt methods of List
a.append(12)        # Add element at the end of the list
a.extend([1,2,3,4]) # Add multiple elements at the end of the list
a.sort()            # Sort the list in ascending order
a.insert(0, 0)      # Insert element at the specified position
b = a.count(2)      # Count the number of occurrences of the specified element
b = a.index(3)      # Get the index of the first occurrence of the specified element
a.reverse()         # Reverse the list
a.remove(54)        # Remove the first occurrence of the specified element
a.pop()             # Remove the last element from the list
a.clear()           # Remove all elements from the list


# Sum
def sum(a):
    c = 0
    for i in a:
        c += i
    return c
a = [1,2,3,4,5]
print(sum(a))


# Sort From Back
def bsort(a):
    n = len(a)
    f = False
    for i in range(n):
        for j in range(n-i-1):
            if a[j][1] > a[j+1][1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                f = True
        if not f:
            return a
    return a

a = [(2,5),(1,2),(4,4),(2,3),(2,1)]
print(bsort(a))


# Check aleast one is equal
def checkOneEqual(a,b):
    for i in a:
        if i in b:
            return True
a = [1,2,3,4,5,6]
b = [6,7,8,9,0]
print(checkOneEqual(a,b))


# Sort a list of non empty tuples by their sum
def sort_tuples_by_sum(a):
    n = len(a)
    f = False
    for i in range(n):
        for j in range(n-i-1):
            if a[j][0]+a[j][1] > a[j+1][0]+a[j+1][1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                f = True
        if not f:
            return a
    return a

a = [(2,5),(1,2),(4,4),(2,3),(2,1)]
print(sort_tuples_by_sum(a))