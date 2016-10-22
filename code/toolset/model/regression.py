from __future__ import print_function
import statsmodels.api as sm
from sklearn.linear_model import LogisticRegression as sklr #import LogisticRegression as lr
import numpy as np
from validate import train_split as ts

def sm_reg(data, outcome, predictors, mode='ols', ps = 'n', max_train = 0):

  df_tmp = data.ix[0:max_train, outcome+predictors]
  if mode=='log':

    model = sm.Logit(df_tmp.ix[:, outcome], sm.add_constant(df_tmp.ix[:, predictors]) )
    res= model.fit()
    if ps=='y':
       print(res.summary())

    x = data.ix[max_train+1: len(data), predictors]
    y = res.predict(sm.add_constant(x))
    return x,y,model

  elif mode =='ols':

    model = sm.OLS(df_tmp.ix[0:max_train,outcome], sm.add_constant(df_tmp.ix[0:max_train, predictors]) )
    res= model.fit()
    if ps=='y':
       print(res.summary())

    x = data.ix[max_train+1: len(data), outcome+predictors]#.as_matrix()
    y = model.predict(x)
    return x,y,model



def sk_reg(data, outcome, predictors, train_ratio, mode='log' ):

  #df_tmp = data.ix[0:max_train, outcome+predictors]
  # x = df_tmp.ix[0:max_train, predictors].as_matrix()
  #y = df_tmp.ix[0:max_train, outcome].as_matrix() #values.ravel()
  # logit = sk fit( x.as_matrix(),y)
  #Xtrain = x.as_matrix()

  x_tr, x_te, l_tr, l_te = ts(data, outcome, predictors,  train_ratio )
  model = sklr()
  model.fit(x_tr, l_tr)

  ypred = model.predict( x_tr )
  return x_tr, x_te, l_tr, l_te,ypred, model
