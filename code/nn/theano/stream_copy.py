from __future__ import print_function
import theano
import numpy
import theano.tensor as T
from theano import function as fn
from theano.sandbox.rng_mrg import MRG_RandomStreams
from theano.tensor.shared_randomstreams import RandomStreams

#class to be used in initialization of an object
class Graph():
  def __init__(self, seed=504):
     self.rng = RandomStreams(seed)
     self.y = self.rng.uniform(size=(1,))


def copy_random_state(g1, g2):
    if isinstance(g1.rng, MRG_RandomStreams):
       g2.rng.rstate = g1.rng.rstate
    for (su1, su2) in zip(g1.rng.state_updates, g2.rng.state_updates):
       su2[0].set_value(su1[0].get_value())


g1 = Graph(seed=123)
f1 = fn([], g1.y)
f2 = fn([], g1.y)
print("\n\nFunctions taking on the same initialization graph are ouf of sync")
print([ zip(f1(),f2()) for i in xrange(3)])

print("\n\nSame with two other graphs")
g2 = Graph()
f2 = fn([], g2.y)

print("\n\nHowever, we could share the random state")
copy_random_state(g1, g2)
print([ zip(f1(),f2()) for i in xrange(3)])
