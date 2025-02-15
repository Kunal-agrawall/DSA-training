# Sort a list of tuples by the first element in each tuple.
# Sample List: [(5, 1), (2, 4), (3, 3), (1, 2)]

# Expected Output:
# [(1, 2), (2, 4), (3, 3), (5, 1)]
# Explanation: The tuples are sorted by the first element. The sorted list is: [(1, 2), (2, 4), (3, 3), (5, 1)].

# list = [(5, 1), (2, 4), (3, 3), (1, 2)]
# sorted_list = sorted(list, key=lambda x: x[0])
# print(sorted_list)

# ///////////////////////////////////////////////////////////////////

'''Sort a list of tuples by the sum of the elements in each tuple.
Sample List: [(1, 2), (2, 3), (3, 1), (4, 2)]

Expected Output:
[(1, 2), (3, 1), (4, 2), (2, 3)]
Explanation: The tuples are sorted based on the sum of their elements. Sum of elements in the tuples:

(1, 2) → 3
(2, 3) → 5
(3, 1) → 4
(4, 2) → 6
The sorted list by sum of elements: [(1, 2), (3, 1), (4, 2), (2, 3)].'''

# list = [(1, 2), (2, 3), (3, 1), (4, 2)]
# sorted_list = sorted(list, key=lambda x: sum(x))
# print(sorted_list)

# ///////////////////////////////////////////////////////////////////////////

'''Sort a list of tuples in reverse order based on the first element in each tuple.
Sample List: [(3, 4), (1, 2), (5, 1), (2, 3)]

Expected Output:

python
Copy
[(5, 1), (3, 4), (2, 3), (1, 2)]
Explanation: The tuples are sorted by the first element in reverse order: 5 > 3 > 2 > 1.
'''

# list = [(3, 4), (1, 2), (5, 1), (2, 3)]
# sorted_list = sorted(list, key=lambda x: x[0], reverse=True)
# print(sorted_list)

# ///////////////////////////////////////////////////////////////////////////

'''Group tuples by the first element in each tuple and sort the groups by the last element.
Sample List: [(2, 5), (1, 2), (2, 3), (1, 1), (2, 4)]

Expected Output:
[(1, 1), (1, 2), (2, 3), (2, 4), (2, 5)]
Explanation: First, the list is grouped by the first element (1 and 2), and then each group is sorted by the second element. The final result is [(1, 1), (1, 2), (2, 3), (2, 4), (2, 5)].
'''

# list = [(2, 5), (1, 2), (2, 3), (1, 1), (2, 4)]
# result = sorted(list, key=lambda x: (x[0], x[1]))
# print(result)

# ///////////////////////////////////////////////////////////////////////////

'''Sort a list of tuples by the length of each tuple.
Sample List: [(1, 2), (1, 2, 3), (4,), (2,)]

Expected Output:
[(4,), (2,), (1, 2), (1, 2, 3)]
Explanation: The tuples are sorted by their length: [(4,), (2,), (1, 2), (1, 2, 3)].
'''

# list = [(1, 2), (1, 2, 3), (4,), (2,)]
# sorted_list = sorted(list, key=len)
# print(sorted_list)

# ///////////////////////////////////////////////////////////////////////////

'''Sort a list of tuples by the first element, and in case of a tie, by the second element.
Sample List: [(1, 3), (1, 2), (2, 4), (2, 3)]

Expected Output:

[(1, 2), (1, 3), (2, 3), (2, 4)]
Explanation: The tuples are first sorted by the first element. If two tuples have the same first element, they are then sorted by the second element. The result is: [(1, 2), (1, 3), (2, 3), (2, 4)].
'''

# list = [(1, 3), (1, 2), (2, 4), (2, 3)]
# list.sort(key=lambda x: x[0])
# list.sort(key=lambda x: x[1])
# print(list)

# ///////////////////////////////////////////////////////////////////////////

'''Find the tuple with the maximum sum of elements from a list of tuples.
Sample List: [(1, 2), (3, 1), (5, 2), (4, 3)]

Expected Output:
(5, 2)
Explanation: The sum of the elements in the tuples:

(1, 2) → 3
(3, 1) → 4
(5, 2) → 7
(4, 3) → 7
The tuple with the maximum sum is (5, 2) or (4, 3) (since both have the same sum of 7). In case of a tie, the tuple that appears first is chosen.
'''

# list = [(1, 2), (3, 1), (5, 2), (4, 3)]
# max_sum = max(list, key=lambda x: sum(x))
# print(max_sum)

# ///////////////////////////////////////////////////////////////////////////

'''Find the tuple with the minimum first element in a list of tuples.
Sample List: [(4, 5), (2, 3), (1, 6), (3, 2)]

Expected Output:
(1, 6)
Explanation: The tuple with the minimum first element is (1, 6).
'''

# list = [(4, 5), (2, 3), (1, 6), (3, 2)]
# result = min(list, key=lambda x: x[0])
# print(result)

