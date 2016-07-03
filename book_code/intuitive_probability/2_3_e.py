from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from math import pi

N = 100000

x = np.random.uniform(0,1,N)

# x^n = 1/(n+1) * x^(n+1) = 1/3

print( sum( x**2 )/ N )

x = np.random.uniform(-1,1,N)

print( sum( (1.0/np.sqrt(2*pi)) * np.exp(-0.5 * x**2) )/N )





