from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import scipy.optimize as opt


h_o = 3
t_o = 9

def likelihood(x ,h ,t):
  return ( ( x**h ) * ( (1-x)**t))

pDataGivenTheta = [ likelihood(i ,h_o ,t_o) for i in Theta]
pData = sum( [i[0]*i[1] for i in zip(pDataGivenTheta,pTheta)])
pThetaGivenData = [  i[0]*i[1]/pData for i in zip(pDataGivenTheta, pTheta)]

heads = [ 1 for i in xrange(h_o) ]
tails = [ 0 for i in xrange(t_o) ]

data = heads + tails
p = np.linspace(0.01,0.99,20)

def ber_logprob(p, sign=-1):
   return np.sum( sign*stats.bernoulli.logpmf(data,p=p))

p_est = opt.minimize_scalar(ber_logprob)


colors = ['#348ABD', '#A60628', '#7A68A6', '#467821', '#D55E00', 
          '#CC79A7', '#56B4E9', '#009E73', '#F0E442', '#0072B2']

x_min = 10.0
x_max = 20.0

#p(t|d) = p(d|t)p(d)
N=63
t = np.linspace(0.0,1.0,N)
pt = [np.min([i, 1.0-i]) for i in t]
pdgt = [ likelihood(i ,h_o ,t_o) for i in t]
pd = sum( [ i[0]*i[1] for i in zip(pdgt,p,t)] )

ptgd = [ i[0] * i[1] / pd  for i in zip(pdgt,pt)]

def plt_res(t, pt, pdgt, ptgd):
  fig = plt.figure(figsize=(10,6))
  fig.add_subplot(311)
  plt.scatter(t,pt, color=colors[1])   
  plt.xlim(x_min, x_max)
  plt.ylabel('Frequency')
  plt.title('Prior')
  fig.add_subplot(312)
  plt.scatter(t,pdgt, color=colors[1])   
  plt.xlim(x_min,x_max)
  plt.ylim(0, np.max(pdgt)+0.0001)
  plt.ylabel('Frequency')
  plt.title('pDataGivenTheta')
  fig.add_subplot(313)
  plt.scatter(t,ptgd,  color=colors[1])
  plt.ylim(0, np.max(ptgd)+0.0001)
  plt.ylabel('Frequency')
  plt.title('pThetaGivenData')
  plt.tight_layout()
  plt.show()


plt_res(t=t, pt=pt, pdgt=pdgt, ptgd=ptgd)
plt_res(t=Theta, pt=pTheta, pdgt=pDataGivenTheta, ptgd=pThetaGivenData)
