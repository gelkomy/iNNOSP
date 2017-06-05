
# import pickle
# data=pickle.load(open(r'E:\Faculty of Engineering\InnoTech\Epilipsy\Data\pkl patient 14\file6_only.pkl','r'))
#
# from kalman_filter import kalman_filter
# print "*** kalman filter processing ***"
# for electrode in data:
#     print "##### the current electrode is ", electrode
#     temp= kalman_filter(data[electrode])
#     data[electrode]=temp
#
# pickle.dump(data,open(r'E:\Faculty of Engineering\InnoTech\Epilipsy\Data\pkl patient 14\file6_kalman.pkl','w'))

# test={'1':'adfadsf', '2': 'asdfadsf'}
#
# for i in test:
#     print test[i]




from calculate_R import calculate_R
# x = preprocessing(r'E:\Faculty of Engineering\InnoTech\Epilipsy\Data\Patient 14 csv - Copy')


import pickle
x=pickle.load(open(r'E:\Faculty of Engineering\InnoTech\Epilipsy\Data\pkl patient 14\file6_kalman.pkl','r'))


r = calculate_R(x)
from PrepareYVector import getY
from PrepareWindowsVector import getWindows
from feature_basis_selection import feature_basis_selection
from electrode_selection import electrode_selction

text_file=r'E:\Faculty of Engineering\InnoTech\Epilipsy\Data\Patient14\chb14-summary.txt'
yTimeLine = getY(text_file,6 ,6 )
#
y = getWindows(yTimeLine)
#
#
result=feature_basis_selection(x,y,r)
sel_elec = electrode_selction(result, y)
