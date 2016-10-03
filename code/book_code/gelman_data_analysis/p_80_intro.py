####
#this code shows that thre functions return the same values for 
# different input values of x
###
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-20,20,100)

def a(x):
   return 1.0*np.exp(x) / ( 1 + np.exp(x) )
def b(x):
   return 1.0 / ( 1.0 + np.exp(-x) )
def c(x):
   return (1.0 + np.tanh( ( 1.0 * x) / 2) ) / 2

#test if functions return the same values

print ( "a(x) and b(x): ", np.allclose(a(x),b(x)))
print ( "a(x) and c(x): ", np.allclose(a(x),c(x)))

#ploting 2 functions
#1st the logit funciton
#2nd function from the book
plt.plot(x, a(x), label="logit(x)")
plt.plot(x, a(-1.40 + 0.33*x), label="logit(-1.40 + 0.33x")
plt.grid()
plt.legend(loc = 'upper left')
plt.show()


