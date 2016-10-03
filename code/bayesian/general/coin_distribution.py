import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# we are trying to infere p(H)
# lets guess values

prior = [ 0.25, 0.5, 0.75]
guess = [ 0.25, 0.5, 0.25]


def lh( p_h, h, t):
   return ( (1.0 - p_h) **t )*(  p_h**h     )

def post( prior, guess, h, t, x ):

    return  [  guess[j] * lh(prior[j], h, t) 
               / 
               np.sum(
                             [ i[0]*i[1] for i in zip( prior, [lh(prior[i], 3, 9) for i in xrange(x) ])]
               )
    #         ]
             for j in xrange(x)]
'''
            / 
            np.sum([i[0]*i[1] for i in zip(prior,lh(prior, h, t))])  
            for i in xrange(3)  ]
   
'''
