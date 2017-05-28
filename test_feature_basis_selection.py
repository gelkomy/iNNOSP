# -*- coding: utf-8 -*-
"""
Created on Mon May 22 14:29:56 2017

@author: Gamal
"""

import pandas as pd
import pickle
from preprocessing import preprocessing
from feature_extraction import feature_extraction
from calculate_R import calculate_R
from compute_j import compute_j

from feature_basis_selection import feature_basis_selection
from PrepareYVector import getY
from PrepareWindowsVector import getWindows

#with open(r'E:\Faculty of Engineering\InnoTech\Python Release\data.pkl', 'rb') as input:
#    data=pickle.load(input)
#
#with open(r'E:\Faculty of Engineering\InnoTech\Python Release\r.pkl', 'rb') as input:
#    R=pickle.load(input)    
#y=pd.read_csv(r'E:\Faculty of Engineering\InnoTech\Python Release\y.csv')
#y=y.ix[0:3600,1]

folder_dir=r'E:\Faculty of Engineering\InnoTech\Epilipsy\Data\Patient 14 csv - Copy'
data=preprocessing(folder_dir)
#data=feature_extraction(data)
R=calculate_R(data)

#electrode_data= data['FP1-F7']
#
#
#
#
##text_file=r'C:\Users\Yousef Essam\Desktop\Task1-ReadY\Patient14\test.txt'
#text_file=r'E:\Faculty of Engineering\InnoTech\Epilipsy\Data\Patient14\chb14-summary.txt'
#yTimeLine = getY(text_file,6 ,7 )
#
#y = getWindows(yTimeLine)
#
#
#result=feature_basis_selection(data,y,R)
