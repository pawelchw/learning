import numpy as np
from theano import function as fn
import theano.tensor as T
import matplotlib.pyplot as plt

#create a vector and call it x
x = T.vector('x')
#build a return variable
s = (1.0*1) / ( 1.0 + np.exp(-x) )
#create a function based on association
f = fn( [x], s)

#x line for the function
l_start = -20.0
l_end = 20
l_n = 1000
d = np.linspace(l_start, l_end,l_n)


#plot
plt.plot(d,f(d))
plt.grid()
plt.show()


# we can show that
#
#   1           1+ tanh(x/2)
# ----------- = -----------
#  1+ e(-x)         2
#

s2 = (1.0 + np.tanh(x/2.0) ) / 2
f2 = fn( [x], s2)


#show that both functions return the same values.
print(np.allclose( f(d), f2(d) ) )
