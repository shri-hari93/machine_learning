#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#Data Processing

#Import Libararies
import numpy as np #mathematical tools
import matplotlib.pyplot as plt #for ploting charts
import pandas as pd #import data sets and manage data sets

dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values #: - takes all the values in row and :- take all the column except the last one
Y = dataset.iloc[:, 3].values
                
#Taking care of missing data
from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values= "NaN", strategy= "mean", axis=0) #strategy default value is mean, axis = 1 => row, axis = 0 => column
imputer = imputer.fit(X[:,1:3]) #The upper bound 3 is excluded
X[:,1:3] = imputer.transform(X[:,1:3])