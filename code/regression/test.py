from __future__ import print_function
import numpy as np
import pandas as pd
import csv
import string
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression as sklr #import LogisticRegression as lr


N = 1000
def prep_df()
  h_min_m = 160
  h_max_m = 210
  m = pd.DataFrame()
  m_u = 120000
  m_sd = 10000
  m['gender'] = [1 for i in xrange(N)]
  m['height'] = [np.random.randint(h_min_m, h_max_m) for i in xrange(N)]
  m['pay'] = [ m.ix[i, 'height'] * np.random.randint(m.ix[i,'height'], np.max(m.height)+1 ) for i in xrange(N)]

  h_min_f = 150
  h_max_f = 180
  f = pd.DataFrame()
  f_u = 50000
  f_sd = 10000
  f['gender'] = [0 for i in xrange(N)]
  f['height'] = [np.random.randint(h_min_f, h_max_f) for i in xrange(N)]
  f['pay'] = [ f.ix[i, 'height'] * np.random.randint(f.ix[i,'height'], np.max(f.height)+1 ) for i in xrange(N)]

  h_min_c = 90
  h_max_c = 140
  c = pd.DataFrame()
  c_u = 30000
  c_sd = 5000
  c['gender'] = [-1 for i in xrange(N)]
  c['height'] = [np.random.randint(h_min_c, h_max_c) for i in xrange(N)]
  c['pay'] = [ c.ix[i, 'height'] * np.random.randint(c.ix[i,'height'], np.max(c.height)+1 ) for i in xrange(N)]

  df_tmp = pd.merge( m,f, on=['gender','pay','height'], how='outer')
  df = pd.merge( df_tmp,c, on=['gender','pay','height'], how='outer')
  #df = df_tmp
  df['pay_l'] = np.log(df['pay'])

  # pick the predictors and outcome variables
p=['pay_l'] # 'height',
o=['gender']


x = df[p].as_matrix()
y = df[o].as_matrix() #values.ravel()
# logit = sk fit( x.as_matrix(),y)
model = sklr()
#Xtrain = x.as_matrix()
model.fit(x,y.ravel())
xpred =df[p].as_matrix()
ypred = model.predict( xpred )

