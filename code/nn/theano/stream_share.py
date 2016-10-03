import numpy as np
from theano import function as fn
from theano import In
from theano import shared
from theano.tensor.shared_randomstreams import RandomStreams
import theano.tensor as T
import matplotlib.pyplot as plt

srng = RandomStreams(seed=504)
# create random 2x2 matrices for 
#uniform and normal distributions respectively
rv_u = srng.uniform((2,2))
rv_n = srng.normal((2,2))

f = fn([],rv_u)
g = fn([], rv_n, no_default_updates = True)
nearly_zeros = fn([], rv_u + rv_u - 2*rv_u)

st_nz = rv_u.rng.get_value().get_state()

#print(nearly_zeros())
print(f())
v1 = f()
rng = rv_u.rng.get_value(borrow=True)
rng.set_state(st_nz)
rv_u.rng.set_value(rng, borrow = True)
v2 = f()
v3 = f()
print( v1)
print( v2)
print( v3)
