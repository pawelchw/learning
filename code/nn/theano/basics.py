import theano.tensor as T
from theano import function as f
from theano import In
import numpy as np

x = T.dscalar('x')
y = T.dscalar('y')

z = x + y

fn = f([x,y], z)

#Returns True if two arrays are element-wise equal within a tolerance.

print(np.allclose(fn(33.0003, 33.0003), 66.0006))

print ( 'This will not work now: print(fn([1,2], [3,4]))')
print('\n because those are scalars, not matrices')

x = T.dmatrix('x')
y = T.dmatrix('y')

z = x+y
fn = f([x, y], z)


# default values

x,y = T.dscalars('x','y')
z = x + y

fn = f( [x, In(y,value=0)],z)
