'''
this file performs the data preparation phase which contains preprossing,
kalman filter, and computing y.

% /**************************************************************************** 
%  * Job:             Data Preparation phase                    * 
%  *                                                                          * 
%  *Inputs: patien_number, is_kalman (True if we want to apply kalman filter
    and False otherwise
    Outputs: prepared_data {'y':y_windowed, 'features': features}
                y_windowed (DataFrame) is classes lables for each window
                features (Dictionary) is features data for each electrode 
%  *                                                                          * 
%  * Generated on:    Sun, May 21, 2017                                       * 
%  * Generated by:    Hassan Eldeeb                                                    * 
%  * Version:         1                                                       * 
%  ****************************************************************************/ 
'''

from preprocessing import preprocessing
from feature_extraction import feature_extraction
from kalman_filter import kalman_filter
from PrepareYVector import getY
from PrepareWindowsVector import getWindows
import pandas as pd

def feature_preparation(patient_no, is_kalman = True):
    '''
    patient data should be located at 'data' folder withen the same folder
    containing this file. Data files for each patient is combined in a folder
    named 'patientX' where X is the patient number.
    '''
    #is_kalman = False
    #patient_no = 14
    if patient_no < 10:
        patient_no = str('0'+str(patient_no))
    path = r".\data\patient" + str(patient_no)
    preprocessed_data = preprocessing(path)
    features = feature_extraction(preprocessed_data)
    feature_kalman = {}
    if is_kalman:
        for electrode in features:
            feature_kalman[electrode] = kalman_filter(features[electrode])
    else:
        feature_kalman = features
    summary_file = path + '\chb' + str(patient_no) + '-summary.txt'
    y_ms = getY(summary_file)
    y_windowed = getWindows(y_ms)
    y_windowed = pd.DataFrame(y_windowed, columns=['y'])
    y_windowed = y_windowed.iloc[0:feature_kalman[list(feature_kalman.keys())[0]].shape[0]]
    # for electrode in feature_kalman:
    #     pd.concat([feature_kalman[electrode], y_windowed], axis=1)
    prepared_data = {'y': y_windowed, 'features': feature_kalman}
    return prepared_data
