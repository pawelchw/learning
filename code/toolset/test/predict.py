import numpy as np
import matplotlib.pyplot as plt


def pred(point):
  x = 6
  y = 5
  r = 4
  c1 = ( x - point[0]) ** 2
  c2 = ( y - point[1] ) ** 2

  x = 2
  y = 4
  r = 2
  e1 = ( ( x - point[0]) ** 2) / 0.16
  e2 = ( ( y - point[1] ) ** 2) / 2.0

  if (c1 + c2 <= r) or (e1 + e2 <= r):
     return 1
  else:
     return 0

def diff_c(flag):

   res = 'b'
   if flag == 1:
      res='r'
   return res

def plot_circle(data):

   for i in xrange( len(data) ):
      plt.scatter(data[i][0],data[i][1],color = diff_c( pred(data[i]) ) )
   plt.show()

def svm_plot(data):
   h = .01  # step size in the mesh
   # create a mesh to plot in
   x_min, x_max = data[:, 0].min() - 1, data[:, 0].max() + 1
   y_min, y_max = data[:, 1].min() - 1, data[:, 1].max() + 1
   xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                        np.arange(y_min, y_max, h))


   # Plot the decision boundary. For that, we will assign a color to each
   # point in the mesh [x_min, m_max]x[y_min, y_max].
   a = np.c_[xx.ravel(), yy.ravel()]
   b = np.array([pred(i) for i in a])
   #Z = model.predict(np.c_[xx.ravel(), yy.ravel()])

   # Put the result into a color plot
   Z = b.reshape(xx.shape)
   plt.contour(xx, yy, Z, cmap=plt.cm.Paired)
   plt.show()

xn = 0
xx = 10
yn = 0
yx = 8
mean = [5,5]
cov = [ [5,0] , [10,10] ]
nums = []
N = 3000
t_s = np.random.multivariate_normal(mean,cov,N) 
for i in xrange(N):
  a = t_s[i]
  if a[0]>= xn and a[0]<=xx and a[1] >= yn and a[1] <= yx:
    nums.append(a.ravel())

nums = np.array(nums)

