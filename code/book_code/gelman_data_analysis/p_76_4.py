from required_imports import essentials as es

#read the file
df = es.pd.read_csv("/home/pch/learning/datasets/regression/gelman_reg/earnings/df.csv")
#clean the data frame
# by that we mean:
# (1) remove nulls
# (2) remove earning equals or less then zero - both will geerate issues on for the log function
dfc=df[ (~df['earn'].isnull()) & (df['earn'] >0)]
dfc= dfc.reset_index()

