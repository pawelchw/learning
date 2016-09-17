from __future__ import print_function

from scipy.special import comb, factorial

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.80, 0.95, 50)

data=[comb(100,i)*(x**i)*(1-x)**(100-i) for i  in xrange(95,100)]

y=np.zeros(len(x))

for row in xrange(5):
   for column in xrange(len(x)):
      y[column]=y[column]+data[row][column]

plt.plot(x,y)
plt.show()

#def n_r(n,r):

#   l_res = 1

#   for i in xrange(r):
#      l_res=l_res*( n - (r-i)+1 )
#   return l_res


#print(4.0/ comb( 52 ,5 , exact=True))

##       comb
## ---------------
##       52
##        5
##
#llprint( 4.0*factorial(5, exact=True)/ n_r(52,5))
##    4.0 * 5!
## ----------------
##  52*51*50*49*48
##    
##
