import pandas as pd

data1 = {
    'key':['k0', 'k1', 'k2', 'k3'],
    'Name':['Rahul', 'Prince', 'Gaurav', 'Anuj'],
    'Age':[20, 21, 19, 18]
}

data2 = {
    'key':['k0', 'k1', 'k2', 'k3'],
    'address':['abc', 'def', 'ghi', 'jkl'],
    'phone':['123', '456', '789', '012']
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

m = pd.merge(df1, df2, on='key')
print(m)