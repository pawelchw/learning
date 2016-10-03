import numpy as np
from theano import function as fn
from theano import In
import theano.tensor as T
import matplotlib.pyplot as plt

a,b = T.dmatrices('a','b')

diff = a-b
abs_diff = abs(diff)
diff_sr =  diff ** 2

f = fn( [a,b], [diff, abs_diff, diff_sr])

n = [ [11,22], [22,11] ]
m = [ [1,2], [3,4] ]

print( f(m,n) )

x,y,z = f(n,m)

# we coul try out a default value.
f2 = fn( [a, In(b, value = [ [0,0], [0,0] ]) ], diff_sr)
