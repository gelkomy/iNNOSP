# -*- coding: utf-8 -*-
"""
Created on Mon May 22 14:38:01 2017

@author: Yousef Essam
"""

from preprocessing import preprocessing
import matplotlib.pyplot as plt
from pykalman import KalmanFilter
from kalman_filter import kalman_filter
import pandas as pd
folder_dir=r'E:\Inno Tech\Patient14_2'
data1=preprocessing(folder_dir)
data = pd.DataFrame(data1.ix[1:10000,1]);
#res = kalman_filter(data);

result=pd.DataFrame() # will hold the results
for col in data.columns:
    
#   creating kalman filter object
    kf = KalmanFilter(transition_matrices = [1],
                      observation_matrices = [1],
                      initial_state_mean = 0,
                      initial_state_covariance = 1,
                      observation_covariance=6,  # fixes the error
                      transition_covariance=.01)
    
#   Auto compute kalman filter parameters ,yousef #learn kalman filter parameters
    kf = kf.em(data.loc[:,col], n_iter=5)
            
    # Use the observed values of the price to get a rolling mean
    # perform smoothing
    state_means, _ = kf.smooth(data.loc[:,col])
    # convert to pandas series
    state_means = pd.Series(state_means.flatten(), index=data.loc[:,col].index)
    
    # Plot original data and estimated mean
    plt.plot(data)
    plt.plot(state_means)
    plt.title('Kalman filter estimate of average')
    plt.legend(['Kalman Estimate','Kalman Estimate Emulate', 'X'])

    #concat the result with the output data frame
    result=pd.concat([result, state_means ] ,axis=1)                  
