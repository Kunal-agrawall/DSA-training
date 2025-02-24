import matplotlib.pyplot as plt

x = [0,1,2,3,4,5,6,7,8]
y = [i*10 for i in x]

plt.scatter(x,y)
plt.show()