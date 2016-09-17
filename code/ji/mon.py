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

p = pd.read_csv("/home/pawel-dell/learning/cv_pack/apes_master/promo_lookup.csv")
t = pd.read_csv("/home/pawel-dell/learning/cv_pack/apes_master/txn_data.csv")
u = pd.read_csv("/home/pawel-dell/learning/cv_pack/apes_master/user_data.csv")
d = pd.read_csv("/home/pawel-dell/learning/cv_pack/apes_master/user_day_data.csv")
