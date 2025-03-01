import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


'''
Given two sorted arrays of integers, find the median of the two sorted arrays. 
find_median_sorted_arrays([1,3], [2])
output: 2.0
'''

# def find_median_sorted_arrays(num1, num2):
#     merged_arr = sorted(num1 + num2)
#     length = len(merged_arr)
#     if length % 2 == 0:
#         return (merged_arr[length//2 - 1] + merged_arr[length//2]) / 2
#     else:
#         return merged_arr[length//2]

# a = find_median_sorted_arrays([1,3], [2])
# print(a)

# //////////////////////////////////////////////////////////////////////////////////////////////////



'''
Given a dataframe with multiple columns (e.g., category, sales, region), perform a complex aggregation where you calculate
the total sales for each category per region, as well as the percentage of the total sales by each category in each region.
df = pd.DataFrame({
    'category': ['A', 'B', 'A', 'B', 'A'],
   'sales': [100, 200, 150, 300, 50],
   'region': ['East', 'West', 'East', 'West', 'East']
})
result = complex_aggregation(df)
output: DataFrame with the total sales and the percentage for each category
'''


'''
Write a function to find the longest palindromic substring in a given string.
longest_palindromic_substring("babad")
output: "bab" or "aba"
'''

# def longest_palindromic_substring(s):
#     if len(s) <= 1:
#         return s
#     max_length = 1
#     start = 0
#     for i in range(len(s)):

# //////////////////////////////////////////////////////////////////////////////////////////////////



'''
Given two DataFrames, perform a conditional merge where you only merge rows based on multiple conditions 
(e.g. merge on two columns, but only when another condition on a third column is met).

df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'value' : [10, 20, 30],
    'region' : ['East', 'West', 'East']
})

df2 = pd.DataFrame({
    'id': [1,2,3],
    'value' : [100, 200, 300],
    'category' : ['A', 'B', 'A']
})
merged_df = conditional_merge(df1, df2, condition_column= 'region')
'''


# /////////////////////////////////////////////////////////////////////

'''
Given a 2D NumPy array representing a matrix of values, create a heatmap with a custom  colormap. Label the axes and add
a color bar to indicate the range of values.
'''

# data = np.random.rand(10, 10)

# /////////////////////////////////////////////////////////////////////

'''
Given a large multivariate dataset (e.g., a DataFrame with multiple numerical columns), use seaborn.pairplot() or matplotlib
to create a matrix of scatter plots for each pair of variables. Add custom labels and legends to the plot.

import seaborn as sns
df = pd.DataFrame(np.random.rand(100, 5), columns=['A', 'B', 'C', 'D', 'E'])
plot_pairplot(df)
'''

# df = pd.DataFrame(np.random.rand(100, 5), columns=['A', 'B', 'C', 'D', 'E'])
# sns.pairplot(df)
# plt.show()

# ///////////////////////////////////////////////////////////////////////////