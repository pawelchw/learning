execfile('/home/pawel-dell/learning/code/init_files/regression_analysis.py')
execfile('/home/pawel-dell/learning/code/init_files/random_classification_sets.py')
execfile('col_names.py')
df = pd.read_csv('/home/pawel-dell/learning/datasets/regression/Communities_and_Crime_Unnormalized/data.csv')
df.columns = col_names


x_pd = pd.DataFrame(df.ix[:,4:30])
x_pd['target'] = pd.DataFrame(df['murders'])
x = x_pd.ix[:,:-1]
y = x_pd['target']
xi = c_inter.fit_transform(x)
main_effects = c_inter.n_input_features_
variables = x.columns
def r2_est(x,y):
   return r2_score(y, lin_reg.fit(x,y).predict(x))

x_tr, x_te, y_tr, y_te = train_test_split(x,y.astype(float), test_size = 0.33, random_state=432)

y_res=lin_reg.fit(x_tr,y_tr).predict(x_te).astype(int)

base = r2_est(x_tr, y_tr)

for k, effect in enumerate(c_inter.powers_[(main_effects):]):
    terma, termb = variables[effect==1]
    incr = r2_est(xi[:, list(range(0,main_effects))+[main_effects+k]],y) - base
    if incr > 0.01:
        print('adding interactions:', terma,' ', termb,' ',incr)

