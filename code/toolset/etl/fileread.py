import pandas as pd

def space_read(loc):

   f = open(loc,"r")
   lines = f.read().split("\n")
   cols = ['switch','arsenic','dist','assoc','educ']
   df = pd.DataFrame(columns = cols)
   counter = 0
   for line in lines:

      if len(line) > 0:
         if counter <> 0:
           vals = line.split()
           df.loc[counter-1]=[ float(v) for v in vals[1:]]
         
         counter +=1
   return df
