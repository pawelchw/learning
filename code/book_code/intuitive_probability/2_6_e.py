from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from math import pi

N = 10000

U1 = np.random.uniform(0,1,N)
U2 = np.random.uniform(0,1,N)

x = U1*U2
B=100
plt.hist(x,bins=B)
