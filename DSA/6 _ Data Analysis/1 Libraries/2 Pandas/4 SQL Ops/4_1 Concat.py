# Merging, Joining, Concat
import pandas as pd

data1 = {
    'Name':['Rahul', 'Prince', 'Gaurav', 'Anuj'],
    'Age':[20, 21, 19, 18],
    'Address':['Delhi', 'Mumbai', 'Kolkata', 'Chennai'],
    'Qualification':['MSC', 'MA', 'MBA', 'MCA']
}

data2 = {
    'Name':['Abhi', 'Ayushi', 'Vanshika Moti', 'Sarita'],
    'Age':[22, 17, 20, 21],
    'Address':['Mumbai', 'Agra', 'N. Korea', 'Kolkata'],
    'Qualification':['MSC', 'MA', 'MBA', 'MCA']
}


# Concat
n1, n2 = len(data1['Name']), len(data2['Name'])
df1 = pd.DataFrame(data1, index=[i for i in range(n1)])
df2 = pd.DataFrame(data2, index=[i for i in range(n1, n1+n2)])


# With some different columns 
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
# print(pd.concat([df1, df2]))



# Apply Append
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
y = df1._append(df2)
# print(y)


# Concat on Keys
frames = [df1, df2]
z1 = pd.concat(frames, keys=['x', 'y'])
# print(z1)



# Add new row
data1 = {
    'Name':['Rahul', 'Prince', 'Gaurav', 'Anuj'],
    'Age':[20, 21, 19, 18],
    'Address':['Delhi', 'Mumbai', 'Kolkata', 'Chennai'],
    'Qualification':['MSC', 'MA', 'MBA', 'MCA'],
    'Contact':['1234567890', '9876543210', '1111111111', '2222222222']
}

df = pd.DataFrame(data1)
s1 = pd.Series([10000,20000,30000,40000], name='Salary')
df = pd.concat([df, s1], axis=1)
print(df)
