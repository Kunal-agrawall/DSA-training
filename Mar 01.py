# def split_palindrome(s):
#     n = len(s)
#     for i in range(1, n):  # Try splitting at different points
#         left, right = s[:i], s[i:]
#         if left == left[::-1] and right == right[::-1]:  # Check if both are palindromes
#             return left, right
#     return "No valid split"

# s = "abaaba"
# result = split_palindrome(s)
# print(result)  # Output: ('aba', 'aba')


import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame (Replace this with your actual data)
data = {
    "age": [20, 30, 40, 50, 60],
    "bmi": [18, 22, 25, 30, 35],
    "charges": [1000, 2000, 3000, 4000, 5000]
}

df = pd.DataFrame(data)

# Calculate percentages
df_percentage = df.div(df.sum()) * 100

# Plotting
df_percentage.plot(kind='bar', figsize=(8, 5))
plt.title("Percentage Contribution of Each Column")
plt.ylabel("Percentage")
plt.xlabel("Index")
plt.legend(title="Categories")
plt.show()
