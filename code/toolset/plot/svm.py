import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn

def svm_plot(data, model):
   h = .05  # step size in the mesh
   # create a mesh to plot in
   x_min, x_max = data.ix[:, 0].min() - 1, data.ix[:, 0].max() + 2
   y_min, y_max = data.ix[:, 1].min() - 1, data.ix[:, 1].max() + 2
   xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                        np.arange(y_min, y_max, h))


   # Plot the decision boundary. For that, we will assign a color to eachx
   # point in the mesh [x_min, m_max]x[y_min, y_max].
   Z = model.predict(np.c_[xx.ravel(), yy.ravel()])

   # Put the result into a color plot
   Z = Z.reshape(xx.shape)
   plt.contour(xx, yy, Z, cmap=plt.cm.Paired)
   #plt.grid()
   plt.show()

