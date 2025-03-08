# Seaborn 

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use('classic')
# %matplotlib inline
rng=np.random.RandomState(0)
x=np.linspace(0,10,250)
y=np.cumsum(rng.randn(250,6),0)
plt.plot(x,y)
plt.legend('ABCD',ncol=2,loc='best')
plt.show()