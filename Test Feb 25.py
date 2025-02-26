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

print(titanic[titanic["age"].isnull()])
