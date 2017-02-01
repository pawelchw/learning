from __future__ import print_function
from prep import clean as cln
from model import validate  as va
from model import correlation_analysis as ca
from model import feature_importance as fi
from plot import scat_mat_cor as smc
from plot import outlier_analisys as poa
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
#pth_kagle_db
exec(open('./reqs/filepaths.py').read())

df = pd.read_csv(pth_kagle_db +'house_price/train.csv')
df_cln = cln.clean_nans(df)
df_names,df_cln = cln.replace_with_avg(df_cln)
print(df_cln.isnull().sum().tolist())
corrmat = smc.net_plot(df_cln)
#optionally here
#plt.show()
ex_col,ex_col_sng,col_sum = ca.corr_greater_than(corrmat,df_cln)
outlier_names = cln.outlier_stats(df_cln)
poa.outlier_histogram(df_cln, outlier_names,2,2)
print( ex_col.sort(['co1_unq_values','col2_unq_values'], ascending = [False,False]) )
