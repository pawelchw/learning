from __future__ import print_function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# columns - 100-130, 130-160, 160-190,190-220, 220-250
# rows
# 5 - 5.4
# 5.4 - 5.8
# 5.8 - 6
# 6 - 6.4
# 6.4 - 6.8
data = np.array( [
                 [ 0.06,   0.04,    0.02,      0,   0]
               , [ 0.06,   0.12,    0.06,   0.02,   0]
               , [ 0,      0.06,    0.14,   0.06,   0]
               , [ 0,      0.02,    0.06,   0.10, 0.04]
               , [ 0,      0,       0,      0.08, 0.04]
                 ]
               )

#weight in 130-160

print("weight in 130-160:", np.sum(data[:,1]) )

#weight in 130-160, given a studen is less than 6'
# col_value_1 + col value_2 + col value_3
# ----------------------------------------
# entire row_1 + entire row_2 + entire row_3

print("weight in 130-160, given a studen is less than 6':"
     , np.sum(data[0,1]+ data[1,1]+ data[2,1]) 
     / ( np.sum(data[0,:]) + np.sum(data[1,:]) +np.sum(data[2,:]) )
     #+ np.sum(data[1,1]/np.sum(data[1,:]))
     #+ np.sum(data[2,1]/np.sum(data[1,:]))
     )# + np.sum(data[1:,1:1]/data) + np.sum(data[2:,2:2]/data))



#weight in 130-160, given a studen is greater than 6'
# col_value_1 + col value_2 + col value_3
# ----------------------------------------
# entire row_1 + entire row_2 + entire row_3

print("weight in 130-160, given a studen is greater than 6':"
     , np.sum( data[3,1]+ data[4,1]) 
     / (  np.sum(data[3,:]) +np.sum(data[4,:]) )
     #+ np.sum(data[1,1]/np.sum(data[1,:]))
     #+ np.sum(data[2,1]/np.sum(data[1,:]))
     )# + np.sum(data[1:,1:1]/data) + np.sum(data[2:,2:2]/data))

