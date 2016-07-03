import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(1,100,100)


def n_r(n,r):

   l_res = 1

   for i in xrange(r):
      l_res=l_res*( n - (r-i)+1 )
   return l_res


y=[ 1.0-(n_r(365.0,i))/365.0**i for i in xrange(len(x))]
