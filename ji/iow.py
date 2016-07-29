from __future__ import print_function
import numpy as np
import pandas as pd
import csv
import string
import statsmodels.api as sm
import matplotlib.pyplot as plt
import pdb

'''
proper print out
>>> for i in tr['Agent'].unique() :
...     ''.join(['if df[\'Agent\'] ==\'',i,'\':','df[\'',i,'\']==1'])
'''


c = pd.read_csv("/home/pawel-dell/learning/cv_pack/iwo/calls.csv", skiprows = 1)
l = pd.read_csv("/home/pawel-dell/learning/cv_pack/iwo/leads.csv", skiprows = 1)
s = pd.read_csv("/home/pawel-dell/learning/cv_pack/iwo/signups.csv", skiprows = 1)

c.columns =[ 'Phone_Number','Call_Outcome','Agent','Call_Number']
l.columns =[ 'Name', 'Phone_Number','Region','Sector','Age']
#s.columns =[ 'Lead', 'Approval','Decision']

##the most calls
##
'''
Which agent made the most calls? 
'''
###
def question_1():
   print(c.groupby('Agent').size())

###
'''
For the leads that received one or more calls, how many calls were received on
average?
'''
### 

def question_2():
  cl = pd.merge(c,l, on='Phone_Number', how='inner', indicator=True)
  #called more than once
  a = cl.groupby('Phone_Number')
  b = a.filter( lambda x: len(x) > 1)
  d=b.groupby("Phone_Number")
  e=d['Agent'].aggregate( len).reset_index()
  print(np.mean(e.ix[:,'Agent']))

###
'''
For the leads that signed up, how many calls were received, on average?
'''
###
def question_3():

   cl = pd.merge(c,l, on='Phone_Number', how='inner', indicator=True)
   a=cl[ cl['Call_Outcome']=='INTERESTED']
   b = pd.DataFrame(a['Phone_Number'].unique())
   b.columns = ['Phone_Number']
   d = pd.merge(cl,b, on = 'Phone_Number', how ='inner')
   e = d.groupby("Phone_Number")
   f = e['Agent'].aggregate( len).reset_index()
   print(np.mean(f.ix[:,'Agent']))

###
'''
Which agent had the most signups? Which assumptions did you make? (note that there
is a many-to-one relationship between calls and leads)
'''
###
def question_4():
  cl = pd.merge(c,l, on='Phone_Number', how='inner', indicator=True)
  a=cl[cl['Call_Outcome'] == 'INTERESTED' ]
  b=pd.DataFrame(a['Phone_Number'].unique())
  b.columns=['Phone_Number']
  cl[ cl['Phone_Number']==992847426160]


cl = pd.merge(c,l, on='Phone_Number', how='inner', indicator=True)
cl=cl.drop('_merge',axis=1)
'''
###interested
intrested=cl[ cl['Call_Outcome']=='INTERESTED']
intrested_p = pd.DataFrame(intrested['Phone_Number'].unique())
intrested_p.columns = ['Phone_Number']
intrested_join = pd.merge(cl,intrested_p, on = 'Phone_Number', how ='inner')
intrested_join = intrested_join[ intrested_join['Call_Outcome']=='INTERESTED' ]
#intrested_join = intrested_join.drop('_merge',axis=1)
###not intrestedested
not_intrested = cl[ cl['Call_Outcome']!='INTERESTED']
not_intrested_p = pd.DataFrame(not_intrested['Phone_Number'].unique())
not_intrested_p.columns = ['Phone_Number']
not_intrested_join = pd.merge(cl, not_intrested_p, on='Phone_Number', how='inner', indicator=True)
''' 
cl['int']=0
cl['not_int']=0
for i in xrange(len(cl)):
   if cl.ix[i,'Call_Outcome']=='INTERESTED':
      cl.ix[i,'int']=1
   else:
       cl.ix[i,'not_int']=1
gr = cl.groupby("Phone_Number")
res = pd.DataFrame(gr.aggregate( np.sum ))

interested = cl[ (cl['int']==1) & (cl['not_int']==0)].reset_index()
not_interested = cl[ (cl['int']==0) & (cl['not_int']==1)].reset_index()



