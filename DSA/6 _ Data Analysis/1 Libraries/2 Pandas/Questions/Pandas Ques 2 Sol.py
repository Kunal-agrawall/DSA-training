import pandas as pd
import numpy as np

exam_data = {
            'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
            'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
            'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
            'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
            }

# Q1                        
length = len(exam_data['name'])
df = pd.DataFrame(exam_data, index=[chr(97+i) for i in range(length)])

filtered_df = df[(df['score'] >= 15) & (df['score'] <= 20)]
#print(filtered_df)


# Q2
df.loc['d', 'score'] = 11.5
print(df)

# Q3
print("Sum  : ", sum(df['attempts']))

# Q4
print("Mean : ", np.mean(df['score']))

# Q5
s1 = {"name" : "Suresh", "score": 15.5, "attempts": 1, "qualify": "yes"}
s1 = pd.DataFrame(s1, index=[chr(97+length)])
length += 1
df = pd.concat([df, s1])
#print(df)

# Q6
df = df.drop(['j'], axis='rows')
print()
#print(df)