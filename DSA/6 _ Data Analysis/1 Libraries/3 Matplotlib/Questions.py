# WAP to plot graph of students record (5 records) using bar chart.
# Labels : Name, Marks

import matplotlib.pyplot as plt

name = [1,2,3,4,5]
marks = [10,24,36,40,5]
tick_labels  = ['Jatin', 'Shalu', 'Vanshika', 'Kunal', 'Rohan']

plt.bar(name, marks, tick_label=tick_labels, width=0.8, color=['g', 'b'])

plt.xlabel('Names')
plt.ylabel('Marks')
plt.title('Students Marks')
plt.show()