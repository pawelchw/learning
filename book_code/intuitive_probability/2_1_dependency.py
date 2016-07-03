import numpy as np
import matplotlib.pyplot as plt

N = 1000

x = np.random.uniform(0,1,N)
y = np.random.uniform(0,1,N)

plt.scatter(x,y)

plt.show()

plt.scatter(x, 0.5*x + 0.5*y)

plt.show()
