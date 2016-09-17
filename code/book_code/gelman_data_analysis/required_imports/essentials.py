from __future__ import print_function
import numpy as np
import pandas as pd
import csv
import string
import statsmodels.api as sm
import matplotlib.pyplot as plt
import pymc3 as pm
import seaborn as sns

def run_reg(data, outcome, predictors, mode='ols', ps = 'n'):

  ttt = data.ix[:, outcome+predictors]

  if mode=='logit':

    logit = sm.Logit(ttt.ix[:,outcome], sm.add_constant(ttt.ix[:, predictors]) )
    res= logit.fit()
    if ps=='y':
       print(res.summary())

  elif mode =='ols':

    ols = sm.OLS(ttt.ix[:,outcome], sm.add_constant(ttt.ix[:, predictors]) )
    res= ols.fit()
    if ps=='y':
       print(res.summary())

  return ttt, res

