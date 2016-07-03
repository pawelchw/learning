import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

def likelihood(x,h,t):
   return ( (x**h)*(1-x)**(t-h))

a,b = 1.0, 1.0
h = 11
t = 14
a_f = a+h
b_f = b+t-h
x = np.linspace( beta.ppf(0.01,a_f,b_f), beta.ppf(0.99,a_f,b_f), 100)

prior = beta.pdf(x,a,b)
like = [ i for i in likelihood(x,h,t)]
post =  beta.pdf(x,a_f,b_f)  


def plt_res(x, prior, like, post):
  colors = ['#348ABD', '#A60628', '#7A68A6', '#467821', '#D55E00', 
             '#CC79A7', '#56B4E9', '#009E73', '#F0E442', '#0072B2']
  x_min = np.min(x)
  x_max = np.max(x)
  fig = plt.figure(figsize=(10,6))
  fig.add_subplot(311)
  plt.plot(x,prior, color=colors[1])   
  plt.xlim(x_min, x_max)
  plt.ylabel('Frequency')
  plt.title('Prior')
  fig.add_subplot(312)
  plt.plot(x,like, color=colors[1])   
  plt.xlim(x_min,x_max)
  plt.ylim(0, np.max(like)+0.0001)
  plt.ylabel('Frequency')
  plt.title('Likelihood')
  fig.add_subplot(313)
  plt.plot(x,post,  color=colors[1])
  plt.ylabel('Frequency')
  plt.title('Posterior')
  plt.tight_layout()
  plt.show()

