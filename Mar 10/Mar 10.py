# -*- coding: utf-8 -*-
"""Mar 10, 2025.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/126Nrhdda6wydADFxJYwhNrDBdzFECiJP

1. Calculate Basic Statistics of a Dataset
You have a dataset containing the following columns:

ID: Unique identifier of a person.
Age: Age of the person.
Salary: Annual salary of the person.
Using Pandas, write a function to:

Calculate the mean, median, and standard deviation of Age and Salary.
Find the person with the highest salary and their age.
"""

import pandas as pd

def calculate_statistics(df):
    stats = df[['Age', 'Salary']].agg(['mean', 'median', 'std'])
    highest_salary_person = df.loc[df['Salary'].idxmax(), ['ID', 'Age', 'Salary']]

    return stats, highest_salary_person

# Example usage
data = {'ID': [1, 2, 3, 4, 5], 'Age': [25, 30, 35, 40, 45], 'Salary': [50000, 60000, 70000, 80000, 90000]}
df = pd.DataFrame(data)

stats, highest_salary_person = calculate_statistics(df)
print(stats)
print(highest_salary_person)

"""2. Generate Random Data and Perform Analysis
Create a NumPy array of 1000 random integers between 10 and 100. Then:

Calculate the mean, median, and standard deviation of the array.
Create a histogram of the random numbers using Matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.random.randint(10, 100, 1000)

mean_val = np.mean(data)
median_val = np.median(data)
std_dev = np.std(data)

plt.hist(data, bins=20, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Random Integers')
plt.show()
print("\n")
print(f"Mean: {mean_val}, Median: {median_val}, Std Dev: {std_dev}")

"""3. Temperature Data Analysis
Given a CSV file temperature_data.csv with the columns Date (in 'YYYY-MM-DD' format) and Temperature (Celsius):

Calculate the average temperature for each month.
Plot the temperature trend over the course of the year.
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:\my desk\Coding\Training\Mar 10\daily_temperatures.csv", parse_dates=["Date"])

df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month

monthly_avg = df.groupby("Month")["Temperature"].mean()

plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["Temperature"], label="Daily Temperature", alpha=0.6)
plt.plot(monthly_avg.index, monthly_avg.values, marker="o", linestyle="-", color="red", label="Monthly Avg Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Trend Over the Year")
plt.xticks(range(1, 13), ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
plt.legend()
plt.grid()
plt.show()

print("\n")
print(monthly_avg)

"""4. Time Series Data: Moving Average
Given a time series data of daily sales for a product (with columns Date and Sales), calculate and plot a 7-day moving average of the sales data. Use Pandas to load the data, compute the moving average, and visualize the results with Matplotlib.

"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:\my desk\Coding\Training\Mar 10\sales_data.csv", parse_dates=["Date"])
df = df.sort_values("Date")
df["7-day MA"] = df["Sales"].rolling(window=7).mean()

plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["Sales"], label="Daily Sales")
plt.plot(df["Date"], df["7-day MA"], linestyle="-", color="red", label="7-day Moving Average")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.title("7-Day Moving Average of Sales")
plt.legend()
plt.grid()
plt.show()

"""5. Find Correlation Between Two Variables
Given a Pandas DataFrame with columns Height and Weight, calculate the Pearson correlation coefficient between the two. Then visualize the relationship with a scatter plot using Matplotlib.
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:\my desk\Coding\Training\Mar 10\height_weight_data.csv")
correlation = df["Height"].corr(df["Weight"])
print(f"Pearson Correlation Coefficient: {correlation:.2f}")
print("\n")

plt.figure(figsize=(8, 5))
plt.scatter(df["Height"], df["Weight"], alpha=0.6)
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.title("Height vs. Weight Relationship")
plt.grid()
plt.show()

"""6. Group Data and Compute Aggregates
You have a Pandas DataFrame with the following columns: Region, Product, and Sales. Write a function to:

Calculate the total sales for each region.
Find the average sales per product for each region.
Create a bar plot of the total sales by region.
"""

df = pd.DataFrame({'Region': ['North', 'South', 'North', 'South', 'East'],
                   'Product': ['A', 'B', 'A', 'C', 'B'],
                   'Sales': [100, 200, 150, 300, 250]})

total_sales_by_region = df.groupby('Region')['Sales'].sum()
avg_sales_per_product = df.groupby(['Region', 'Product'])['Sales'].mean()

total_sales_by_region.plot(kind='bar', title='Total Sales by Region', color='skyblue')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.show()

print(total_sales_by_region)
print(avg_sales_per_product)

"""7. Find the Outliers in a Dataset
Given a dataset containing the Age and Income of 1000 people, write a function to:

Identify outliers in Income using the Z-score method.
Remove the outliers and plot a histogram of the cleaned Income data.
"""



"""8. Data Filtering and Plotting
Given a dataset student_scores.csv with columns Student_ID, Math_Score, English_Score, and Science_Score, write a function to:

Filter out students with a Math score greater than 80.
Create a bar plot comparing the English and Science scores for these students.

"""

df = pd.read_csv('D:\my desk\Coding\Training\Mar 10\student_scores.csv')

filtered_students = df[df['Math_Score'] > 80]
filtered_students[['English_Score', 'Science_Score']].plot(kind='bar')
plt.xlabel('Student ID')
plt.ylabel('Scores')
plt.title('Comparison of English and Science Scores for High Math Scorers')
plt.show()

"""9. Simulating a Normal Distribution
Using NumPy, simulate 1000 random data points that follow a normal distribution with a mean of 50 and a standard deviation of 10. Then:

Plot a histogram of the data.
Calculate the percentage of values that are above 60.

"""

data = np.random.normal(50, 10, 1000)

plt.hist(data, bins=30, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Normally Distributed Data')
plt.show()

above_60 = np.sum(data > 60) / len(data) * 100
print(f"Percentage of values above 60: {above_60:.2f}%")

"""10. Visualizing Relationships Between Multiple Variables
Given a dataset with columns Age, Height, and Weight, create:

A scatter plot matrix (pairplot) to visualize the relationships between all pairs of variables.
A heatmap of the correlation matrix between Age, Height, and Weight.


"""

import seaborn as sns

df = pd.DataFrame({'Age': np.random.randint(18, 60, 100),
                   'Height': np.random.randint(150, 200, 100),
                   'Weight': np.random.randint(50, 100, 100)})

sns.pairplot(df)
plt.show()

sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix Heatmap')
plt.show()

"""11. You are given a dataset containing information about daily temperatures in a city over a year. The dataset consists of two columns:

Date: The date (in format 'YYYY-MM-DD')
Temperature: The temperature on that date in Celsius.
"""

df = pd.read_csv('D:\my desk\Coding\Training\Mar 10\daily_temperatures.csv', parse_dates=['Date'])
df['Month'] = df['Date'].dt.month

monthly_avg_temp = df.groupby('Month')['Temperature'].mean()
print(monthly_avg_temp)

plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Temperature'], label='Temperature')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Trend Over the Year')
plt.legend()
plt.show()