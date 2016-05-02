import count_data_analysis as c
import matplotlib.pyplot as plt
s_mu, s_ob, s_es, s_model, s_map,  ml, g_df, s_mcmc = c.main()
obs = g_df
est = s_mcmc.trace('estimated')[:]
mu = s_mcmc.trace('mu')[:]
d = [ obs, est, mu]
x=[i for i in xrange(   min(   min(d[0]), min(d[1]), min(d[2])  )-1,   max(   max(d[0]), max(d[1]), max(d[2])  )+1 )   ]
x_l = ['','','']
y_l = ['val','val','val']
t_l = ['observed', 'estimated', 'estimated mu']
c.plt_comparison(d,x,x_l,y_l,t_l)
