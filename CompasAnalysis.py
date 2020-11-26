# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 20:11:42 2020

@author: 17324
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 14:24:25 2020

@author: 17324
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 22:16:18 2020

@author: 17324
"""


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import random as r
import seaborn as sb
import datetime as dt 

Compass= pd.read_csv("C:/Users/17324/OneDrive/Documents/PythonScripts/RacialBias/CompasData.csv",encoding= 'unicode_escape')

#consistent labeling 
Compass['Ethnicity'] = Compass['Ethnicity'].replace('African-Am','African-American')

#not looking at ambigious Ethnicities or those with lower populaiton in the dataset 
Compass=Compass[(Compass['Ethnicity'] != 'Other') & (Compass['Ethnicity'] != "Oriental") & (Compass['Ethnicity'] != 'Arabic') &(Compass['Ethnicity'] != 'Asian') & (Compass['Ethnicity'] != 'Native American')]

#So I can calculate age 
Compass['Birthday'] = pd.to_datetime(Compass['Birthday'])

today = dt.date.today()
Compass['Age'] = today.year - Compass['Birthday'].dt.year

#Making Risk a binary variable where  High is 1, low, medium, and medium with override is 0. 
Compass['HighRisk'] = Compass['RecSupervisionLevelText'].replace({'Medium with Override Consideration':0,'Medium':0,'Low':0,'High':1})

RiskV= Compass[(Compass["DisplayText"] =='Risk of Violence')]

Compass= Compass[Compass['Age'] > 17]

group_names = ['18-25', '26-50', '51-100']
Compass['Age_group'] = pd.qcut(Compass['Age'], q = 3,labels = group_names)
# Print Age_group column
Compass[['Age_group', 'Age']]

sb.catplot(x="Age_group",y='HighRisk', kind="bar", data=RiskV)

