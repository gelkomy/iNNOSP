# -*- coding: utf-8 -*-
"""
Created on Sun May 21 11:17:31 2017

@author: Gamal
"""
from PrepareYVector import getY
from PrepareWindowsVector import getWindows
from feature_selection import feature_selection
from electrode_selection import electrode_selction
from binary_classification import binary_classification
import pandas as pd
import cPickle as pickle


folder_dir=r'D:\College\Inno\InnoBCI\data\Patient 14 csv'
#data=preprocessing(folder_dir)

data=pickle.load(open(r'D:\College\Inno\Python code\all_files_hp.pkl','rb'))

#electrode_data= data['FP1-F7']

#text_file=r'C:\Users\Yousef Essam\Desktop\Task1-ReadY\Patient14\test.txt'
summary_file=r'D:\College\Inno\InnoBCI\data\Patient 14 csv\chb14-summary.txt'
yTimeLine = getY(summary_file,1,42)

y = getWindows(yTimeLine)

y=pd.DataFrame(y)

data = feature_selection(data,y)

selected_electrodes = electrode_selction(data, y)

if len(selected_electrodes)>1:
    data = pd.concat([data[selected_electrodes[0]],data[selected_electrodes[1]]], axis=1)
else:
    data = data[selected_electrodes]
binary_classification(data, y)



