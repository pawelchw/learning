from sklearn.svm import SVR
import numpy as np

cols = im_sc_loop.tail(20).ix[:,1]

X = x_train_clean.ix[:,cols].as_matrix()
Xp = x_test_clean.ix[:,cols].as_matrix()
Y = l_train.as_matrix().ravel()

clf = SVR(C=1.0, epsilon = 0.2,kernel = 'linear')
clf.fit(X,Y)
pred = clf.predict(Xp)
l_test['pred'] = pred
print(l_test.head(20))
