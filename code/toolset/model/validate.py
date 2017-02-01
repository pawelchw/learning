from sklearn.cross_validation import train_test_split as tts
import numpy as np

def train_split(data, outcome, predictors, ratio = 0.3 ):

   x_train, x_test, l_train, l_test = tts(data[predictors], data[outcome],test_size=ratio, random_state=123)
   return x_train, x_test, l_train, l_test

def data_std(data, cols, std = 0):

   columns = []
   if not cols:
      columns = data.columns
   else:
      columns = cols

   if std == 1:

      for xx in columns:

         data.ix[:,xx]= ( data.ix[:,xx] - np.mean(data.ix[:,xx])) / np.std(data.ix[:,xx])

   else:

      for xx in columns:

         data.ix[:,xx]= ( data.ix[:,xx] - np.mean(data.ix[:,xx]))


   return data


def train_data_std(data, std, avg ):

   columns = std.ix[:,0]

   for xx in columns:

       data.ix[:,xx]= ( data.ix[:,xx] - np.float(avg[ avg[0]==xx][1]) ) / np.float( std[ std[0]==xx][1] )


   return data
