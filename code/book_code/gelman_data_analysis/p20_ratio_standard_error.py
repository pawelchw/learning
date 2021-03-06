from __future__ import print_function
import numpy as np
import scipy as sp
import scipy.stats as st
import statsmodels.stats.proportion as prop

def se_error(mu,n):
  return np.sqrt( mu * ( 1-mu) /n )

n_m = 500
mu_m = 0.75
se_m = se_error( mu_m, n_m)

n_w = 500
mu_w = 0.65
se_w = se_error( mu_w, n_w)


n = 1000

p_m = np.random.normal( mu_m, se_m,n )
p_w = np.random.normal( mu_w, se_w,n )

r = p_m / p_w

print( st.mstats.mquantiles(r, [.025, .975]))
