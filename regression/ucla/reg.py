from __future__ import print_function
import numpy as np
import pandas as pd
import csv
import string
import statsmodels.api as sm
import matplotlib.pyplot as plt

c = pd.read_csv("/home/pawel-dell/learning/datasets/regression/ucla/sample.csv")
c.columns = ['female','read','write','math','hon','femalexmath']

logit = sm.Logit(c['hon'], sm.add_constant(c.ix[:, ['female']]))
res= logit.fit()
print(res.summary())
ctab  = pd.crosstab(c['hon'], c['female'])
logit = sm.Logit(c['hon'], c.ix[:, ['female']])
print('Parameter:', res.params, '\nExponential of the parameter: ',np.exp(res.params))

print('\n\nTotal males: ',  np.sum(ctab.ix[:,0]))
print('Males in hon class: ',  np.sum(ctab.ix[1,0]))
print('Males not in hon class: ',  np.sum(ctab.ix[0,0]))
print('The odds of being in honorous class(',np.sum(ctab.ix[1,0]) ,'/',np.sum(ctab.ix[0,0]) ,'): ' \
     , np.sum(ctab.ix[1,0])*1.0 / np.sum(ctab.ix[0,0]) \
     , ' , which is the same as the exponent of the intercept');
print('Male is the reference group since, female=0 \n\n ')
print('Total females: ',  np.sum(ctab.ix[:,1]))
print('Females in hon class: ',  np.sum(ctab.ix[1,1]))
print('Females not in hon class: ',  np.sum(ctab.ix[0,1]))
print('The odds of being in honorous class(',np.sum(ctab.ix[1,1]) ,'/',np.sum(ctab.ix[0,1]) ,'): ' \
       , 1.0*np.sum(ctab.ix[1,1]) /np.sum(ctab.ix[0,1]))
print('The ratio of the odds of females to males is( [' \
      , np.sum(ctab.ix[1,1]) , '/' , np.sum(ctab.ix[0,1]) , ' ] / [ ' \
      , np.sum(ctab.ix[1,0]) , '/' , np.sum(ctab.ix[0,0]) , ' ] ) : ' \
      , (1.0*np.sum(ctab.ix[1,1]) / np.sum(ctab.ix[0,1])) / (1.0*np.sum(ctab.ix[1,0]) / np.sum(ctab.ix[0,0])) \
      , ', which is the same as the exponent of the coefficient of female'
      )


logit = sm.Logit(c['hon'], sm.add_constant(c.ix[:, ['math']]))
print('\n\n')
res= logit.fit()
print(res.summary())
print('\nParameter:', res.params, '\nExponential of the parameter: ',np.exp(res.params))
print('\n\nThe estimated coefficient for the intercept is the log odds of a student with a math score of zero being in an honors class')
print('Now we can see this is very low due to the math scores being distributed around the value of 50')
print('\n\n The coefficient of math corresponds to the chage of log odds of being in a honorous class with a unit increase in the math score')
print('Therefore, the odds of being in the honrous class increase by exp(',res.params[1],')=',np.exp(res.params[1]) ,', which is roughly 17%')


print('\n\n')

logit = sm.Logit(c['hon'], sm.add_constant(c.ix[:, ['math','female','read']]))
print('\n\n')
res= logit.fit()
print(res.summary())
print('\nParameter:', res.params, '\nExponential of the parameter: ',np.exp(res.params))
print('This fitted model says that, holding math and reading at a fixed value, the odds of getting into an honors class for females (female = 1)over the odds of getting into an honors class for males (female = 0) is exp(',res.params[1],') = ',np.exp(res.params[1]),'; which corresponds to 166% of chance increase. ')



c.ix[:,'fmath']=c['math']*c['female']

print('\n\n')

logit = sm.Logit(c['hon'], sm.add_constant(c.ix[:, ['math','female','fmath']]))
print('\n\n')
res= logit.fit()
print(res.summary())

print('\nThe equation has got the following form:','\nlogit(p) = log(p/(1-p))= B0 + B1*female + B2*math + B3*female*math', \
      ' that can be split further in this order: ')
print('For males (female=0), the equation is simply','\nlogit(p) = log(p/(1-p))= B0 + B2*math.' \
     , '\nFor females, the equation is:', '\nlogit(p) = log(p/(1-p))= (B0 + B1) + (B2 + B3 )*math.'
     )
print('\n Therefore, one unit increase of math score per student group has the following impact:' \
     , '\n...1) for male student that is exp(B2) = exp(',res.params[1],') = ', np.exp(res.params[1])
     , '\n...2) for female student that is exp(B2 + B3) = exp(',res.params[1]+res.params[3],') = ', np.exp(res.params[1]+res.params[3])
     )
print( '\nThe ration of the odds ratio for males an females is;' \
     , '\n(',np.exp(res.params[1]+res.params[3]) ,'/',np.exp(res.params[1]) , ' ) = ', np.exp(res.params[1]+res.params[3]) / np.exp(res.params[1]) \
     , '\nwhic is the exponent of exp(',np.log(np.exp(res.params[1]+res.params[3]) / np.exp(res.params[1])),')= '\
     , np.exp(res.params[1]+res.params[3]) / np.exp(res.params[1])
     , ' which is the intercept for fmath.'
     )
