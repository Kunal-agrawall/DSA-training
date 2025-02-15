# List

# WAP to craete a ist with elements and apply list methods 
# list = [10,20,30,120,150,13.02,1589,1456]
# print(list)
# print("\n")
# list.sort()
# print(list)
# print("\n")
# list.append(0)
# print(list)
# list.reverse()
# print("\n")
# print(list)
# list.count(0)
# print("\n")
# print(list)
# //////////////////////////////////////////////
# WAP to sum all the items in a list
# list= [1,2,3,4,5,6,7,8,9]
# sum = 0
# for i in list:
#     sum += i

# print(sum)

# ///////////////////////////////////////
# WAP to get a list, sorted in increasing order by last element in each tuple from a given list of non-empty tuples
# Sample list: [(2,5), (1,2), (4,4), (2,3), (2,1)]
# Result: [(2,1), (1,2), (2,3),(4,4), (2,5)]
# list = [(2,5), (1,2), (4,4), (2,3), (2,1)]

# def last(n):
#     return n[-1]

# print(last(list))
# def sorted_list(tuples):
#     return sorted(tuples, key=last)
# print(sorted_list(list))

# SECOND METHOD

# def sort(list):
#     n=len(list)
#     for i in range(n):
#         for j in range(n):
#             if list[i][1]<list[j][1]:
#                 list[i],list[j]=list[j],list[i]
#     return list

# print(sort(list))


# ///////////////////////////////////////////////////////////
# WAP that takes two lists and returns True if they have at least one common member

# list1 = [1,2,3,4,5]
# list2 = [5,6,7,8]
# for i in range(len(list1)):
#     for j in range(len(list2)):
#         if list1[i]==list2[j]:
#             print("True")

# ///////////////////////////////////////////////
# WAP to sort a given list of non-empty tuples in increasing order by the sum of elements in each tuple
# Sample list: [(2,5), (1,2), (4,4), (2,3), (2,1)]
# result : [(1,2), (2,1), (2,3), (2,5), (4,4)]

# list = [(2,5), (1,2), (4,4), (2,3), (2,1), (5,5)]
# def add(n):
#     return n[0]+n[1]

# def sorted_list(tuples):
#     return sorted(tuples, key=sum)
# print(sorted_list(list))

# /////////////////////////////////////////////////////

# Tuple

# tup = (1,2,3,4,5,2,2)
# print(tup.count(2))

# tup1 = (10,20,30,120,150,13.02,1589,1456)
# print(tup1.index(30,0,5))
# print(len(tup1))

# /////////////////////////////////////////////////
# WAP to get the 4th element from the last element(end) of a tuple

# tup = (1,2,3,4,5)
# print(tup[-4])

# /////////////////////////////////////////////////////////////

# WAP to replace the last value of tuple in a list
# Sample list: [(10,20,40), (40,50,60), (70,80,90)]
# result: [(10,20,100), (40,50,100), (70,80,100)]

# lst = [(10,20,40), (40,50,60), (70,80,90)]
# for i in range(len(lst)):
#     lst[i] = (lst[i][0],lst[i][1],100)
# print(lst)

# /////////////////////////////////////////////////////////
# WAP to remove an empty tuple(s) from a list of tuples
# Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# result: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

# lst = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d', 'e')]
# lst = [i for i in lst if i != ()]
# print(lst)

# ////////////////////////////////////////////
# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8}
# print(set1.union(set2)) 
# print(set1.intersection(set2))
# print(set1.difference(set2))

# /////////////////////////////////////////
# WAP to find all the unique words and count the frequency of occurance from a given list of strings. Use Python set data type.
lst=  ['black', 'green', 'black', 'red', 'red', 'black', 'white', 'yellow', 'green', 'white']
unique = set(lst)
print(unique)
# /////////////////////////////////////////
# WAP to find the two numbers whose product is maximum among all the pairs in a given list of numbers. Use Python set data type.

lst1 = [1,2,3,4,5,6,7,8,9]
lst2 = [1,2,-1,-2,5,-8,8,10,7,20]


# //////////////////////////////////////////////////
# WAP to find all the unique combinations of 3 numbers from a given list of numbers, adding up to a given target number.
lst1 = [1,2,3,4,5,6,7,8,9]
