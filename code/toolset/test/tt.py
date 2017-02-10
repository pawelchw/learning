for xx in aa.columns:

   if xx <> 'SalePrice':

      smc.smc_plot(aa, [xx, 'SalePrice'])
      plt.show()
