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


from nltk.corpus import stopwords
#nltk.download('stopwords')
# Import the 'word_tokenize' function
from nltk.tokenize import word_tokenize
# The following is used in the tokenize function
#nltk.download('punkt')
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import random as r
import seaborn as sb
import datetime as dt 

Compass= pd.read_csv("C:/Users/17324/OneDrive/Documents/PythonScripts/RacialBias/CompasData.csv",encoding= 'unicode_escape')

#let's make everything uppercase 
Compass['FirstName'] = Compass['FirstName'].str.upper()
Compass['LastName'] = Compass['LastName'].str.upper()
Compass['Birthday'] = pd.to_datetime(Compass['Birthday'],infer_datetime_format=True,errors='coerce')

SubsetViol= pd.read_csv("C:/Users/17324/OneDrive/Documents/PythonScripts/RacialBias/Violent.csv",encoding= 'unicode_escape')

#let's make everything uppercase 
SubsetViol['FirstName'] = SubsetViol['FirstName'].str.upper()
SubsetViol['LastName'] = SubsetViol['LastName'].str.upper()

SubsetViol['Birthday'] = pd.to_datetime(SubsetViol['Birthday'],infer_datetime_format=True,errors='coerce')
#let's make everything uppercase 

Data = pd.merge(Compass, SubsetViol, how='left', on=['FirstName', 'LastName','Birthday'])
Data= pd.read_csv("C:/Users/17324/OneDrive/Documents/PythonScripts/RacialBias/CombinedData.csv",encoding= 'unicode_escape')

#export_csv = Data.to_csv (r'C:/Users/17324/OneDrive/Documents/PythonScripts/RacialBias/CombinedData.csv', index = None, header=True)


Data.dtypes

Data.info()
#Predict liklihood of taking a personal loan! 
#Cleaning 

Data['Ethnic_Code_Text'] = Data['Ethnic_Code_Text'].replace('African-Am','African-American')
Data=Data[(Data['Ethnic_Code_Text'] != 'Other') & (Data['Ethnic_Code_Text'] != "Oriental")]

RiskV= Data[(Data["DisplayText"] =='Risk of Violence')]

sb.catplot(x="RecSupervisionLevelText", kind="count",hue='Ethnic_Code_Text', data=RiskV)

sb.catplot(x="Ethnic_Code_Text" , y="DecileScore" ,kind="bar", data=Data)
