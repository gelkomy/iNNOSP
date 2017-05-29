from preprocessing import preprocessing
from calculate_R import calculate_R
x = preprocessing(r'D:\College\Inno\InnoBCI\data\Patient 14 csv')



r = calculate_R(x)

print r