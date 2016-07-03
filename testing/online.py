from __future__ import division
import pymc as mc
import matplotlib.pyplot as plt

# create test data
N = 50
mu = 5
data = randn(N) + mu

# start PyMC variables
mu_0 = mc.Uniform('$\mu_0$', 0, 10)
sigma_0 = mc.Uniform('$\sigma_0$', 0, 2)

data = mc.Normal('data', mu_0, sigma_0**-2, observed=True, value=data)

# sample
mcmc = mc.MCMC([data, mu_0, sigma_0]) 
mcmc.sample(iter=50000, burn=5000)

# plot
figure()
