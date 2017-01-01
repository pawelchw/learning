import matplotlib.pyplot as plt
import seaborn as sn
import numpy as np


def dec_boun(x,smodel):

    h = .01  # step size in the mesh
    # create a mesh to plot in
    x_min, x_max = x.ix[:, 0].min() - 1, x.ix[:, 0].max() + 1
    y_min, y_max = x.ix[:, 1].min() - 1, x.ix[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))


    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, m_max]x[y_min, y_max].
    Z = smodel.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.contour(xx, yy, Z, cmap=plt.cm.Paired)
    plt.show()






def p_log(d ,p, o, params):

   plt.scatter(d.ix[:, [o]], d.ix[:, [p]])
   x = np.linespace(np.min(d.ix[:, [p]])-1,np.max(d.ix[:, [p]])+1,1000)
   y = [(1.0 + np.tanh((params[0] + params[1]*i)/2.0) ) / 2 for i in x]
   plt.plot(x,y)
   plt.grid()
   plt.show()
