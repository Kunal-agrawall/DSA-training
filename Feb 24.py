import pandas as pd
import numpy as np

stud = pd.read_csv("D:\my desk\Coding\Training\student_record.csv")

# Count Total Null in each column
myNull = stud.isnull().sum()

# Count Total Null in each rows
myNull = stud[stud['roll no.'].isnull()]

#print(myNull)

# Add another row
# stud.loc['24', : ] = 'Jatin', '54','54','20k','89','89%','passed'

# Update a nan value
stud['roll no.'].iloc[4]=15
stud["roll no."].iloc[13]=25
stud["roll no."].iloc[19]=29
stud["roll no."].iloc[18]=28
# or
stud.name.iloc[19] = 'Vanshika Moti'


stud.exam_id=stud.exam_id.fillna(1)
stud.fees=stud.fees.fillna("14k")
stud.marks=stud.marks.fillna(34.0)
stud.percentage=stud.percentage.fillna('90%')
stud.result=stud.result.fillna("passed")

# Lets update nan automatically and logically
# for i in ['marks', 'percentage']:
#     total = sum(stud[i])
#     avg = stud[i]/total
#     #for j in range(len(stud.index)):
#     for j in stud[stud['roll no.'].isnull()].index:
#         if stud.loc[j, i] == np.nan:
#             stud.loc[j, i] = avg

print(stud)
print(stud.isnull().sum())


import matplotlib.pyplot as plt

plt.bar(stud.name, stud.marks)
plt.xticks(rotation=90)  # Rotate names 90 degrees for better visibility
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.title("Student Marks Bar Chart")
plt.show()

print(type(stud.name))
print(type(stud.marks))
