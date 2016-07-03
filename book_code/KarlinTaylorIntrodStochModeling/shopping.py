import pymc as pm
import matplotlib.pyplot as plt
from pymc.Matplot import plot

#customers buy with probability of 0.3

b_alpha = 30
b_beta = 70

# mean = 0.3

shopping = pm.Beta("shopping", alpha = b_alpha, beta = b_beta)
arrivals = pm.Poisson("arrivals",mu=10)

orders = pm.Bernoulli("orders", p=shopping, size=arrivals)

model = pm.MCMC([shopping,arrivals,orders])
M=model.sample(10000,5000)
