from preprocessing import preprocessing
from calculate_R import calculate_R
# x = preprocessing(r'E:\Faculty of Engineering\InnoTech\Epilipsy\Data\Patient 14 csv - Copy')


import pickle
x=pickle.load(open(r'E:\Faculty of Engineering\InnoTech\Epilipsy\Data\pkl patient 14\all_files.pkl','rb'))

r = calculate_R(x)
from PrepareYVector import getY
from PrepareWindowsVector import getWindows
from feature_basis_selection import feature_basis_selection

text_file=r'E:\Faculty of Engineering\InnoTech\Epilipsy\Data\Patient14\chb14-summary.txt'
yTimeLine = getY(text_file,1 ,1 )
y = getWindows(yTimeLine)
result=feature_basis_selection(x,y,r)

print r
