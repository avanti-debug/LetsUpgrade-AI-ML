# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 15:21:48 2020

@author: Dell
"""


import pandas as ps
import numpy as nm
import matplotlib.pyplot as plt

mydata=ps.read_csv("C:/Users/Dell/Downloads/general_data.csv")

#There is no significant diffrence between in YearsAtCompany and PercentSalaryHike

from scipy.stats import mannwhitneyu

stats,p=mannwhitneyu(mydata.YearsAtCompany,mydata.PercentSalaryHike)

print(stats, p)

# as value of p is  0.0 we can accept the null hypothesis 