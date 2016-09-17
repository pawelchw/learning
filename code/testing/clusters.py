import numpy as np
import matplotlib.pyplot as plt
import pymc as pm
k = 3
ndata = 500
spread = 5
centres = np.array([ -spread,0, spread])
v = np.random.randint(0,k,ndata)
data = centres[v] + np.random.randn(ndata)

l_res = plt.hist(data)

plt.show()

a = pm.constant( np.array( [1., 1., 1.] ) )
p = pm.Dirichlet('p', a=a, shape = k)

p_min_potential = pm.Potential('p_min_potential', tt.switch(tt.min(p) < .1, -np.inf, 0) )

means = pm.Normal('means', mu=[0, 0, 0], sd=15, shape = k)

order_means_potential = pm.Potential(   'order_means_potential'
                                    , ttswitch(means[1]-means[0]<0,-np.inf,0)
                                    + ttswitch(means[2]-means[1]<0,-np.inf,0)
                                    )
