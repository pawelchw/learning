from sklearn.ensemble import AdaBoostRegressor
from sklearn.metrics import mean_squared_error, explained_variance_score
from sklearn.utils import shuffle
from sklearn.tree import DecisionTreeRegressor

mse = 100
eva = 100
added_feature = ''
feature_corr = 10
prev_mse = 100
prev_eva = 100
o = ['SalePrice']
ol = ['sp_log']
aa [ol] = np.log( 1+ aa[o])
df_l = aa.ix[:,ol].as_matrix().ravel()

df_res_sng = pd.DataFrame([], columns=['feature','cor','prev_mse','prev_eva','mse','eva'])
columns =[]
l_max_depth = 4

for xx in l_col.col.tolist():

   l_cor = l_col[l_col.col == xx].ix[:,1].tolist()
   columns = columns+ [xx]
   df_t = aa.ix[:, columns].as_matrix()
   X,y = shuffle(df_t, df_l,random_state=123)
   num_training = int(0.8 * len(X))
   Xtr, ytr = X[:num_training], y[:num_training]
   Xte, yte = X[num_training:], y[num_training:]
   regdt = DecisionTreeRegressor(max_depth = l_max_depth)
   regdt.fit(Xtr,ytr)
   reg = AdaBoostRegressor( n_estimators = 400, random_state=123)
   reg.fit(Xtr,ytr)
   y_pred = reg.predict(Xte)
   prev_mse = mse
   prev_eva = eva
   mse = mean_squared_error(yte,y_pred)
   eva = explained_variance_score(yte,y_pred)
   df_res_sng.loc[len(df_res_sng)] = [xx, l_col.corrval[l_col.col == xx].tolist(), prev_mse,prev_eva,mse,eva]


df_res = pd.DataFrame([], columns=['feature','cor','prev_mse','prev_eva','mse','eva'])          
for xx in l_col.col.tolist():

   l_cor = l_col[l_col.col == xx].ix[:,1].tolist()
   columns = columns+ [xx]
   df_t = aa.ix[:, columns].as_matrix()
   X,y = shuffle(df_t, df_l,random_state=123)
   num_training = int(0.8 * len(X))
   Xtr, ytr = X[:num_training], y[:num_training]
   Xte, yte = X[num_training:], y[num_training:]
   regdt = DecisionTreeRegressor(max_depth = l_max_depth)
   regdt.fit(Xtr,ytr)
   reg = AdaBoostRegressor(DecisionTreeRegressor(max_depth = l_max_depth), n_estimators = 400, random_state=123)
   reg.fit(Xtr,ytr)
   y_pred = reg.predict(Xte)
   prev_mse = mse
   prev_eva = eva
   mse = mean_squared_error(yte,y_pred)
   eva = explained_variance_score(yte,y_pred)
   df_res.loc[len(df_res)] = [xx, l_col.corrval[l_col.col == xx].tolist(), prev_mse,prev_eva,mse,eva]

