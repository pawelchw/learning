n_l = 5
n_short = names[:5]
samples = df.ix[:,n_short].sample(replace=False, frac=0.2)
samples = samples.reset_index()
#samples = samples.drop('index',axis=1)
ss = samples.ix[:,1:]

for xx in ss.columns:
   print(xx)
   ss.ix[:,xx] = pd.to_numeric(ss.ix[:,xx])

axs = pd.tools.plotting.scatter_matrix(ss,alpha=0.2, diagonal ='kde')
#samples = samples.reset_index()
#df_corr = samples.corr().as_matrix()

#for i,j in zip(*plt.np.triu_indices_from(axs,k=1)):
#   axs[i,j].annotate( "%.3f" %df_corr[i,j], (0.8, 0.8), xycords = 'axes fraction', ha = 'center', va='center')
'''
n = len(samples.columns)
for i in range(n):
   v = axs[i,0]
   v.yaxis.label.set_rotation(0)
   v.yaxis.label.set_ha('right')
   v.set_yticks(())
   h = axs[n-1,i]
   h.xaxis.label.set_rotation(90)
   h.set_xticks(())
'''
plt.show()


