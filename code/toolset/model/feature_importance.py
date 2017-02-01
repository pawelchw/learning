from sklearn.cross_validation import ShuffleSplit
from sklearn.metrics import r2_score
from collections import defaultdict
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import pandas as pd

def feature_importance_loop( Data_x, Data_y):

   X = Data_x.as_matrix()
   Y = Data_y.as_matrix().ravel()

   rf = RandomForestRegressor()
   scores = defaultdict(list)
   names = Data_x.columns

   for trid,teid in ShuffleSplit( len(X), 100, 3):

      Xtr,Xte = X[trid], X[teid]
      Ytr,Yte = Y[trid], Y[teid]
      r = rf.fit(Xtr, Ytr)
      acc = r2_score(Yte, rf.predict(Xte))

      for xx in  xrange(X.shape[1]):

          Xt = Xte.copy()
          np.random.shuffle( Xt[:,xx])
          shuff_acc = r2_score(Yte, rf.predict(Xt))
          scores[ names[xx] ].append( (acc-shuff_acc) / acc )

   return pd.DataFrame(sorted( [ ( round(np.nanmean(score),4), feat) for feat,score in scores.items()], reverse = True) )
