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

Compas Data 
#let's make everything uppercase 
Compass['FirstName'] = Compass['FirstName'].str.upper()
Compass['LastName'] = Compass['LastName'].str.upper()
Compass['Birthday'] = pd.to_datetime(Compass['Birthday'],infer_datetime_format=True,errors='coerce') #make sure everything has the same data format 

More info Risk of Violence Data 
#let's make everything uppercase 
SubsetViol['FirstName'] = SubsetViol['FirstName'].str.upper()
SubsetViol['LastName'] = SubsetViol['LastName'].str.upper()

SubsetViol['Birthday'] = pd.to_datetime(SubsetViol['Birthday'],infer_datetime_format=True,errors='coerce')

#Merge the data by 
Data = pd.merge(Compass, SubsetViol, how='left', on=['FirstName', 'LastName','Birthday'])
Data= pd.read_csv("C:/Users/17324/OneDrive/Documents/PythonScripts/RacialBias/CombinedData.csv",encoding= 'unicode_escape')

#export_csv = Data.to_csv (r'C:/Users/17324/OneDrive/Documents/PythonScripts/RacialBias/CombinedData.csv', index = None, header=True)


