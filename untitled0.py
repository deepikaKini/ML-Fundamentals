#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 18:22:54 2020

@author: deepika
"""


#how to create dataframes AND CHECK IF IT IS EMPTY
import pandas as pd


# Create an empty Dataframe
dfObj = pd.DataFrame(columns=['Date', 'UserName', 'Action'])
# Check if Dataframe is empty using empty attribute
if dfObj.empty == True:
    print('DataFrame is empty(using empty')
else:
    print('DataFrame is not empty(using empty')
    
    #-------
import numpy as np    

    # List of Tuples
students = [(np.NaN, np.NaN, np.NaN),
            (np.NaN, np.NaN, np.NaN),
            (np.NaN, np.NaN, np.NaN)
           ]
# Create a DataFrame object
studentsDfObj = pd.DataFrame(students, columns=['Name', 'Age', 'City'])
# Check if Dataframe is empty using empty attribute
if studentsDfObj.empty == True:
    print('Student DataFrame is empty(using empty)')
else:
    print('Student DataFrame is not empty(using empty)')
    
    #---------
    
    # Create an empty Dataframe
dfObj = pd.DataFrame(columns=['Date', 'UserName', 'Action'])
# Check if Dataframe is empty using dataframe's shape attribute
if dfObj.shape[0] == 0:
    print('DataFrame is empty(using shape)')
else:
    print('DataFrame is not empty(using shape)')
    
    #---------
    
    # Create an empty Dataframe
dfObj = pd.DataFrame(columns=['Date', 'UserName', 'Action'])
# check if length of index is 0 to verify if dataframe is empty
if len(dfObj.index.values) == 0:
    print('DataFrame is empty(using index)')
else:
    print('DataFrame is not empty(using index)')
    
    
    
     #---------
    
    # check if length of dataframe is 0 by calling len on Dataframe
if len(dfObj) == 0:
    print('DataFrame is empty(using len())')
else:
    print('DataFrame is not empty(using len()')