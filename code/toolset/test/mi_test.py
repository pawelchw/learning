import numpy as np
import matplotlib.pyplot as plt
import math as mt
from minepy import MINE

def corx(N, rho = 0.5):
  r = np.random.randn(N,2)
  r1 = r[:,0]
  r11 = r[:,1]
  r2 = rho*r1 + (1-rho**2)**0.5 * r11
  return r1,r2

def realm(x):

  y = [ -0.5* mt.log(1-i**2,2) for i in x]
  return y


mn = MINE(alpha=0.6, c=15)
x = np.linspace(0.01, 0.99,20)
y = realm(x)
N=2000
res=[]
for i in xrange(len(x)):
    r1,r2 = corx(N,x[i])
    mn.compute_score(r1,r2)
    res.append(mn.mic())
    print(i)
