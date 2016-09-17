import numpy as np
import matplotlib.pyplot as plt
#how many elements
a = 2
# how many trials
n = 1000
# p of success
p = 0.5
res = np.random.binomial(a, p, n)
proportion=np.zeros(n)
h = 0
t = 0
for i in xrange(n):
   if res[i]==1:
      h = h + 1
   else:
      t = t + 1
   proportion[i] = ( h * 1.0 ) / ( h + t )

plt.plot(proportion, color='red', linewidth=1.0, label='Coin Toss Proportion')
plt.legend(loc = 'upper left', frameon = False)
