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

print("\n\nnew values every time")
for i in xrange(2):
   print(f())
print("\n\nsame numbers as thers no updates")
for i in xrange(2):
   print(g())

print("\n\nrandom seed swap test")
print(f())
a = rv_u.rng.get_value(borrow=True)
a.seed(504)
rv_u.rng.set_value(a, borrow = True)
print(f())
