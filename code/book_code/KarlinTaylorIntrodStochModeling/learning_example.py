import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pymc

x_inp = np.random.normal(5,2,1000)
y_inp = np.random.uniform(20,30,1000)
plt.scatter(x_inp, y_inp)
