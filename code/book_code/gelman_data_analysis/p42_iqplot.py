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

def plot_res(data, outcome, predictor, model):

   x = np.linspace(int(np.min(data.ix[:,predictor])-3), int(np.max(data.ix[:,predictor])+3), 1000)
   plt.scatter(data.ix[:,predictor],data.ix[:,outcome])
   plt.plot(x, model.params[0] + x*model.params[1])
   plt.xlabel(p)
   plt.ylabel(o)
   plt.show()

def diff_c(hs):

   res = 'b'
   if hs == 1 or hs=='mom_hs':
      res='r'
   return res

def plot_double_res(data, outcome, predictor,bin_var, model):

   for i in xrange( len(data) ):
      plt.scatter(data.ix[i,predictor],data.ix[i,outcome],color = diff_c(data.ix[i,'mom_hs']))

   x = np.linspace(int(np.min(data.ix[:,predictor])-3), int(np.max(data.ix[:,predictor])+3), 1000)
   params=pd.DataFrame([ [k,v] for k,v in m.params.iteritems()])
   plt.plot(x, params.ix[0,1] + params.ix[1,1]*x + params.ix[2,1], color = diff_c(params.ix[1,0]))
   plt.plot(x, params.ix[0,1] + params.ix[1,1]*x , color = diff_c(params.ix[2,0]))
   plt.xlabel(p)
   plt.ylabel(o)
   plt.show()

def plot_inter_res(data, outcome, predictor,bin_var,inter_var, model):

  # for i in xrange( len(data) ):
   shsy=plt.scatter(data.ix[ data['mom_hs']==0, predictor ],data.ix[ data['mom_hs']==0, outcome ],color = diff_c(0))
   shsn=plt.scatter(data.ix[ data['mom_hs']==1, predictor ],data.ix[ data['mom_hs']==1, outcome ],color = diff_c(1))

   x = np.linspace(int(np.min(data.ix[:,predictor])-3), int(np.max(data.ix[:,predictor])+3), 1000)
   params=pd.DataFrame([ [k,v] for k,v in m.params.iteritems()])
   lhsn, =plt.plot(x, params.ix[0,1] + params.ix[1,1]*x , color = diff_c(0))
   lhsy, =plt.plot(x, params.ix[0,1] + params.ix[1,1]*x + params.ix[2,1]+params.ix[3,1]*x, color = diff_c(1))
   plt.xlabel(p)
   plt.ylabel(o)
   plt.legend( ( shsy, shsn, lhsn, lhsy), ('no high school','high school attended','no high school','high school attended'), loc = 2, prop = {'size':8})
   plt.show()


# single predictor
p=['mom_iq']
o=['kid_score']
#tt, m =run_reg(df,o,p,'ols')
#plot_res(df,o,p,m)
# two predictors
p=['mom_iq']
b=['mom_hs']
o=['kid_score']
#tt, m =run_reg(df,o,p+b,'ols')
#plot_double_res(df,o,p,b,m)
#interactions
df['mom_hs_iq']= df['mom_iq']*df['mom_hs']
p=['mom_iq']
b=['mom_hs']
i=['mom_hs_iq']
o=['kid_score']
tt, m =run_reg(df,o,p+b+i,'ols','y')
#plot_double_res(df,o,p,b,m)
plot_inter_res(df, o, p,b,i,m)
