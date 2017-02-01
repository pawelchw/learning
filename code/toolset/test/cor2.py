import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sn
df = pd.DataFrame(np.random.randn(10,4), columns=['a','b','c','d'])
pd.tools.plotting.scatter_matrix(df, alpha=0.2, diagonal='kde')