# ///////////////////////////////////////////////////////////////////////////

'''Sort a list of tuples by the second element, but if two second elements are equal, sort by the first element.
Sample List: [(3, 5), (1, 4), (2, 4), (4, 5)]

Expected Output:
[(1, 4), (2, 4), (3, 5), (4, 5)]
Explanation: The tuples are first sorted by the second element, and if the second elements are equal, they are sorted by the first element.
'''

# list = [(3, 5), (1, 4), (2, 4), (4, 5)]
# list.sort(key=lambda x: x[1])
# list.sort(key=lambda x: x[0])
# print(list)

# ///////////////////////////////////////////////////////////////////////////

''' Create a new list of tuples where each tuple contains the sum of the elements from the original list of tuples. Sort it in increasing order of the sum.
Sample List: [(1, 3), (2, 1), (4, 2), (3, 1)]

Expected Output:
[(2, 1), (3, 1), (1, 3), (4, 2)]
Explanation: First, calculate the sum of elements in each tuple:

(1, 3) → 4
(2, 1) → 3
(4, 2) → 6
(3, 1) → 4
After sorting by sum: [(2, 1), (3, 1), (1, 3), (4, 2)].
'''

# sample_list = [(1, 3), (2, 1), (4, 2), (3, 1)]
# sorted_list = sorted(sample_list, key=lambda x: sum(x))

# print(sorted_list)


# /////////////////////////////////////////////////////////////////

'''Merge Sorted Lists:
 Given two sorted lists, write a Python function to merge them into a single sorted list without using the sorted() function.'''

# def merge_lists(list1, list2):
#     merged_list = []
#     while list1 and list2:
#         merged_list.append((list1 if list1[0] < list2[0] else list2).pop(0))
#     return merged_list + list1 + list2

# list1 = [1, 3, 5]
# list2 = [2, 4, 6]
# result = merge_lists(list1, list2)
# print(result) 

# ///////////////////////////////////////////////////////////////////////////

'''Rotate List: 
Write a Python function that rotates a list to the right by k positions. 
(For example, [1, 2, 3, 4, 5] rotated by 2 positions becomes [4, 5, 1, 2, 3]).'''

# def rotate_list(nums, k):
#     k = k % len(nums)  # to handle the case where k is larger than the list size
#     return nums[-k:] + nums[:-k]

# # Example usage:
# nums = [1, 2, 3, 4, 5]
# k = 2
# rotated_list = rotate_list(nums, k)
# print(rotated_list)  # Output: [4, 5, 1, 2, 3]

# ///////////////////////////////////////////////////////////////////////////

'''Find the Longest Increasing Subsequence: Given a list of integers, 
write a Python function that returns the longest increasing subsequence.'''






# ///////////////////////////////////////////////////////////////////////////////////

'''Group Anagrams: 
Write a function that takes a list of strings and groups them into anagrams (i.e., strings that are anagrams of each other).'''

# def group_anagrams(strs):
#     anagram_dict = {}
#     for word in strs:
#         sorted_word = ''.join(sorted(word))
#         if sorted_word in anagram_dict:
#             anagram_dict[sorted_word].append(word)
#         else:
#             anagram_dict[sorted_word] = [word]
#     return list(anagram_dict.values())


# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# result = group_anagrams(strs)
# print(result)

# ///////////////////////////////////////////////////////////////////////////////////

'''Nested List Flattening: 
Write a Python program that flattens a nested list of lists into a single list (e.g., [[1, 2], [3, [4, 5]], 6] becomes [1, 2, 3, 4, 5, 6]).'''

# def flatten_list(nested_list):
#     flattened_list = []
#     for item in nested_list:
#         if isinstance(item, list):
#             flattened_list.extend(flatten_list(item))
#         else:
#             flattened_list.append(item)
#     return flattened_list

# nested_list = [[1, 2], [3, [4, 5]], 6]
# result = flatten_list(nested_list)
# print(result)

# ///////////////////////////////////////////////////////////////////////////////////

'''Tuple Comparison: 
Write a function that compares two tuples element by element and returns True if all elements are equal, otherwise False.'''

# def compare_tuples(tuple1, tuple2):
#     if len(tuple1) != len(tuple2):
#         return False
#     for i in range(len(tuple1)):
#         if tuple1[i] != tuple2[i]:
#             return False
#     return True

# tuple1 = (1, 2, 3)
# tuple2 = (1, 2, 3)
# result = compare_tuples(tuple1, tuple2)
# print(result)  # Output: True

# //////////////////////////////////////////////////////////////////

'''Find the Second Largest Element: 
Write a Python function that returns the second largest element in a tuple without converting it to a list.'''

# def second_largest(data):
#     largest, second = float('-inf'), float('-inf')
#     for num in data:
#         largest, second = (num, largest) if num > largest else (largest, max(second, num))
#     return second if second != float('-inf') else None

# print(second_largest((10, 5, 8, 3, 7, 19)))

# ///////////////////////////////////////////////////////////////////////////

