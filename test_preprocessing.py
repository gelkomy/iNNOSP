from preprocessing import preprocessing
from calculate_R import calculate_R
# x = preprocessing(r'E:\Faculty of Engineering\InnoTech\Epilipsy\Data\Patient 14 csv - Copy')


import pickle


x=pickle.load(open(r'C:\Users\Hassan\Documents\Innotech\Epilepsy Python\iNNOSP\data\all_files_hp.pkl','rb'))


r = calculate_R(x)
from PrepareYVector import getY
from PrepareWindowsVector import getWindows
from feature_basis_selection import feature_basis_selection
from electrode_selection import electrode_selction

text_file=r'C:\Users\Hassan\Documents\Innotech\Epilepsy Python\iNNOSP\data\patient14\chb14-summary.txt'
yTimeLine = getY(text_file, 1, 42)

y = getWindows(yTimeLine)

result=feature_basis_selection(x,y,r)
sel_elec = electrode_selction(result, y)

print r
