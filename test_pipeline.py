# -*- coding: utf-8 -*-
"""
Created on Sun May 21 11:17:31 2017

@author: Gamal
"""
from preprocessing import preprocessing
from feature_extraction import feature_extraction
from calculate_R import calculate_R
from compute_j import compute_j
import pandas as pd
folder_dir=r'E:\Faculty of Engineering\InnoTech\Epilipsy\Data\Patient 14 csv - Copy'
data=preprocessing(folder_dir)
data=feature_extraction(data)
r=calculate_R(data)

electrode_data= data['FP1-F7']


from PrepareYVector import getY
from PrepareWindowsVector import getWindows

#text_file=r'C:\Users\Yousef Essam\Desktop\Task1-ReadY\Patient14\test.txt'
text_file=r'E:\Faculty of Engineering\InnoTech\Epilipsy\Data\Patient14\chb14-summary.txt'
yTimeLine = getY(text_file)

windows = getWindows(yTimeLine)
windows=pd.DataFrame(windows)
x=electrode_data.shape[0]
windows=windows.ix[0:x,]

j=compute_j(electrode_data, windows[0])


