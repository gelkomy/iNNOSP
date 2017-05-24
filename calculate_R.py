'''
% This function calculate R linearly independent features
% that achieve the maximum linear separability criteria for each electrode,
% where R is determined by eigenvalue analysis.
%
% The input  is a dictionary of  dataframes indexed by electrode name
% with all the features.
%
% The output is a dictionary that has a value R indexed by electrode name.
 
% /**************************************************************************** 
%  * Job:             calculate_R                   * 
%  *                                                                          * 
%  * Generated on:    Mon, May 15, 2017                                       * 
%  * Generated by:    Emad                                                    * 
%  * Version:         1                                                       * 
%  ****************************************************************************/ 
'''

def calculate_R(input_data):

    import numpy as np
    import pandas as pd
    import math

##    for testing purpose
##    df1 = pd.DataFrame(np.random.randint(0,100,size=(100, 44)))
##    df2 = pd.DataFrame(np.random.randint(0,100,size=(100, 44)))
##    df3 = pd.DataFrame(np.random.randint(0,100,size=(100, 44)))
##    input_data = {'e1':df1 , 'e2':df2 , 'e3':df3}


    R_total={}

    for electrode in input_data:
        max_diff = -float("inf")

        input_features = input_data[electrode]  #input frame of each electrode
        
        cov_matrix = input_features.cov()  #covariance of input_features --> gives dataframe 
        
        n_cov_matrix = cov_matrix.apply(pd.to_numeric, errors='coerce').fillna(0)  #convert cov matrix to numeric data instead of object 
        # errors='coerce' --> error message in case of errors
        # fillna --> in case of NaN --> replace with 0
        
        eig_vals, eig_vecs = np.linalg.eig(n_cov_matrix)
        eig_vals = pd.DataFrame(eig_vals)  # the eigenvalues
        #eig_vecs = pd.DataFrame(eig_vecs)  # normalized eigenvectors

        abs_eig_vals = eig_vals.abs()  #Calculate abs(eig)

        abs_eig_vals = 10 * np.log10(abs_eig_vals)  # 10*log10(abs)

        abs_eig_vals.sort_index()  #Sorts descending by default
        for i in range(abs_eig_vals.size-1):
            diff = abs_eig_vals.loc[i,0] - abs_eig_vals.loc[i+1,0]

            if max_diff < diff:
                max_diff = diff
                max_diff_index = i

        R = max_diff_index

        R_total[electrode] = R
        
    return R_total

