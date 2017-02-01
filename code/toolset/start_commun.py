from __future__ import print_function
from model import validate  as va
from model import correlation_analysis as ca
from model import feature_importance as fi
from plot import scat_mat_cor as smc
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
import math
import numpy as np
exec(open('./reqs/comm_col_names.py').read())
df = pd.read_csv('/home/pch/learning/datasets/regression/Communities_and_Crime_Unnormalized/data.csv')
df.columns = col_names

df_cpy = df

names=[]
for xx in df.columns:#   ['communityname']:#   ['arsons']     ['fold']

    ## gather first few values to discover if those are mainly numbers
    first_strings = df.ix[:,xx][:100]
    ##convert to is a number or not
    ##using to_numeric to convert non nums into nans
    num_test = [math.isnan(i) for i in pd.to_numeric(first_strings, errors='coerce')]
    #by mainly we mean at least 80 prct of values are nums
    string_limit = 0.9
    if sum( num_test )*1.0 / len(first_strings) <= string_limit:
      names = names + [xx]

      #get a column we are looking at
      l_col = df.ix[:,xx].astype(str)
      #extract nums
      #pdb.set_trace()      
      l_col_nums = [ ii for ii in  l_col if ii!= '?' ] #l_col[ l_col <> '?' ]

      l_avg = np.mean( pd.to_numeric(l_col_nums) )

      l_col[ l_col == '?'] = l_avg
  
      df.ix[:,xx]= l_col

for xx in names:

   df.ix[:,xx] = pd.to_numeric(df.ix[:,xx])

samples = df.ix[:,names].sample(replace=False, frac=0.2)
samples = samples.reset_index()
#samples = samples.drop('index',axis=1)
samples = samples.ix[:,1:]

names_not_pred = list(set(names) - set(col_names_pred))

o = ['murders']
x_train, x_test, l_train, l_test = va.train_split(df, o, names_not_pred, ratio = 0.3 )


cmat = smc.net_plot(x_train)
col_mat, cols = ca.corr_greater_than( cmat, 0.9 )
x_train_clean = x_train.drop( cols.index, axis=1 )
x_train_clean = va.data_std(x_train_clean, cols=[], std = 0)

x_train_std = pd.DataFrame([ (a,b) for a,b in zip( x_train_clean.columns, np.std(x_train)) ])
x_train_avg = pd.DataFrame([ (a,b) for a,b in zip( x_train_clean.columns, np.mean(x_train)) ])
x_test_clean = x_test.drop( cols.index, axis=1 )
x_test_clean = va.train_data_std(x_test_clean, x_train_std, x_train_avg)

X = x_train_clean.as_matrix()
Y = l_train.as_matrix()
rf=RandomForestRegressor()
a = rf.fit(X,Y)
#print(a)
im_sc = pd.DataFrame( sorted( zip(map(lambda x: round(x,4),rf.feature_importances_), names), reverse=True), columns=['score','cname'])
im_sc_loop = fi.feature_importance_loop( x_train_clean, l_train)

'''
n_l = 5
n_short = names[:5]
samples = df.ix[:,n_short].sample(replace=False, frac=0.2)
samples = samples.reset_index()
#samples = samples.drop('index',axis=1)
ss = samples.ix[:,1:]

for xx in ss.columns:

   ss.ix[:,xx] = pd.to_numeric(ss.ix[:,xx])


x_pd = pd.DataFrame(df.ix[:,4:30])
x_pd['target'] = pd.DataFrame(df['murders'])
x = x_pd.ix[:,:-1]
y = x_pd['target']
xi = c_inter.fit_transform(x)
main_effects = c_inter.n_input_features_
variables = x.columns
def r2_est(x,y):
   return r2_score(y, lin_reg.fit(x,y).predict(x))

x_tr, x_te, y_tr, y_te = train_test_split(x,y.astype(float), test_size = 0.33, random_state=432)

y_res=lin_reg.fit(x_tr,y_tr).predict(x_te).astype(int)

base = r2_est(x_tr, y_tr)

for k, effect in enumerate(c_inter.powers_[(main_effects):]):
    terma, termb = variables[effect==1]
    incr = r2_est(xi[:, list(range(0,main_effects))+[main_effects+k]],y) - base
    if incr > 0.01:
        print('adding interactions:', terma,' ', termb,' ',incr)

'''
