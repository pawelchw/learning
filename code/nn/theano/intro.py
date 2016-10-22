import numpy as np
from theano import function as fn
import theano
from theano.tensor.shared_randomstreams import RandomStreams
import theano.tensor as T
import matplotlib.pyplot as plt


# create two matrix objects in theano
a,b = T.dmatrices('a','b')

#create a function that perfroms multiple operations
# 1 add
op_add = a + b
# 2 subtract
op_sub = a-b
# 3 picewise multiply
op_mul = a*b

fn_maths = fn( [a,b], [op_add, op_sub, op_mul])

#test

print ( fn_maths([ [1,2], [3,4] ],  [ [1,1], [2,2] ]) )


# theano uses scan for looping
# defining the tensor variables
# there is an example on the website to calculate
# tanh( x(t).dot(W) + b )
X = T.matrix("X")
W = T.matrix("W")
b_sym = T.vector("b_sym")


# lambda call means input v and return v*W + b_sym
results, updates = scan(lambda v: T.tanh(T.dot(v, W) + b_sym), sequences=X)
res = fn( inputs = [X, W, b_sym], outputs = results)

x = np.eye(2, dtype=theano.config.floatX)
w = np.ones((2, 2), dtype=theano.config.floatX)
b = np.ones((2), dtype=theano.config.floatX)
b[1] = 2

print(res(x, w, b))
