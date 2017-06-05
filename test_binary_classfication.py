import pandas as pd
import numpy as np
from binary_classification import binary_classification
data = pd.read_csv(r'.\data\data.csv', skiprows=0)
data = data.fillna(value=0)
x = data.ix[:, 0:-1]
y = data.ix[:, -1]
y = pd.factorize(y)
yy = np.array(y)
y = pd.DataFrame(yy)
binary_classification(x, y)

