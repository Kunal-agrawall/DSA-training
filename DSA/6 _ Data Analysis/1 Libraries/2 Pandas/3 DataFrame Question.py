import pandas as pd

'''
Q1. WAP to create students record table which contain column names:
    Roll No, Name, Age, Class, Address, Phone No, Email, Stream

    Create DataFrame and pass all student record in DataFrame.
    Number of values takes 10 lines(entries) of each columns.
'''

dict = {
    'Roll No': [1, 2, 3, 4],
    'Name': ['Rahul', 'Rohan', 'Rahul', 'Ram'],
    'Age': [20, 21, 19, 18],
    'Class': ['X', 'X', 'X', 'X'],
    'Address': ['Delhi', 'Mumbai', 'Kolkata', 'Chennai'],
    'Phone No': ['1234567890', '9876543210', '111111', '23435556'],
    'Email': ['rahul@gmail.com', 'rohan@gmail.com', 'rahul@gmail.com', 'anede113@gmail.com'],
    'Stream': ['Science', 'Arts', 'Commerce', 'Science']
}

df = pd.DataFrame(dict)


'''
Q2. WAP to create and display a DataFrame from specified Dictionary data which has the
    index labels like a,b,c,d....
'''

df.index = [chr(97+i) for i in range(len(df.index))]


'''
Q3. Print first 3 rows.
'''

d = df.head(3)


'''
Q4. Print Name, Age.
'''

d = df[['Name', 'Age']]


'''
Q5. Select rows with age >= 20
'''

d = df[df.Age>=20]
print(d)