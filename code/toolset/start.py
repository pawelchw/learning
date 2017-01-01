#import pandas as pd
import numpy as np
from etl import fileread as f
from model import regression as r
from model import support_machines as s
#df = f.space_read("/home/pch/learning/datasets/regression/gelman_reg/arsenic/wells.dat")
df['dist100'] = df['dist'] / 100

o = ['switch']
p = ['dist100','arsenic']

x = ['dist100']
df['dist_m'] = ( df[x] - np.mean(df[x]) ) / np.std(df[x])

x = ['arsenic']
df['arsenic_m'] = ( df[x] - np.mean(df[x])) / np.std(df[x])


p = ['dist_m','arsenic_m']

tr = 0.25
x_tr, x_te, l_tr, l_te,ypred, model = r.sm_reg(df, o, p,'log','n', tr)
#sx_tr, sx_te, sl_tr, sl_te,sypred, smodel= r.sk_reg(df, o, p,tr,'log')
sx_tr, sx_te, sl_tr, sl_te,sypred, smodel= s.sk_svm(df, o, p,tr)
#sk_reg(data, outcome, predictors, mode='log',max_train = 0 ):

res=l_te
res['log'] = [int(i) for i in ypred>= 0.5]
res['svm'] = sypred

print( res.groupby( ['switch','log'] ).size() )
print( res.groupby( ['switch','svm'] ).size() )
