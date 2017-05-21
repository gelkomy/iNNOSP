# -*- coding: utf-8 -*-
"""
Created on Sun May 21 11:17:31 2017

@author: Gamal
"""
from preprocessing import preprocessing
from feature_extraction import feature_extraction
from calculate_R import calculate_R
folder_dir=r'E:\Faculty of Engineering\InnoTech\Epilipsy\Data\Patient 14 csv - Copy'
data=preprocessing(folder_dir)
data=feature_extraction(data)
r=calculate_R(data)
del data
