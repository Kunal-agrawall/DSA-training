import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

student=pd.read_csv("D:\my desk\Coding\Training\student_record.csv")
print(student)

print(list(student.columns))

print(student.isnull().sum())

print(student[student["name"].isnull()])


student["name"].iloc[19]="kuldeep"
# print(student)

print(student.isnull().sum())


# print(student[student["roll no."].isnull()])
# student["roll no."].iloc[4]=23
# student["roll no."].iloc[13]=25
# student["roll no."].iloc[18]=28
# student["roll no."].iloc[19]=29
# print(student)

print(student[student["exam_id"].isnull()])

# student.iloc[student["roll no."].isnull()]=[23,25,47,56]
# print(student)

student.exam_id=student.exam_id.fillna(1)
student.fees=student.fees.fillna("14k")
student.marks=student.marks.fillna(34)
student.percentage=student.percentage.fillna(90)
student.result=student.result.fillna("passed")
# print(student)
# student=student.drop(index=19)


print(student)
print(student.isnull().sum())

import matplotlib.pyplot as plt

plt.bar(student.name, student.marks)
plt.xticks(rotation=90)  # Rotate names 90 degrees for better visibility
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.title("Student Marks Bar Chart")
plt.show()

print(type(student.name))
print(type(student.marks))








