###
'''
This code shows that correlated data generate zero slope intercept.
'''
###
from __future__ import print_function
import numpy as np
import pandas as pd
import csv
import string
import statsmodels.api as sm
import matplotlib.pyplot as plt

n=500
x = np.random.normal(0,1,n)
y = 0.5*x + np.random.normal(1,1,n)
d = pd.DataFrame()
d['y'] = ( y - np.mean(y) ) / 2.0 * np.std(y)
d['x'] = ( x - np.mean(x) ) / 2.0 * np.std(x)
l = sm.OLS(d.ix[:,'y'], sm.add_constant(d.ix[:,'x']) )
r = l.fit()
print(r.summary())

