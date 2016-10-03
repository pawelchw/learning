from __future__ import print_function
import theano
import numpy
import theano.tensor as T
from theano import function as fn
import matplotlib.pyplot as plt

rng = numpy.random
#no of rows
N = 100
#no of features
feats = 10

# generate a dataset: D = (input_values, target_class)
# therefore
# D will have a matrix of N rows and t columns
# t is the number of features
# target class is a random in between low and high -1

D = (rng.randn(N, feats), rng.randint(size=N, low=0, high=2))
training_steps = 10000


x = T.dmatrix("x")
y = T.dvector("y")


# create two shared variables that will have
# common updates between iterations

# weight vector w
w = theano.shared(rng.randn(feats), name="w")

# bias term
b = theano.shared(0., name="b")



p_1 = 1 / (1 + T.exp(-T.dot(x, w) - b))            # Probability that target = 1
prediction = p_1 > 0.5                             # The prediction threshold
xent = -y * T.log(p_1) - (1-y) * T.log(1-p_1)      # Cross-entropy loss function
cost = xent.mean() + 0.01 * (w ** 2).sum()         # The cost to minimize
gw, gb = T.grad(cost, [w, b]) 

# Compile
train = theano.function(
          inputs=[x,y],
          outputs=[prediction, xent],
          updates=((w, w - 0.1 * gw), (b, b - 0.1 * gb)))
predict = theano.function(inputs=[x], outputs=prediction)

for i in range(training_steps):
    pred, err = train(D[0], D[1])

print("Final model:")
print(w.get_value())
print(b.get_value())
print("target values for D:")
print(D[1])
print("prediction on D:")
print(predict(D[0]))
