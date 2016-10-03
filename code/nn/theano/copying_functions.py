import numpy as np
from theano import function as fn
from theano import In
from theano import shared
import theano.tensor as T
import matplotlib.pyplot as plt

state = shared(0)
inc = T.iscalar('inc')
acc = fn( [inc], state , updates = [(state, state+inc)]
        , on_unused_input = 'ignore')

#overwrite the state variable with new state and copy
new_state = shared(-1)
new_acc = acc.copy( swap = {state:new_state} )
new_acc(100)
print(new_state.get_value())
print(state.get_value())

#we could delete updates mechanism like this

null_acc = acc.copy(delete_updates = True)

null_acc(123)
print(state.get_value())
