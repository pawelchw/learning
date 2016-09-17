###
'''
This code shows that standarization does not improve the fit - the r squared values are the same for both models.
Interestingly, the interaction intercept and its standard error remain the same too.
'''
###
from __future__ import print_function
import numpy as np
import pandas as pd
import csv
import string
import statsmodels.api as sm
import matplotlib.pyplot as plt

df = pd.io.stata.read_stata("/home/pawel-dell/learning/datasets/regression/gelman_reg/child.iq/kidiq.dta")
#print(df.head())

def run_reg(data, outcome, predictors, mode='ols', ps = 'n'):

  ttt = data.ix[:, outcome+predictors]

  if mode=='logit':

    logit = sm.Logit(tt.ix[:,outcome], sm.add_constant(ttt.ix[:, predictors]) )
    res= logit.fit()
    if ps=='y':
       print(res.summary())

  elif mode =='ols':

    ols = sm.OLS(ttt.ix[:,outcome], sm.add_constant(ttt.ix[:, predictors]) )
    res= ols.fit()
    if ps=='y':
       print(res.summary())

  return ttt, res


#plot_double_res(df,o,p,b,m)
#interactions
df['mom_hs_iq']= df['mom_iq']*df['mom_hs']
p=['mom_iq']
b=['mom_hs']
i=['mom_hs_iq']
o=['kid_score']
tt, m =run_reg(df,o,p+b+i,'ols','y')


df['mean_hs'] = df['mom_hs'] - np.mean(df['mom_hs'])
df['mean_iq'] = df['mom_iq'] - np.mean(df['mom_iq'])
df['mean_ih'] = df['mean_hs']*df['mean_iq']
p=['mean_iq']
b=['mean_hs']
i=['mean_ih']
o=['kid_score']
tt, m =run_reg(df,o,p+b+i,'ols','y')


df['norm_hs'] = (df['mom_hs'] - np.mean(df['mom_hs'])) / ( 2.0* np.std(df['mom_hs']) )
df['norm_iq'] = (df['mom_iq'] - np.mean(df['mom_iq'])) / ( 2.0* np.std(df['mom_iq']) )
df['norm_ih'] = df['mean_hs']*df['mean_iq']
p=['norm_iq']
b=['norm_hs']
i=['norm_ih']
o=['kid_score']
tt, m =run_reg(df,o,p+b+i,'ols','y')
