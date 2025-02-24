import matplotlib.pyplot as plt

left = [1,2,3,4,5]
height = [10,24,36,40,5]
tick_labels  = ['one', 'two', 'three', 'four', 'five']

plt.bar(left, height, tick_label=tick_labels, width=0.8, color=['g', 'b'])

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Bar Chart')
plt.show()