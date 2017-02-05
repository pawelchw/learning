aa = df_cln
for xx in aa.columns:

   if aa[xx].dtype =='object':

      aa[xx] = df_cln_fnl[ xx+'_tran']


aa = aa.ix[:,1:]

for xx in aa.columns:

   if xx != 'SalePrice':

     c = aa.ix[:,xx]
     aa[xx] = ( c - np.mean(c))/ np.std(c)



aa [ 'SalePrice'] = np.log( 1+aa.ix[:, 'SalePrice'])

from sklearn.decomposition import PCA

pca = PCA()

o = ['SalePrice']
names_not_pred = list(set(aa.columns) - set(o))   
from sklearn.svm import SVR

'''
x_train, x_test, l_train, l_test = va.train_split(aa, o, names_not_pred, ratio = 0.3 )
x_train_tr = pca.fit_transform(x_train)
x_test_tr = pca.transform(x_test)

clf = SVR(C=2.0, epsilon = 0.01, kernel = 'poly')
clf.fit(x_train_tr,l_train.as_matrix())
l_test_out = clf.predict(x_test_tr)

l_test[ 'pred'] = l_test_out
outp = [ int(i) for i in abs(np.exp(l_test[ 'pred'].as_matrix())-1 - (  np.exp(l_test[ 'SalePrice'].as_matrix())) -1 )]

www=plt.hist(outp, bins=100)
plt.show()
'''
o = ['SalePrice']
names_not_pred = list(set(aa.columns) - set(o))   

X = aa.ix[:, names_not_pred].as_matrix()
Y = aa.ix[:, o].as_matrix().ravel()


Xtr = pca.fit_transform(X)

from sklearn.grid_search import GridSearchCV
k=['rbf', 'linear','poly','sigmoid']
c= range(1,100)
g=np.arange(1e-4,1e-2,0.0001)
g=g.tolist()
param_grid=dict(kernel=k, C=c, gamma=g)
print param_grid
clf = SVR()

grid = GridSearchCV(clf, param_grid, cv=5) #,scoring='accuracy')
grid.fit(Xtr, Y)  
print()
print("Grid scores on development set:")
print()  
print grid.grid_scores_  
print("Best parameters set found on development set:")
print()
print(grid.best_params_)
print("Grid best score:")
print()
print (grid.best_score_)
