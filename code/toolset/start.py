#import pandas as pd
from etl import fileread as f
from model import regression as r
df = f.space_read("/home/pch/learning/datasets/regression/gelman_reg/arsenic/wells.dat")
df['dist100'] = df['dist'] / 100

o = ['switch']
p = ['dist100','arsenic']

tr = 2000
xm,ym,mm = r.sm_reg(df, o, p,'log','n', tr)
xs,yx,mx = r.sk_reg(df, o, p,'log',tr)
#sk_reg(data, outcome, predictors, mode='log',max_train = 0 ):
