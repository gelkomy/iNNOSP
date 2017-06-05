
import pickle
data=pickle.load(open(r'E:\Faculty of Engineering\InnoTech\Epilipsy\Data\pkl patient 14\file6_only.pkl','r'))

from kalman_filter import kalman_filter
print "*** kalman filter processing ***"
for electrode in data:
    print "##### the current electrode is ", electrode
    temp= kalman_filter(data[electrode])
    data[electrode]=temp

pickle.dump(data,open(r'E:\Faculty of Engineering\InnoTech\Epilipsy\Data\pkl patient 14\file6_kalman.pkl','w'))

# test={'1':'adfadsf', '2': 'asdfadsf'}
#
# for i in test:
#     print test[i]

