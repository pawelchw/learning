import pylab as pl
import matplotlib.pyplot as plt
from etl import fileread as f
from sklearn.linear_model import LogisticRegression as lr
import numpy as np
#df = f.space_read("/home/pch/learning/datasets/regression/gelman_reg/arsenic/wells.dat")
df['dist100'] = df['dist']/100
p = ['dist100','arsenic']
o = ['switch']

model = lr()
x = df.ix[:, p]
y = df.ix[:, o].values.ravel()
#x = x.reshape(len(x),1)
#y = y.reshape(len(y),1)
#model.fit( df.ix[:, p].as_matrix().ravel(), df.ix[:, o].as_matrix().ravel())
model.fit( x.as_matrix(),y)

x_min, x_max = float(np.min(x.dist100)-0.1), float(np.max(x.dist100)+0.1)
y_min, y_max = np.min(x.arsenic)-0.1, np.max(x.arsenic)+0.1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 50),
                     np.linspace(y_min, y_max, 50))
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())

#plot background colors
ax = plt.gca()
Z = model.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]
Z = Z.reshape(xx.shape)
cs = ax.contourf(xx, yy, Z, cmap='RdBu', alpha=.5)
cs2 = ax.contour(xx, yy, Z, cmap='RdBu', alpha=.5)
plt.clabel(cs2, fmt = '%2.1f', colors = 'k', fontsize=14)
Xtrain = x.as_matrix()
Ypred = model.predict( x.as_matrix() )


# Plot the points
ax.plot(Xtrain[Ypred == 0, 0], Xtrain[Ypred == 0, 1], 'ro', label='Class 1')
ax.plot(Xtrain[Ypred == 1, 0], Xtrain[Ypred == 1, 1], 'bo', label='Class 2')

# make legend
plt.legend(loc='upper left', scatterpoints=1, numpoints=1)
plt.show()
