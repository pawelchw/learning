###
'''
This code shows the application of log transformation of the response variable.
'''
###
from required_imports import essentials as es

#read the file
df = es.pd.read_csv("/home/pawel-dell/learning/datasets/regression/gelman_reg/earnings/df.csv")

#clean the data frame
# by that we mean:
# (1) remove nulls
# (2) remove earning equals or less then zero - both will geerate issues on for the log function
df_clr=df[ (~df['earn'].isnull()) & (df['earn'] >0)]
df_clr = df_clr.reset_index()
df_clr['earn_l'] = es.np.log(df_clr['earn']  )


# pick the predictors and outcome variables
p=['height']
o=['earn_l']

#run the model
tt, m = es.run_reg(df_clr,o,p,'ols','y')



print("\n\nCould we attribute the 6% difference to different earning distributions between genders?\n\n")


df_clr['gender'] = df_clr['sex'] - 1

# pick the predictors and outcome variables
b1=['height']
b2 = ['gender']
o = ['earn_l']


#run the model
tt, m = es.run_reg(df_clr,o,b1+b2,'ols','y')


df_clr['height_male'] = df_clr['gender'] * df_clr['height']

# pick the predictors and outcome variables
b1=['height']
b2 = ['gender']
b3 = ['height_male']
o = ['earn_l']


#run the model
tt, m = es.run_reg(df_clr,o,b1+b2+b3,'ols','y')
