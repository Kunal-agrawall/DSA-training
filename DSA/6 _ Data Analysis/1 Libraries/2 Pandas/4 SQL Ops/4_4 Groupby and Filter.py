'''
    Retrieve the department name and the highest salary in each department 
    from the employee dataset, but only for departments where the highest salary 
    is greater than $70,000.
'''

import pandas as pd

# Sample data
data = {'Department': ['Sales', 'Sales', 'HR', 'HR', 'Engineering', 'Engineering'],
        'Salary': [60000, 80000, 75000, 65000, 72000, 90000]}
df = pd.DataFrame(data)

'''
    Group and Filter: Use groupby() to find the highest salary in each department, 
    then filter based on the condition.
'''

# Group by department and find max salary
result = df.groupby('Department')['Salary'].max().reset_index()

# Filter departments with highest salary > 70000
result = result[result['Salary'] > 70000]
print(result)