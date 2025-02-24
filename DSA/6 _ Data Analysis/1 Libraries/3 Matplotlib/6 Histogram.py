import matplotlib.pyplot as plt
import random
import numpy as np

# __________________________________________________________________________
# n = 10 # No. of random numbers
# arr = random.sample(range(1,101), n)

# plt.hist(arr, rwidth=0.8)
# plt.show()

# __________________________________________________________________________
# ages = [2,5,4,7,9,2,10,20,25,14,1,16,18,19,10,19,17,22,25,24,26,28,27,29]

# my_range = (0,100) # Set range
# bins = 10          # Set no. of Intervels

# plt.hist(ages, bins, my_range, color='g', histtype='bar', rwidth=0.8)
# plt.show()


# __________________________________________________________________________
students = np.random.randint(1,101,50)

bins = 10
plt.hist(students, bins, color='skyblue', histtype='bar', rwidth=0.8)

plt.xlabel('Marks')
plt.ylabel('Frequency')

plt.show()
