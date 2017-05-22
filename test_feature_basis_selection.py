# -*- coding: utf-8 -*-
"""
Created on Mon May 22 14:29:56 2017

@author: Gamal
"""

import pandas as pd
import pickle

from feature_basis_selection import feature_basis_selection

with open(r'E:\Faculty of Engineering\InnoTech\Python Release\data.pkl', 'rb') as input:
    data=pickle.load(input)

with open(r'E:\Faculty of Engineering\InnoTech\Python Release\r.pkl', 'rb') as input:
    R=pickle.load(input)    
y=pd.read_csv(r'E:\Faculty of Engineering\InnoTech\Python Release\y.csv')
y=y.ix[0:3600,1]

result=feature_basis_selection(data,y,R)
