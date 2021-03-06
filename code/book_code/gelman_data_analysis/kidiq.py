from __future__ import print_function
import numpy as np
import pandas as pd
import csv
import string
import statsmodels.api as sm
import matplotlib.pyplot as plt

df = pd.io.stata.read_stata("/home/pawel-dell/learning/datasets/regression/gelman_reg/child.iq/kidiq.dta")
#print(df.head())



def run_reg(data, outcome, predictors, mode='ols'):

  ttt = data.ix[:, outcome+predictors]
  '''
  for i in xrange( len(ttt)-1,-1,-1 ):
     if ( ttt.ix[i,'int'] ==0 and np.sum(ttt.ix[i, t_cols]) == 0 ) or ( ttt.ix[i,'int'] ==1 and np.sum(ttt.ix[i, t_cols]) == 1 ):
        ttt = ttt.drop(i)
  ttt = ttt.reset_index()
  ttt=ttt.drop('index', axis=1)
  '''

  if mode=='logit':

    logit = sm.Logit(tt.ix[:,outcome], sm.add_constant(ttt.ix[:, predictors]) )
    res= logit.fit()
    print(res.summary())

  elif mode =='ols':

    ols = sm.OLS(ttt.ix[:,outcome], sm.add_constant(ttt.ix[:, predictors]) )
    res= ols.fit()
    print(res.summary())
  return ttt


tt=run_reg(df,o,p,'ols')

print('\n The intercept. If a child had a mother with an IQ of 0 and who did not complete high school (thus, mom in hs = 0)');
print(', then we would predict this childs test score to be 26. This is not a useful prediction, since no mothers have IQs of 0.');

print('\n\n The coefficient of maternal high school completion. Comparing children whose mothers have the same IQ, but who differed in whether they completed high ');
print('school, the model predicts an expected difference of 6 in their test scores');


print('\n\n The coefficient of maternal IQ. Comparing children with the same value of mom_hs, but whose mothers differ by 1 point in IQ, we would expect to see ');
print(' a difference of 0.6 points in the childs test score (equivalently, a difference of 10 in mothers IQs corresponds to a difference of 6 points for their children).');
