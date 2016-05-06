'''
Simple analysis of the file found here
https://datamarket.com/data/set/22p5/number-of-deaths-and-serious-injuries-in-uk-road-accidents-each-month-jan-1969-dec-1984-seatbelt-law-introduced-in-feb-1983-indicator-in-second-column#!ds=22p5!2eks&display=line
'''
from __future__ import print_function
import pandas as pd
import numpy as np
import pymc as pm
import scipy.stats as stats
import scipy.optimize as opt
import matplotlib.pyplot as plt
plt.style.use('bmh')
colors = ['#348ABD', '#A60628', '#7A68A6', '#467821', '#D55E00', 
          '#CC79A7', '#56B4E9', '#009E73', '#F0E442', '#0072B2']


M=50000
B = 5000
g_df = 0
def load_csv( path="aa" ):
   #accidents = df.ix[:,1]
   df = pd.read_csv("/home/pawel-dell/learning/datasets/count_data/car_accidents/cars.csv")
   return df.ix[:,1]

def plt_comparison( p_data
                  , p_x
                  , p_x_label
                  , p_y_label
                  , p_title
                  , p_add_mu = 'n'
                  ):
  global colors
  fig = plt.figure(figsize=(10,6))
  x_min = np.min(p_x)
  x_max = np.max(p_x)
  l_start = 0
  
  if p_add_mu == 'y':
      l_start=1
      fig.add_subplot( int(str(len(p_data)+l_start) + '11' ) )
      x = [i for i in xrange(len(p_data[0]))]
      plt.plot(x,p_data[0])

      for i in xrange(1,len(p_data)):

        y=np.mean(p_data[i])
        y_seq = [y for s in x]
        plt.plot(x,y_seq)

      

  for i in xrange( len(p_data) ):

    # add stacked charts
    # this many charts - int(str(len(z))
    # this many columns - '1'
    # this exactly char - str(i+1)
    fig.add_subplot( int(str(len(p_data)+l_start) + '1' + str(l_start+i+1) ) )
    plt.hist(p_data[i], range=[x_min, x_max], bins=100, histtype='stepfilled', color=colors[1])   
    plt.xlim(x_min, x_max)
    plt.xlabel( p_x_label[i] )
    plt.ylabel( p_y_label[i] )
    plt.title( p_title[i] )

#at first we run (-) minimum likelihood optimisation

def poisson_logprob(mu):

   global g_df
   return (-1.0)*np.sum( stats.poisson.logpmf( g_df, mu=mu  ))

def max_likelihood():
   return opt.minimize_scalar( poisson_logprob)   

def simple_mcmc_model( p_df ):

   s_mu = pm.Normal('mu', mu=np.mean(p_df), tau=0.00001)
   s_ob = pm.Poisson('observed', mu=s_mu,value=p_df, observed=True)
   s_es = pm.Poisson('estimated',mu=s_mu, observed=False)

   s_model = pm.Model([ s_mu, s_ob, s_es ])
   return s_mu ,s_ob ,s_es ,s_model

def max_a_posteriori( p_model ):

   ma = pm.MAP(p_model)
   ma.fit()
   return ma

def mcmc_estimation( N,B, p_model ):

   mcmc = pm.MCMC(p_model)
   mc_res = mcmc.sample(N,B)
   return mcmc

def negative_b_mcm_model( p_df ):

  n_mu =  pm.Normal('n_mu', mu=1650, tau=0.00001)
  n_lam = pm.Uniform('n_uni_alpha',0,1)
  n_alpha = pm.Exponential('n_alpha', beta=n_lam)
  n_ob = pm.NegativeBinomial('n_observed', mu=n_mu, alpha = n_alpha, value=p_df, observed=True)
  n_es = pm.NegativeBinomial('n_estimated',mu=n_mu, alpha = n_alpha, observed=False)
  n_model = pm.Model([ n_mu, n_lam, n_alpha, n_ob, n_es ])

  return n_mu, n_lam, n_alpha, n_ob, n_es, n_model

def two_model_comparison( p_df ):

   a_n = len(p_df)
   d_lam = pm.Uniform('d_lam',0,1)
   #d_lam = 1.0 / np.mean(p_df)
   lambda_1 = pm.Exponential("lambda_1", d_lam)
   #lambda_1 = pm.Uniform("lambda_1", min(p_df), max(p_df))
   lambda_2 = pm.Exponential("lambda_2", d_lam)
   #lambda_2 = pm.Uniform("lambda_2",min(p_df), max(p_df))

   #tau = pm.DiscreteUniform("tau", lower=min(p_df), upper=max(p_df) )
   tau = pm.DiscreteUniform("tau", lower=0, upper=max(p_df) )
   @pm.deterministic
   def lambda_(tau=tau, lambda_1=lambda_1, lambda_2=lambda_2):
      out = np.zeros(a_n)
      out[:tau] = lambda_1  # lambda before tau is lambda1
      out[tau:] = lambda_2  # lambda after (and including) tau is lambda2
      return out

   d_obs = pm.Poisson('d_observed', mu=lambda_, value=p_df, observed=True)

   d_model = pm.Model([d_obs, d_lam, lambda_1, lambda_2, tau])
   #d_model = pm.Model([d_obs,  lambda_1, lambda_2, tau])

   return d_model, d_obs, d_lam, lambda_1, lambda_2, tau

