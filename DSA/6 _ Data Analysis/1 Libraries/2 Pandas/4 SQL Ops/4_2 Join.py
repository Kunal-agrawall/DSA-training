import pandas as pd

'''
Types of Joins:
    1. INNER JOIN: Returns records that have matching values in both tables.

    2. LEFT JOIN: Returns all records from the left table, and the matched records from
       the right table. If there is no match, the result will contain NULL on the right
       side.

    3. RIGHT JOIN: This is similar to the LEFT JOIN, but returns all records from
       the right table, and the matched records from the left table.

    4. FULL OUTER JOIN: Returns all records when there is a match in either left or
       right table records.
'''

data1 = {
    'Name':['Rahul', 'Prince', 'Gaurav', 'Anuj'],
    'Age':[20, 21, 19, 18],
    'Address':['Delhi', 'Mumbai', 'Kolkata', 'Chennai'],
    'Qualification':['MSC', 'MA', 'MBA', 'MCA'],
    'Contact':['1234567890', '9876543210', '1111111111', '2222222222']
}

data2 = {
    'Name':['Abhi', 'Ayushi', 'Vanshika Moti', 'Sarita'],
    'Age':[22, 17, 20, 21],
    'Address':['Mumbai', 'Agra', 'N. Korea', 'Kolkata'],
    'Qualification':['MSC', 'MA', 'MBA', 'MCA'],
    'Gmail':['abc', 'def', 'ghi', 'jkl']
}

n1, n2 = len(data1['Name']), len(data2['Name'])
df1 = pd.DataFrame(data1, index=[i for i in range(n1)])
df2 = pd.DataFrame(data2, index=[i for i in range(n1, n1+n2)])

y = pd.concat([df1, df2], axis=0, join='inner')
z = pd.concat([df1, df2], axis=1, sort=False)
print(z)