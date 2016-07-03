from __future__ import print_function

from scipy.special import comb, factorial

def n_r(n,r):

   l_res = 1

   for i in xrange(r):
      l_res=l_res*( n - (r-i)+1 )
   return l_res


print(4.0/ comb( 52 ,5 , exact=True))

##       4.0
## ---------------
##       52
##        5
##
print( 4.0*factorial(5, exact=True)/ n_r(52,5))
##    4.0 * 5!
## ----------------
##  52*51*50*49*48
##    
##
