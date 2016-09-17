from __future__ import print_function
from numpy.random import choice as choice

N = 1000
C = 6
total = 0
eyes = 0
for i in xrange(0,N):

   d_1 = choice(C,1 )+1
   d_2 = choice(C,1 )+1

   if d_1 == 1 and d_2 == 1 :
      eyes = eyes + 1
   else :
      total = total + 1

print('e:', eyes)
print('t:', total)
