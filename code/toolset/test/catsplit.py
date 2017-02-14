#import pandas as pd

aa = df_cln.copy()
for xx in aa.columns:
  if aa[ xx ].dtype == 'object':
      tmp_col = [ i.replace(" ", "") for i in aa[ xx ]]
      tmp_df = pd.DataFrame(tmp_col, columns=[xx])
      tmp_store = pd.get_dummies(tmp_df[xx], prefix=xx+'_')
      aa.drop(xx, axis=1)
      aa[tmp_store.columns.tolist()] = tmp_store


         
df_f = aa.copy()
df_f = df_f.drop(['Id'],axis=1)


a,b,c= ca.corr_greater_than(corrmat,df_f)
df_fi = ca.remove_corr_features(df_f, b,a)
corrmat = smc.net_plot(df_fi)
l_col = pd.DataFrame( corrmat.ix[:,'SalePrice'].reset_index())
l_col.columns = ['col','corrval']


for xx in ['Id','SalePrice']:

   l_col = l_col[ l_col['col'] != xx]

l_col['abs'] = np.abs(l_col['corrval'])

l_col = l_col.sort_values( ['abs'], ascending=[False]).reset_index()
l_col = l_col.ix[:,1:]
