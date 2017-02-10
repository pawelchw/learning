import pandas as pd
import numpy as np

def corr_greater_than( corrmat, data, limit = 0.85 ):

   extracted_colums = pd.DataFrame([], columns=['col1','col2','value', 'co1_unq_values', 'col2_unq_values'])
   extracted_colums_single = pd.DataFrame([], columns=['col','col_unq_values','corr_val'])

   for xx in range(len(corrmat.columns)):
      for yy in range(xx+1, len(corrmat.columns)):

         if corrmat.ix[xx,yy] >= limit :

           extracted_colums.loc[len(extracted_colums)] = [ corrmat.columns[xx]
                                                           , corrmat.columns[yy]
                                                           , corrmat.ix[xx,yy]
                                                           , data.groupby( [ corrmat.columns[xx] ] ).size().shape[0] 
                                                           , data.groupby( [ corrmat.columns[yy] ] ).size().shape[0] 
                                                         ]
           extracted_colums_single.loc[len(extracted_colums_single)] = [ corrmat.columns[xx]
                                                                         , data.groupby( [ corrmat.columns[xx] ] ).size().shape[0]
                                                                         , corrmat.ix[xx,yy]
                                                                       ]
           extracted_colums_single.loc[len(extracted_colums_single)] = [ corrmat.columns[yy]
                                                                         , data.groupby( [ corrmat.columns[yy] ] ).size().shape[0]
                                                                         , corrmat.ix[xx,yy]
                                                                       ]

   cols_summary = pd.DataFrame( extracted_colums.groupby( ['col1']).size(), columns=['cnt'] )

   df_max_unq_values = extracted_colums_single.ix[:, ['col','col_unq_values']].groupby( ['col'] ).aggregate( [ np.max ] ).reset_index()
   df_corr_stats = extracted_colums_single.ix[:, ['col','corr_val']].groupby( ['col'] ).aggregate( [ np.min,np.max,np.mean ] ).reset_index()

   df_max_unq_values_fnl =  pd.DataFrame( [], columns = [ i[0]+i[1] for i in df_max_unq_values.columns.tolist()])
   df_corr_stats_fnl =  pd.DataFrame( [], columns = [ i[0]+i[1] for i in df_corr_stats.columns.tolist()])

   for xx in range( len(df_max_unq_values) ) :

      df_max_unq_values_fnl.loc[ len(df_max_unq_values_fnl)] = [df_max_unq_values.ix[xx,:].tolist()[0], df_max_unq_values.ix[xx,:].tolist()[1]]

   for xx in range( len(df_corr_stats) ) :

      df_corr_stats_fnl.loc[ len(df_corr_stats_fnl)] = [ df_corr_stats.ix[xx,:].tolist()[0]
                                                         , df_corr_stats.ix[xx,:].tolist()[1]
                                                         , df_corr_stats.ix[xx,:].tolist()[2]
                                                         , df_corr_stats.ix[xx,:].tolist()[3]
                                                         ]



   df_merge = pd.merge(df_max_unq_values_fnl,df_corr_stats_fnl, on='col', how='inner')
   extracted_colums_single = df_merge.sort_values( [df_merge.columns[1]], ascending=[True]).reset_index().ix[:,1:]
   return extracted_colums,extracted_colums_single, cols_summary



def remove_corr_features(data, single_corr, multi_corr):

   names = []
   l_size = len( multi_corr )
   l_counter = 0
   while l_size > 0 and l_counter < len(single_corr):

      xx  = single_corr.ix[l_counter, 0]
      names.append(xx)
      multi_corr = multi_corr[ (multi_corr.col1 != xx) & (multi_corr.col2 != xx) ].reset_index().ix[:,1:]
      l_counter = l_counter + 1
      l_size = len(multi_corr)

   return data.drop( names, axis=1 )
