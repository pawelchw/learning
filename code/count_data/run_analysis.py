
import sys
sys.path.insert(0, 'count_data_analysis')
import count_data_analysis as c
import matplotlib.pyplot as plt
'''
s_mu, s_ob, s_es, s_model, s_map,  ml, g_df, s_mcmc, n_mu, n_lam, n_alpha, n_ob, n_es, n_model, n_mcmc\
 , d_model, d_obs, d_lam, lambda_1, lambda_2, tau, d_mcmc, t_model, t_lam, t_lambda_1, t_lambda_2\
 , t_lambda_3, t_tau_1, t_tau_2, t_mcmc = c.main()


'''
t_model, t_lam, t_lambda_1, t_lambda_2, t_lambda_3, t_tau_1, t_tau_2, t_mcmc, g_df = c.t_main()

obs = g_df
l1 = t_mcmc.trace('t_lambda_1')[:]
l2 = t_mcmc.trace('t_lambda_2')[:]
l3 = t_mcmc.trace('t_lambda_3')[:]

d_d = [obs, l1, l2, l3]
x=[i for i in xrange(min(obs)-1, max(obs)+1)]
x_l=['','','','']
y_l = ['frequency','frequency','frequency','frequency']
t_l = ['data', 'l1', 'l2', 'l3']
c.plt_comparison(d_d,x,x_l,y_l,t_l,'y')
plt.show()
'''
d_model, d_obs, d_lam, lambda_1, lambda_2, tau, d_mcmc, g_df = c.d_main()
obs = g_df
l1 = d_mcmc.trace('lambda_1')[:]
l2 = d_mcmc.trace('lambda_2')[:]
d_d = [g_df, l1, l2]
x=[i for i in xrange(min(obs)-1, max(obs)+1)]
x_l=['','','']
y_l = ['frequency','frequency','frequency']
t_l = ['data', 'l1', 'l2']
c.plt_comparison(d_d,x,x_l,y_l,t_l)
plt.show()



s_mu, s_ob, s_es, s_model, s_map,  ml, g_df, s_mcmc, n_mu, n_lam, n_alpha, n_ob, n_es,\
n_model, n_mcmc,d_model, d_obs, d_lam, lambda_1, lambda_2, tau, d_mcmc = c.main()

obs = g_df
est = s_mcmc.trace('estimated')[:]
mu = s_mcmc.trace('mu')[:]
d = [ obs, est, mu]
x=[i for i in xrange(   min(   min(d[0]), min(d[1]), min(d[2])  )-1,   max(   max(d[0]), max(d[1]), max(d[2])  )+1 )   ]
x_l = ['','','']
y_l = ['frequency','frequency','frequency']
t_l = ['observed', 'estimated', 'estimated mu']
c.plt_comparison(d,x,x_l,y_l,t_l)
plt.show()

n_est = n_mcmc.trace('n_estimated')[:]
d_n = [ obs, est, n_est]
n_t_l = ['observed', 'estimated', 'estimated negative']
c.plt_comparison(d_n,x,x_l,y_l,n_t_l)
plt.show()


obs= g_df
l1 = d_mcmc.trace('lambda_1')[:]
l2 = d_mcmc.trace('lambda_2')[:]
x=[i for i in xrange(   min(   min(d[0]), min(d[1]), min(d[2])  )-1,   max(   max(d[0]), max(d[1]), max(d[2])  )+1 )   ]

x_l = ['','','']
y_l = ['frequency','frequency','frequency']

d_d = [obs, l1, l2]
d_t_l=['observed', 'l1','l2']
c.plt_comparison(d_d,x,x_l,y_l,d_t_l)
plt.show()
 
'''
