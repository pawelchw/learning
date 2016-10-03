import numpy as np
from theano import function as fn
from theano import In
from theano import shared
import theano.tensor as T
import matplotlib.pyplot as plt

st = shared(0)
inc = T.iscalar('inc')

acc = fn( [inc], st, updates = [ (st, st+inc)] )

print(st.get_value())
acc(400)
print(st.get_value())
st.set_value(10)
print(st.get_value())

dcc = fn( [inc],  st, updates = [ (st, st-inc)] ) 

res = st * 2 + inc
#something that matches shared var type
v = T.scalar( dtype = st.dtype)

# so v is of state (st) type
# givens gets you state := v but dont modify the value of
# st
skip = fn( [inc,v], res, givens = [(st,v)])
