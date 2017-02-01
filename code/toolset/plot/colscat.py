import matplotlib.pyplot as plt

def diff_c(flag):

   res = 'b'
   if flag == 1:
      res='r'
   return res

def plot_double_res(data, x1, x2, outcome):

   for i in xrange( len(data) ):
      plt.scatter(data.ix[i,x1],data.ix[i,x2],color = diff_c(data.ix[i,outcome].ravel()))
   plt.grid()
   plt.show()
def plot_circle(data):

   for i in xrange( len(data) ):
      plt.scatter(data[i][0],data[i][1],color = diff_c( pred(data[i]) ) )
