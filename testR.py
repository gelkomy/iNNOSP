import cPickle as pickle
from calculate_R import calculate_R


data = pickle.load( open( "../preprocessed.pkl", "rb" ) )
R=calculate_R(data)

print R

