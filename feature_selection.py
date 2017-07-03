# -*- coding: utf-8 -*-
"""
Created on Mon 3 Jul 2017
This file performs feature selection
1- calculates R
2- feature basis selection

and returns the selected features

@author: Gamal
"""
from calculate_R import calculate_R
from feature_basis_selection import feature_basis_selection



def feature_selection(data, y):

    r=calculate_R(data)

    all_electrodes = feature_basis_selection(data,y, r)

    return all_electrodes
