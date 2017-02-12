o = ['SalePrice','Id']
names_not_pred = list(set(aa.columns) - set(o))  
o = ['SalePrice'] 
from sklearn.linear_model import Ridge

x_train, x_test, l_train, l_test = va.train_split(aa, o, names_not_pred, ratio = 0.3 )
l_train.ix[:,'SalePrice'] = np.log( 1 + l_train.ix[:,'SalePrice'] )
l_test.ix[:,'SalePrice'] = np.log( 1 + l_test.ix[:,'SalePrice'] )
X = x_train.ix[:, names_not_pred].as_matrix()
Y = l_train.ix[:, o].as_matrix().ravel()
from sklearn.grid_search import GridSearchCV

#k=['poly']#'rbf', 'linear','poly','sigmoid']
#c= [10,50,100,1000]#range(10,100,15)
#g=[0.0001,0.0005,0.001, 0.1]#np.arange(1e-4,1e-2,0.002)
#d = [2,3,4]
#param_grid=dict(kernel=k, C=c, gamma=g,degree=d)
a = np.arange(0.00001,20,0.05)
param_grid=dict(alpha = a)
print(param_grid)

clf = Ridge()
clf.fit( X,Y)


grid = GridSearchCV(clf, param_grid, cv=5)
grid.fit(x_test.ix[:, names_not_pred].as_matrix(), l_test.ix[:, o].as_matrix().ravel())  
print()
print("Grid scores on development set:")
print()  
print (grid.grid_scores_)
print("Best parameters set found on development set:")
print()
print(grid.best_params_)
print("Grid best score:")
print()
print (grid.best_score_)