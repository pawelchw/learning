from sklearn import svm
from validate import train_split as ts

def sk_svm(data, outcome, predictors, train_ratio ):

  x_tr, x_te, l_tr, l_te = ts(data, outcome, predictors,  train_ratio )
  print( x_tr.shape)
  print( x_te.shape)
  model = svm.SVC(gamma=10, C=10.)
  model.fit(x_tr, l_tr)
  ypred = model.predict( x_te )
  return x_tr, x_te, l_tr, l_te,ypred, model
