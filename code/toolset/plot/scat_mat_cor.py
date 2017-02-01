import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn
import pandas as pd

def smc_plot(data, columns = [] ):

   cols = []

   if not columns:
      cols = data.columns
   else:
      cols = columns

   axs = pd.tools.plotting.scatter_matrix(data.ix[:,cols],alpha=0.2, diagonal ='kde')
   plt.show()

def net_plot(data, columns = []):

   cols = []

   if not columns:
      cols = data.columns
   else:
      cols = columns

   corrmat = data.ix[:,cols].corr()
   sn.heatmap(corrmat, vmax = 8, square = True)
   nets = corrmat.columns.get_level_values(0)#"policeCalls")

   f, ax = plt.subplots( figsize = (12,9) )
   for i,n in enumerate(nets):

      if i and n != nets[i-1]:

         ax.axhline( len(nets)-i, c="w")
         ax.axvline(i, c="w")

   f.tight_layout()
   #plt.show()
   return corrmat
