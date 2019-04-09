# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 16:45:12 2019

@author: Jeffrey
"""

import pandas as pd

# Create a Dataframe from CSV
newdf = pd.read_csv('Churn_Modelling.csv')

# Drop rows with any empty cells
newdf.dropna(axis=1, how='all', thresh=None, subset=None, inplace=False)
newdf.dropna(axis=0, how='all', thresh=None, subset=None, inplace=False)
newdf.to_csv("updated.csv")