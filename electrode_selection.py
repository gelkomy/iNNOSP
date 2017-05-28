'''
this file selects the most effective electrode/electrodes

% /**************************************************************************** 
%  * Job:             electrode selection                    * 
%  *                                                                          * 
%  *Inputs: patien_number, is_kalman (True if we want to apply kalman filter
    and False otherwise
    Outputs: prepared_data {'y':y_windowed, 'features': features}
                y_windowed (DataFrame) is classes lables for each window
                features (Dictionary) is features data for each electrode 
%  *                                                                          * 
%  * Generated on:    Mon, May 22, 2017                                       * 
%  * Generated by:    Hassan Eldeeb                                                    * 
%  * Version:         1                                                       * 
%  ****************************************************************************/ 
'''

from compute_j import compute_j
import pandas as pd
import numpy as np
# for testing purpose
# from preprocessing import preprocessing
# from feature_extraction import feature_extraction
#
# preprocessed_data = preprocessing(r".\data")
# features = feature_extraction(preprocessed_data)

def electrode_selction(features, y):
    #for testing purpose
    # df1 = pd.DataFrame(np.random.randint(0, 100, size=(100, 44)))
    # df2 = pd.DataFrame(np.random.randint(0, 100, size=(100, 44)))
    # df3 = pd.DataFrame(np.random.randint(0, 100, size=(100, 44)))
    #y = pd.DataFrame(np.random.randint(0, 4, size=(100, 1)))
    # features = {'e1': df1, 'e2': df2, 'e3': df3}

    j_singles = {}
    for electrode in features:
        # compute j foreach single electrode
        j_singles[electrode] = compute_j(features[electrode], y)
    j_pairs = np.zeros([len(features), len(features)])

    elec_key = features.keys()
    for i in range(0,len(features)):
        for j in range(i+1,len(features)):
            elec_pair = pd.concat([features[elec_key[i]], features[elec_key[j]]], axis=1)
            elec_pair.columns=list(range(0, features[elec_key[i]].shape[1]+features[elec_key[j]].shape[1]))
            j_pairs[i, j] = compute_j(elec_pair, y)
    selected_electrodes = None
    if np.max(j_singles) < np.max(np.max(j_pairs)):
        idx = np.max(j_pairs)
        selected_electrodes = [elec_key[idx[0][0]], elec_key[idx[1][0]]]
    else:
        idx = max(j_singles)
        selected_electrodes = idx
    return  selected_electrodes
