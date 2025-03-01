import pandas as pd # Data manipulation
import numpy as np # Linear algebra
import warnings # Ignore warnings
import seaborn as sns #plots
import matplotlib.pyplot as plt # plots

df = pd.read_csv('insurance.csv')
# print(df.head())

# print({col:list(df[col].unique()) for col in df.select_dtypes("object")})
# for col in df.select_dtypes("int"):
#     print(col)

