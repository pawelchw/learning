from __future__ import print_function
import statsmodels.api as sm
from sklearn.linear_model import LogisticRegression as sklr #import LogisticRegression as lr
import numpy as np
from validate import train_split as ts

def sm_reg(data, outcome, predictors, mode='ols', ps = 'n', train_ratio = 0):

  x_tr, x_te, l_tr, l_te = ts(data, outcome, predictors,  train_ratio )
  print( x_tr.shape)
  print( x_te.shape)
  if mode=='log':

    model = sm.Logit(l_tr, sm.add_constant(x_tr.as_matrix()))
    res= model.fit()
    if ps=='y':
       print(res.summary())

    ypred = res.predict(sm.add_constant(x_te.as_matrix()))
    return x_tr, x_te, l_tr, l_te,ypred, model

  elif mode =='ols':

    model = sm.OLS(df_tmp.ix[0:max_train,outcome], sm.add_constant(df_tmp.ix[0:max_train, predictors]) )
    res= model.fit()
    if ps=='y':
       print(res.summary())

    x = data.ix[max_train+1: len(data), outcome+predictors]#.as_matrix()
    y = model.predict(x)
    return x,y,model



def sk_reg(data, outcome, predictors, train_ratio, mode='log' ):

  x_tr, x_te, l_tr, l_te = ts(data, outcome, predictors,  train_ratio )
  model = sklr()
  model.fit(x_tr.as_matrix(), l_tr.as_matrix())

  ypred = model.predict( x_tr.as_matrix() )
  return x_tr, x_te, l_tr, l_te,ypred, model
