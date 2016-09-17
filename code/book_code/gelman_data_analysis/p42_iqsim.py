from __future__ import print_function
import numpy as np
import pandas as pd
import csv
import string
import statsmodels.api as sm
import matplotlib.pyplot as plt
import pymc3 as pm
import seaborn as sns

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

def plot_sns(df,trace, b0, b1, predictor, outcome, sams = 100, lsp = 1000):
    #mom_iq  ---> x
    #kid_score  ---> y
    #sns.lmplot(x="x", y="y", data=df, size=10, fit_reg=False)

    xn = int(np.min(df.ix[:,predictor]-10))
    xx = int(np.max(df.ix[:,predictor]+10))
    yn = int(np.min(df.ix[:,outcome]-10))
    yx = int(np.max(df.ix[:,outcome]+10))
    
    plt.xlim(xn, xx)
    plt.ylim(yn, yx)
    plt.scatter(df.ix[:,predictor],df.ix[:,outcome])
    x = np.linspace(xn,xx,lsp)
    pm.glm.plot_posterior_predictive(trace, samples=sams, eval = x)
    y = b0 + b1*x
    plt.plot(x, y, label="True Regression Line", lw=3., c="red")
    '''
    x = np.linspace(0, 200, 1000)
    
    plt.legend(loc=0)
    x = np.linspace(0, 1, N)
    y = beta_0 + beta_1*x
    plt.plot(x, y, label="True Regression Line", lw=3., c="green")
    plt.legend(loc=0)
    '''
    plt.show()

def m_inf(df, it=5000):


    basic_model = pm.Model()
    with basic_model:
        # Create the glm using the Patsy model syntax
        # We use a Normal distribution for the likelihood
        pm.glm.glm('y ~ x' , df, family=pm.glm.families.Normal())

        # Use Maximum A Posteriori (MAP) optimisation as initial value for MCMC
        start = pm.find_MAP()

        # Use the No-U-Turn Sampler
        step = pm.NUTS()

        # Calculate the trace
        trace = pm.sample(
            it, step, start, 
            random_seed=42, progressbar=True
        )

    return trace

def m_inf_t(df, it=5000):


    basic_model = pm.Model()
    with basic_model:
        # Create the glm using the Patsy model syntax
        # We use a Normal distribution for the likelihood
        pm.glm.glm('y ~ x' , df, family=pm.glm.families.StudentT())

        # Use Maximum A Posteriori (MAP) optimisation as initial value for MCMC
        start = pm.find_MAP()

        # Use the No-U-Turn Sampler
        step = pm.NUTS()

        # Calculate the trace
        trace = pm.sample(
            it, step, start, 
            random_seed=42, progressbar=True
        )

    return trace


# single predictor
p=['x']
o=['y']
#os = 'y'
#ps='x'
#p=['mom_iq']
#o=['kid_score']
print(df.head())
df.columns=['y','a','x','b','c']
tt, m =run_reg(df,o,p,'ols','y')
params=pd.DataFrame([ [k,v] for k,v in m.params.iteritems()])
l_trace = m_inf_t(df, it=5000)
plot_sns(df,l_trace, params.ix[0,1], params.ix[1,1], p, o)
l_trace = m_inf(df, it=5000)
plot_sns(df,l_trace, params.ix[0,1], params.ix[1,1], p, o)
#plot_res(df,o,p,m)
