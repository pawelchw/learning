import numpy as np
import pandas as pd
import math
import pdb
def clean_nans(data, limit = 0.8):

   cnt = data.isnull().sum().tolist()
   cnt = [ i*1.0/len(cnt) for i in cnt]
   names = data.columns
   drop_names = []
   for xx in range( len(cnt) ):

      if cnt[xx] >= limit:

          drop_names.append( names[xx] )

   print(drop_names)
   return data.drop( drop_names, axis=1 )


def replace_with_avg(data, string_limit = 0.9):

    names=[]
    for xx in data.columns:#   ['communityname']:#   ['arsons']     ['fold']

      if data.ix[:,xx].dtype != 'object':

        ## gather first few values to discover if those are mainly numbers
        first_strings = data.ix[:,xx][:100]

        ##convert to is a number or not
        ##using to_numeric to convert non nums into nans
        num_test = [math.isnan(i) for i in pd.to_numeric(first_strings, errors='coerce')]
        #by mainly we mean at least string_limit  prct of values are nums

        if sum( num_test )*1.0 / len(first_strings) <= string_limit:

          #get a column we are looking at
          l_col = data.ix[:,xx].astype(float)
          #extract nums

          #l_col_nums = [ ii for ii in  l_col if ii!=  ] #l_col[ l_col <> '?' ]
          l_avg = np.nanmean( pd.to_numeric(l_col) )
          #print( str(l_col[ l_col.isnull() ].shape) +' '+ str(l_avg))
          l_col[ l_col.isnull() ] = l_avg
  
          data.ix[:,xx]= l_col
      else:

        l_col = data.ix[:,xx]
        max_row = pd.DataFrame(data.groupby( [xx] ).size().reset_index().sort_values([0], ascending=[0]).head(1))

        max_value = max_row.ix[:,xx]
        l_col[ l_col.isnull() ] = max_row.ix[:,0].tolist()
        data.ix[:,xx]= l_col

    return names,data


def outlier_stats(data, limit = 4):

   names = pd.DataFrame([], columns = ['names','mdev', 'prct', 'var','unq_val'])
   for xx in data.columns:

      if data.ix[:,xx].dtype != 'object':
         d = np.abs(data.ix[:,xx] - np.median(data.ix[:,xx]))
         mdev = np.median(d)
         s = d/mdev if mdev else d
         names.loc[len(names)] = [ xx
                                   , mdev
                                   , round(data.ix[:,xx][s<4].shape[0]*1.0/ len(data),4)
                                   , int(np.var( data.ix[:,xx] ))
                                   , data.groupby( xx ).size().shape[0]
                                   ]

   sorted_names = names.sort_values( ['prct','var'], ascending=[ True,True] ).reset_index()
   return sorted_names.ix[:,1:]


def replace_categorical(data, columns = []):

   names = []

   if not columns:
      names = data.columns
   else:
      names = columns

   df_trans = pd.DataFrame( [] )
   for xx in names:

      if data[ xx ].dtype == 'object':

         xxx = data.groupby( xx ).size().reset_index()
         aa = data[xx]
         bb = pd.DataFrame( [], columns = [xx] )

         for yy in range( len(aa) ):

            bb.loc[ len(bb) ] =  float(xxx[ xxx[ xx ]== aa.ix[yy,xx] ].index[0])

         df_trans[ xx+'_orig'] = data[xx]
         df_trans[ xx+'_tran'] = bb

   return df_trans
   
