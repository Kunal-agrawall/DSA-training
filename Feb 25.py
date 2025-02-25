import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
# Show first few rows of dataset
# print(titanic.head) 

# Check for null values
myNull = titanic.isnull().sum()
# print(myNull)


# min and max age
# print(titanic['age'].min())
# print(titanic['age'].max())

z = (titanic[titanic["age"].isnull()])
temp = z
print(temp)


# Basic information about the dataset
# print(titanic.info())

# Descriptive statistics
# print(titanic.describe())

titanic['age'].fillna(titanic['age'].mean(), inplace=True)
print(temp)
print(titanic.isnull().sum())
# titanic['embarked'].fillna(titanic['embarked'].mode()[0], inplace=True)

# show the values which was filled in place of null values

# print(titanic)
# print(titanic.isnull().sum())