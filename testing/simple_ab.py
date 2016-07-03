from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
import pymc as pm

p_a = 0.05
p_b = 0.04
N_a = 1500
N_b = 7500

data_a = pm.rbernoulli(p_a,N_a)
data_b = pm.rbernoulli(p_b,N_b)


p_a = pm.Uniform("p_a",0,1)
obs_a = pm.Bernoulli("obs_a",p_a, value=data_a,observed=True)

p_b = pm.Uniform("p_b",0,1)
obs_b = pm.Bernoulli("obs_b",p_b, value=data_b,observed=True)

@pm.deterministic
def delta(p_a = p_a, p_b = p_b):
   return p_a - p_b

mcmc = pm.MCMC([p_a,obs_a,p_b,obs_b,delta])
mcmc.sample(50000,1000)

'''
print ( "mean:" + str(data.mean()) \
      + " true:" + str(p_t) \
      + " form data:" + str( mcmc.trace("p")[:].mean() )  
      )
'''
