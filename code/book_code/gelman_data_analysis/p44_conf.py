from __future__ import print_function
import numpy as np
import scipy as sp
import scipy.stats as st
import statsmodels.stats.proportion as prop

def conf(data, c=0.95):
   t = 1.0*np.array(data)
   n = len(t)
   m,se = np.mean(t), st.sem(t)
   h = se * st.t._ppf( (1+c) / 2., n-1 )
   return m, m-h, m+h

def get_proportion( y=700, n=300):
   return [ 1 for i in xrange(y)] + [0 for i in xrange(n)]

def conf_prop(y=700,n=300, c=0.95):
   data = get_proportion( y, n)
   y_p = (1.0* np.sum([ 1 for i in data if i == 1])) / len(data)
   n_p = (1.0* np.sum([ 1 for i in data if i == 0])) / len(data)

   print('Proportion confidence interval: ',prop.proportion_confint( np.sum([ 1 for i in data if i == 1]), len(data), .5, 'normal'))

d = [35,34,38,35,37]

print('Confidence interval: ',conf(d))
print(conf_prop())

   
