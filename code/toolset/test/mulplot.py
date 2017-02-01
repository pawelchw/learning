import seaborn as sns
corrmat = x_train.ix[:,:50].corr()
sns.heatmap(corrmat, vmax = 8, square = True)
nets = corrmat.columns.get_level_values(0)#"policeCalls")

f, ax = plt.subplots( figsize = (12,9) )
for i,n in enumerate(nets):

   if i and n != nets[i-1]:

      ax.axhline( len(nets)-i, c="w")
      ax.axvline(i, c="w")

f.tight_layout()
plt.show()
