import pandas as pd

def corr_greater_than( corrmat, data, limit = 0.8 ):

   extracted_colums = pd.DataFrame([], columns=['col1','col2','value', 'co1_unq_values', 'col2_unq_values'])
   extracted_colums_single = pd.DataFrame([], columns=['col','col_unq_values'])

   for xx in xrange(len(corrmat.columns)):
      for yy in xrange(xx+1, len(corrmat.columns)):

         if corrmat.ix[xx,yy] >= limit :

           extracted_colums.loc[len(extracted_colums)] = [ corrmat.columns[xx]
                                                           , corrmat.columns[yy]
                                                           , corrmat.ix[xx,yy]
                                                           , data.groupby( [ corrmat.columns[xx] ] ).size().shape[0] 
                                                           , data.groupby( [ corrmat.columns[yy] ] ).size().shape[0] 
                                                         ]
           extracted_colums_single.loc[len(extracted_colums_single)] = [ corrmat.columns[xx]
                                                                         , data.groupby( [ corrmat.columns[xx] ] ).size().shape[0]
                                                                       ]
           extracted_colums_single.loc[len(extracted_colums_single)] = [ corrmat.columns[yy]
                                                                         , data.groupby( [ corrmat.columns[yy] ] ).size().shape[0]
                                                                       ]

   cols_summary = pd.DataFrame( extracted_colums.groupby( ['col1']).size(), columns=['cnt'] )
   return extracted_colums,extracted_colums_single, cols_summary

