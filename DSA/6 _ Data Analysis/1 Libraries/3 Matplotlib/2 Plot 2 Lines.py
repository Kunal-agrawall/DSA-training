# Plot 2 lines on same graph

import matplotlib.pyplot as plt

x1, y1  = [1,2,3], [1,2,3]
x2, y2 = [1,2,3], [1,3,2]

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.plot(x1,y1, label='Line-1')
plt.plot(x2,y2, label='Line-2')
plt.title("My Second Graph")
plt.show()