import pandas as pd
import numpy as np

stud = pd.read_csv("D:\my desk\Coding\Training\student_record.csv")

# Count Total Null in each column
myNull = stud.isnull().sum()

# Count Total Null in each rows
myNull = stud[stud['roll no.'].isnull()]

#print(myNull)

# Add another row
stud.loc['24', : ] = 'Jatin', '54','54','20k','89','89%','passed'

# Update a nan value
stud['roll no.'].iloc[4]=15.0
# or
stud.name.iloc[19] = 'Vanshika Moti'


# Lets update nan automatically and logically
for i in ['marks', 'percentage']:
    total = sum(stud[i])
    avg = stud[i]/total
    #for j in range(len(stud.index)):
    for j in stud[stud['roll no.'].isnull()].index:
        if stud.loc[j, i] == np.nan:
            stud.loc[j, i] = avg

print(stud)
