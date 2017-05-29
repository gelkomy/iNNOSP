#import cPickle as pickle
from calculate_R import calculate_R
import pandas as pd

#data = pickle.load( open( "../preprocessed.pkl", "rb" ) )

data={}
d = pd.read_csv('C:\Users\Emad\Desktop\inF.csv')

data['a'] = d

R=calculate_R(data)

print R

