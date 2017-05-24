# -*- coding: utf-8 -*-
"""
Created on Mon May 22 14:38:01 2017

@author: Yousef Essam
"""

from preprocessing import preprocessing
from feature_extraction import feature_extraction
from calculate_R import calculate_R
from compute_j import compute_j
from kalman_filter import kalman_filter
import pandas as pd
folder_dir=r'E:\Inno Tech\Patient 14 csv'
data=preprocessing(folder_dir)
dataX = pd.DataFrame(data.ix[1:1000000,1]);
res = kalman_filter(dataX);

