import numpy  as np
import theano as th
a = th.tensor.vector('a')
out = a + a ** 10

fn = th.function([a], out)

print( fn([0,1,2]))

b = th.tensor.vector('b')

out = a ** 2 + b ** 2 + 2*a*b

fn = th.function([a,b], out)
