import matplotlib.pyplot as plt
import numpy as np

def p_log(d ,p, o, params)

   plt.scatter(d.ix[:, [o]], d.ix[:, [p]])
   x = np.linespace(np.min(d.ix[:, [p]])-1,np.max(d.ix[:, [p]])+1,1000)
   y = [(1.0 + np.tanh((params[0] + params[1]*i)/2.0) ) / 2 for i in x]
   plt.plot(x,y)
   plt.grid()
   plt.show()
