import matplotlib.pyplot as plt

def outlier_histogram(data,outlier_names, x, y, limit=0.8):

   out_names = outlier_names[ outlier_names.prct < limit].names.tolist()
   fig = plt.figure()

   for xx in xrange(len(out_names)):
     ax = fig.add_subplot(x,y,xx+1)
     plt.hist( data.ix[:, out_names[xx]], bins=100, label = out_names[xx])
     ax.set_title( out_names[xx] )


   plt.show()