'''Tuple to Dictionary: 
Write a function that takes a list of tuples where each tuple contains two elements (key, value), and converts them into a dictionary.'''

# def tuple_to_dict(tuples):
#     dictionary = {}
#     for key, value in tuples:
#         dictionary[key] = value
#     return dictionary

# tuples = [('apple', 10), ('banana', 20), ('cherry', 30)]
# result = tuple_to_dict(tuples)
# print(result) 

# /////////////////////////////////////////////////////////////////////////////////////////

'''Count Occurrences in Tuple: 
Given a tuple of elements, write a Python function that counts the frequency of each element using a dictionary and returns it.
'''

# def count_occurrences(tuple):
    # occurrences = {}
    # for element in tuple:
    #     if element in occurrences:
    #         occurrences[element] += 1
    #     else:
    #         occurrences[element] = 1
    # return occurrences

# tuple = (1, 2, 3, 2, 4, 3, 2)
# result = count_occurrences(tuple)
# print(result)  # Output: {1: 1, 2: 3, 3: 2, 4: 1}

# //////////////////////////////////////////////////////////////////

'''Find Symmetric Difference: 
Write a Python function that takes two sets and returns their symmetric difference (elements that are in one set or the other, but not both).
'''

# def symmetric_difference(set1, set2):
    # return set1.symmetric_difference(set2)

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# result = symmetric_difference(set1, set2)
# print(result)  

# //////////////////////////////////////////////////////////////////

'''Set Operations on Multiple Sets: 
Given multiple sets, write a Python program to find the union, intersection, and difference for all the sets.
'''
# def set_operations(*sets):
#     union_set = set.union(*sets)
#     intersection_set = set.intersection(*sets)
#     difference_set = set.difference(*sets)
    
#     return union_set, intersection_set, difference_set

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# set3 = {4, 6, 7, 8}

# union_result, intersection_result, difference_result = set_operations(set1, set2, set3)

# print("Union:", union_result)
# print("Intersection:", intersection_result)
# print("Difference:", difference_result)

# //////////////////////////////////////////////////////////////////////////////////////////////////

'''Check for Subset and Superset: 
Write a Python function that takes two sets and checks if one is a subset or superset of the other.
'''

# def is_subset_or_superset(set1, set2):
    # return set1.issubset(set2) or set1.issuperset(set2)

# set1 = {1, 2, 3, 4}
# set2 = {1, 2, 3}
# result = is_subset_or_superset(set1, set2)
# print(result) 

# ////////////////////////////////////////////////////////////////////////////////////

'''Set of Frozensets: 
Create a set that contains frozensets. Perform set operations (e.g., union, intersection) on it.
'''

# set_of_frozensets = {frozenset({1, 2, 3}), frozenset({3, 4, 5}), frozenset({5, 6, 7})}
# union_result = set().union(*set_of_frozensets)
# intersection_result = set_of_frozensets.pop()  

# for fs in set_of_frozensets:
#     intersection_result = intersection_result.intersection(fs)

# print("Set of Frozensets:", set_of_frozensets)
# print("Union:", union_result)
# print("Intersection:", intersection_result)

# ////////////////////////////////////////////////////////////////////////////////////

'''Remove Elements from List and Set: 
Given a list and a set, write a function that removes the elements from the list that exist in the set, without modifying the original set.
'''

# def remove_elements(lst, s):
#     lst_without_s = [x for x in lst if x not in s]
#     return lst_without_s

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# s = {3, 4, 5, 6, 7, 8}
# result = remove_elements(lst, s)
# print("List:", result)

# ////////////////////////////////////////////////////////////////////////////////////

'''Find the Intersection of a List of Tuples: 
Given a list of tuples (each tuple has two elements), write a Python function to find the intersection of the first elements of all the tuples and return the result as a set.'''

# def find_intersection(tuples):
    # intersection = set(tuples[0])
    # for t in tuples[1:]:
    #     intersection &= set(t)
    # return intersection

# tuples = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
# result = find_intersection(tuples)
# print("Intersection:", result)  # Output: {2, 3, 4, 5}

# ////////////////////////////////////////////////////////////////////////////////

'''Merge List of Sets:
Write a function that takes a list of sets and merges them into one set, removing any duplicate elements.'''

# def merge_sets(sets):
    # return set().union(*sets)

# sets = [{1, 2, 3}, {3, 4, 5}, {5, 6, 7}]
# result = merge_sets(sets)
# print("Merged Set:", result ) 

# /////////////////////////////////////////////////////////

'''List and Tuple Frequency: 
Given a list and a tuple, write a Python program to count how many times the elements from the tuple appear in the list.'''

# def count_frequency(lst, tup):
    # freq = {}
    # for element in tup:
    #     if element in lst:
    #         freq[element] = lst.count(element)
    # return freq

# lst = [1, 2, 3, 2, 4, 3, 2]
# tup = (2, 3)
# result = count_frequency(lst, tup)
# print("Frequency:", result)
