import matplotlib.pyplot as plt

x = [1,2,3,4,5,6]
y = [2,3,1,5,2,6]

plt.plot(x,y, color='g', linestyle='dashed', linewidth=3, marker='o', markerfacecolor='b', markersize=12)

plt.xlim(1,8)
plt.ylim(1,8)

plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.title("My Third Graph")

plt.show()