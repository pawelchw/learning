cor_names = [ ex_col.ix[i,:2].tolist() for i in xrange(len(ex_col))]
c_names = []

for xx in xrange( len(cor_names) ):

   c_names = c_names + cor_names [xx]

print(ex_col)
smc.smc_plot(df_cln, c_names)
#prep plot of correlated features
