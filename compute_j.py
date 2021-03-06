'''
this file computes the j for a given s_b and s_w

% /**************************************************************************** 
%  * Job:             compute J                    * 
%  *                                                                          * 
%  *Inputs: scatter = {'s_b': s_b, 's_w':s_w}
                S_b: BETWEEN  CLASS SCATTER MATRIX
%               S_w: WITHIN CLASS SCATTER MATRIX
    Outputs:    J
%  *                                                                          * 
%  * Generated on:    Sun, May 21, 2017                                       * 
%  * Generated by:    Hassan Eldeeb                                                    * 
%  * Version:         1                                                       * 
%  ****************************************************************************/ 
'''

from scatter_matrix import scatter_matrix
import numpy as np
from preprocessing import preprocessing
from feature_extraction import feature_extraction

# preprocessed_data = preprocessing(r".\data")
# features = feature_extraction(preprocessed_data)
#
# data = features['C3-P3']
# y = np.random.randint(0, 4, data.shape[0])
def compute_j(data, y):
    scatter = scatter_matrix(data, y)
    try:
        a = np.linalg.det(scatter['s_w'] + scatter['s_b'])
        b = np.linalg.det(scatter['s_w'])
        #print a,b
        J = a/b
    except ZeroDivisionError:
        J = 0
    if np.math.isnan(J) or np.math.isinf(J):
        J = 0
    return J
