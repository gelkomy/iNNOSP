# -*- coding: utf-8 -*-
"""
Created on Mon May 22 14:38:01 2017

@author: Yousef Essam
"""

from preprocessing import preprocessing

from kalman_filter import kalman_filter
import pandas as pd
folder_dir=r'E:\Inno Tech\Patient14_2'
data=preprocessing(folder_dir)
#dataX = pd.DataFrame(data.ix[1:100,1]);
#res = kalman_filter(dataX);

