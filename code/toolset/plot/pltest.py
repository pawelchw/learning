import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn

def diff_c(flag):

   res = 'b'
   if flag == 1:
      res='r'
   return res



#def svm_plot(sx_te, model):
h = .1  # step size in the mesh
# create a mesh to plot in
x_min, x_max = sx_te.ix[:, 0].min() - 1, sx_te.ix[:, 0].max() + 1
y_min, y_max = sx_te.ix[:, 1].min() - 1, sx_te.ix[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))
   # Plot the decision boundary. For that, we will assign a color to each
   # point in the mesh [x_min, m_max]x[y_min, y_max].
Z = smodel.predict(np.c_[xx.ravel(), yy.ravel()])
   # Put the result into a color plot
Z = Z.reshape(xx.shape)

#def plot_double_res(sx_te, x1, x2, outcome):
df_t = sx_te.reset_index()
df_l = sl_te.reset_index()
for i in xrange( len(df_t) ):
   plt.scatter(df_t.ix[i,1],df_t.ix[i,2],color = diff_c(df_l.ix[i,o].ravel()))

plt.contour(xx, yy, Z, cmap=plt.cm.Paired)
plt.show()

