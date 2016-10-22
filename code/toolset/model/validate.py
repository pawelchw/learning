from sklearn.cross_validation import train_test_split as tts

def train_split(data, outcome, predictors, ratio = 0.3 ):

   x_train, x_test, l_train, l_test = tts(data[predictors], data[outcome],test_size=ratio, random_state=123)
   return x_train, x_test, l_train, l_test