def three_model_comparison( p_df ):

   a_n = len(p_df)
   t_lam = pm.Uniform('d_lam',0,1)
   #d_lam = 1.0 / np.mean(p_df)
   t_lambda_1 = pm.Exponential("t_lambda_1", t_lam)
   #t_lambda_1 = pm.Uniform("t_lambda_1", min(p_df), max(p_df))
   t_lambda_2 = pm.Exponential("t_lambda_2", t_lam)
   #t_lambda_2 = pm.Uniform("t_lambda_2",min(p_df), max(p_df))
   t_lambda_3 = pm.Exponential("t_lambda_3", t_lam)
   #t_lambda_2 = pm.Uniform("t_lambda_2",min(p_df), max(p_df))

   #tau = pm.DiscreteUniform("tau", lower=min(p_df), upper=max(p_df) )
   t_tau_1 = pm.DiscreteUniform("tau1", lower=0, upper=max(p_df)-1 )
   t_tau_2 = pm.DiscreteUniform("tau", lower=t_tau_1, upper=max(p_df) )
   @pm.deterministic
   def lambda_(tau_1=t_tau_1,tau_2=t_tau_2, lambda_1=t_lambda_1, lambda_2=t_lambda_2, lambda_3=t_lambda_3):
      out = np.zeros(a_n)
      out[:tau_1] = lambda_1  # lambda before tau_1 is lambda1
      out[tau_1:tau_2] = lambda_2  # lambda_2 between tau_1 and tau_2
      out[tau_2:] = lambda_3  # lambda after (and including) tau is lambda_3
      return out

   t_obs = pm.Poisson('t_observed', mu=lambda_, value=p_df, observed=True)

   t_model = pm.Model([t_obs, t_lam, t_lambda_1, t_lambda_2, t_lambda_3, t_tau_1, t_tau_2])
   #d_model = pm.Model([d_obs,  t_lambda_1, t_lambda_2, tau])

   return t_model, t_lam, t_lambda_1, t_lambda_2, t_lambda_3, t_tau_1, t_tau_2

def main():

   global g_df, M, B
   g_df=load_csv("aa")

   ml = max_likelihood()
   s_mu ,s_ob ,s_es ,s_model = simple_mcmc_model( g_df )
   s_map = max_a_posteriori( s_model )
   s_mcmc = mcmc_estimation( M, B, s_model )


   n_mu, n_lam, n_alpha, n_ob, n_es, n_model = negative_b_mcm_model( g_df )
   n_mcmc = mcmc_estimation( M, B, n_model )

   d_model, d_obs, d_lam, lambda_1, lambda_2, tau = two_model_comparison( g_df )
   d_mcmc = mcmc_estimation( M, B, d_model )

   t_model, t_lam, t_lambda_1, t_lambda_2, t_lambda_3, t_tau_1, t_tau_2= three_model_comparison( g_df )
   t_mcmc = mcmc_estimation( M, B, t_model )


   return s_mu, s_ob, s_es, s_model, s_map,  ml, g_df, s_mcmc, n_mu, n_lam, n_alpha, n_ob, n_es, n_model, n_mcmc\
        , d_model, d_obs, d_lam, lambda_1, lambda_2, tau, d_mcmc, t_model, t_lam, t_lambda_1, t_lambda_2\
        , t_lambda_3, t_tau_1, t_tau_2, t_mcmc


def d_main():

   global g_df, M, B
   g_df=load_csv("aa")

   d_model, d_obs, d_lam, lambda_1, lambda_2, tau = two_model_comparison( g_df )
   d_mcmc = mcmc_estimation( M, B, d_model )

   return d_model, d_obs, d_lam, lambda_1, lambda_2, tau, d_mcmc, g_df


def t_main():

   global g_df, M, B
   g_df=load_csv("aa")

   t_model, t_lam, t_lambda_1, t_lambda_2, t_lambda_3, t_tau_1, t_tau_2= three_model_comparison( g_df )
   t_mcmc = mcmc_estimation( M, B, t_model )

   return t_model, t_lam, t_lambda_1, t_lambda_2, t_lambda_3, t_tau_1, t_tau_2, t_mcmc, g_df

