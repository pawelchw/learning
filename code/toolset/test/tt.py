zz = pd.DataFrame( [], columns = aa.columns)
zz1 = pd.DataFrame( [], columns = aa.columns)
bb=aa.ix[:, ['col','col_unq_values'].groupby( ['col'] ).aggregate( [ np.max ] ).reset_index()
cc=aa.ix[:, ['col','corr_val']].groupby( ['col'] ).aggregate( [ np.min,np.max,np.mean ] ).reset_index()

for xx in xrange( len(bb) ) :

   zz.loc[ len(zz)] = [bb.ix[xx,:].tolist()[1], bb.ix[xx,:].tolist()[0]]
