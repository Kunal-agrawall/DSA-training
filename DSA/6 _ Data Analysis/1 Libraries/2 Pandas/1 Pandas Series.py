import pandas as pd

dict = {}
for i in range(1,27):
    dict[chr(96+i)] = i
df = pd.Series(dict)
# print(df)


# When data contains ndarray
data = [[1,2,3], [4,5,6], [7,8,9], [10]]
df = pd.Series(data)
print(df)