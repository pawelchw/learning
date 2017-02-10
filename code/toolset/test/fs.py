aa = df_cln
for xx in aa.columns:

   if xx+'_tran' in df_cln_fnl.columns:#and aa[xx].dtype =='object':

      aa[xx] = df_cln_fnl[ xx+'_tran']



for xx in aa.columns[1:]:

   #dt = aax
   if ( xx != 'SalePrice' ) and (
           ( xx+'_orig' in df_cln_fnl.columns and str(df_cln_fnl[xx+'_orig'].dtype) <> 'object' ) # exists in trans and no str
        or ( not xx+'_orig' in df_cln_fnl.columns ) # does not exists in trans
      ):

        if aa.groupby(xx).size().shape[0] > len(aa)*1.0/2:
           c = aa.ix[:,xx]
           aa[xx] = ( c - np.mean(c))/ np.std(c)

#aa['YrMoSold'] = str(ax['YrSold']) + str(ax['MoSold'])
corrmat = smc.net_plot(aa)
l_col = pd.DataFrame( corrmat.ix[:,'SalePrice'].reset_index())
l_col.columns = ['col','corrval']


for xx in ['Id','SalePrice']:

   l_col = l_col[ l_col['col'] != xx]

l_col['abs'] = np.abs(l_col['corrval'])

l_col = l_col.sort_values( ['abs'], ascending=[False]).reset_index()
l_col = l_col.ix[:,1:]

#smc.smc_plot(aa, l_col.col[:10].tolist()+['SalePrice'])