def fix_agents( df ):

  df['green']=0
  df['orange']=0
  df['black']=0
  df['blue']=0
  df['red']=0

  df['agriculture'] = 0
  df['construction'] = 0
  df['consultancy'] = 0
  df['entertainment'] = 0
  df['food'] = 0
  df['retail'] = 0
  df['wholesale'] = 0

  df['north-west'] = 0
  df['south-west'] = 0
  df['scotland'] = 0
  df['south-east'] = 0
  df['north-east'] = 0
  df['wales'] = 0
  df['midlands'] = 0
  df['london'] = 0
  df['northern-ireland'] = 0
  df['south'] = 0

  #print(df.head())
  #print(len(df))

  for i in xrange(len(df)):
     ##########
     ###pdb.set_trace()
     #########
     if df.ix[i,'Region'] =='north-west':
        df.ix[i,'north-west']=1
     elif df.ix[i,'Region'] =='south-west':
        df.ix[i,'south-west']= 1
     elif df.ix[i,'Region'] =='scotland':
        df.ix[i,'scotland']= 1
     elif df.ix[i,'Region'] =='south-east':
        df.ix[i,'south-east']= 1
     elif df.ix[i,'Region'] =='north-east':
        df.ix[i,'north-east']= 1
     elif df.ix[i,'Region'] =='wales':
        df.ix[i,'wales']= 1
     elif df.ix[i,'Region'] =='midlands':
        df.ix[i,'midlands']= 1
     elif df.ix[i,'Region'] =='london':
        df.ix[i,'london']= 1
     elif df.ix[i,'Region'] =='northern-ireland':
        df.ix[i,'northern-ireland']= 1
     elif df.ix[i,'Region'] =='south':
        df.ix[i,'south']= 1

     if df.ix[i,'Agent'] =='green':
        df.ix[i,'green']= 1
     elif df.ix[i,'Agent'] =='orange':
        df.ix[i,'orange']= 1
     elif df.ix[i,'Agent'] =='black':
        df.ix[i,'black']= 1
     elif df.ix[i,'Agent'] =='blue':
        df.ix[i,'blue']= 1
     elif df.ix[i,'Agent'] =='red':
        df.ix[i,'red']= 1

     if df.ix[i,'Sector'] =='food':
        df.ix[i,'food']= 1
     elif df.ix[i,'Sector'] =='entertainment':
        df.ix[i,'entertainment']= 1
     elif df.ix[i,'Sector'] =='retail':
        df.ix[i,'retail']= 1
     elif df.ix[i,'Sector'] =='wholesale':
        df.ix[i,'wholesale']= 1
     elif df.ix[i,'Sector'] =='construction':
        df.ix[i,'construction']= 1
     elif df.ix[i,'Sector'] =='agriculture':
        df.ix[i,'agriculture']= 1
  
  return df


int_unq=pd.DataFrame(interested[ ['Region','Sector','Age','Agent','int']])
#.drop_duplicates()
not_int_unq=pd.DataFrame(not_interested[ ['Region','Sector','Age','Agent','int']])

int_unq = fix_agents ( int_unq )
not_int_unq = fix_agents ( not_int_unq )

int_unq = int_unq.drop_duplicates()
not_int_unq = not_int_unq.drop_duplicates()
int_unq = int_unq.reset_index()
not_int_unq = not_int_unq.reset_index()
tr = pd.concat([int_unq, not_int_unq.ix[0:len(int_unq),:]])
tr = tr.reset_index()


t_cols = ['int','Age','blue','green', 'orange', 'red'  # 'black'
          , 'agriculture', 'construction','wholesale', 'entertainment', 'food', 'retail'#,  'consultancy'
          , 'north-west', 'south-west', 'scotland', 'south-east', 'north-east','south', 'midlands', 'london', 'northern-ireland'   #, 'wales'
         ]

tt_cols=['int', 'london', 'red', 'south', 'blue']


def run_logit(cols):

  #logit = sm.Logit(tr['int'], sm.add_constant(tr.ix[:, ['Age', 'orange','black','blue','red'] ]) )
  ttt = tr.ix[:,t_cols]
  for i in xrange( len(ttt)-1,-1,-1 ):
     if ( ttt.ix[i,'int'] ==0 and np.sum(ttt.ix[i, t_cols]) == 0 ) or ( ttt.ix[i,'int'] ==1 and np.sum(ttt.ix[i, t_cols]) == 1 ):
        ttt = ttt.drop(i)
  ttt = ttt.reset_index()
  ttt=ttt.drop('index', axis=1)


  logit = sm.Logit(tr['int'], sm.add_constant(tr.ix[:, cols[1:] ]) )
  res= logit.fit()
  print(res.summary())
  #ctab  = pd.crosstab(c['hon'], c['female'])
  #logit = sm.Logit(c['hon'], c.ix[:, ['female']])
  print('Parameter:', res.params, '\nExponential of the parameter: ',np.exp(res.params))
  return ttt
#  print( pd.crosstab(tr['int'], tr['red']) )
#  print( 'The ratio of interested to not interested is (764/1759) = ', (764.0/1759), ', same as the exponent of the intercept.' )
#  print(' The ratio of odds [ (372.0 / 693) / (764.0/1759) ] = ', (372.0 / 693) / (764.0/1759) , ' , same as the exponent of the red intercept.')
  '''  
  #logit = sm.Logit(tr['int'], sm.add_constant(tr.ix[:, ['green', 'orange','black','blue','red'] ]) )
  logit = sm.Logit(tr['int'], sm.add_constant(tr.ix[:, ['Agent'] ]) )
  logit = sm.Logit(tr['int'], sm.add_constant(tr.ix[:, ['Agent'] ]) )
  res= logit.fit()
  print(res.summary())
  #ctab  = pd.crosstab(c['hon'], c['female'])
  #logit = sm.Logit(c['hon'], c.ix[:, ['female']])
  print('Parameter:', res.params, '\nExponential of the parameter: ',np.exp(res.params))
  print( pd.crosstab(tr['int'], tr['red']) )
  '''
