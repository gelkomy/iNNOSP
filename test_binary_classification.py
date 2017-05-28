# -*- coding: utf-8 -*-
"""
Created on Sun May 28 10:43:39 2017

@author: Gamal
"""
import pandas as pd
from binary_classification import binary_classification
data=pd.read_csv(r'E:\Faculty of Engineering\InnoTech\Epilipsy\latest_data.csv', header=None)
X=data[[0,1,2,3,4,5,6,7,8]]
y=data[[9]]
binary_classification(X,y)