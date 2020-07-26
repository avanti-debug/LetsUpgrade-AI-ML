# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as ps
import numpy as nm
import matplotlib.pyplot as plt

mydata=ps.read_csv("C:/Users/Dell/Downloads/general_data.csv")

mydata.isnull()

mydata.duplicated()
mydata.drop_duplicates()

mydata.columns

dataset = mydata[['Age',  'DistanceFromHome',
       'Education',  'MonthlyIncome',
       'NumCompaniesWorked',  'PercentSalaryHike', 'TrainingTimesLastYear',
       'YearsAtCompany', 'YearsSinceLastPromotion', 'YearsWithCurrManager']].describe()

print(dataset)

dataset= mydata[['Age',  'DistanceFromHome',
       'Education',  'MonthlyIncome',
       'NumCompaniesWorked',  'PercentSalaryHike', 'TrainingTimesLastYear',
       'YearsAtCompany', 'YearsSinceLastPromotion', 'YearsWithCurrManager']].median()


print(dataset)

dataset= mydata[['Age',  'DistanceFromHome',
       'Education',  'MonthlyIncome',
       'NumCompaniesWorked',  'PercentSalaryHike', 'TrainingTimesLastYear',
       'YearsAtCompany', 'YearsSinceLastPromotion', 'YearsWithCurrManager']].mode()

print(dataset)

dataset= mydata[['Age',  'DistanceFromHome',
       'Education',  'MonthlyIncome',
       'NumCompaniesWorked',  'PercentSalaryHike', 'TrainingTimesLastYear',
       'YearsAtCompany', 'YearsSinceLastPromotion', 'YearsWithCurrManager']].var()

print(dataset)

dataset= mydata[['Age',  'DistanceFromHome',
       'Education',  'MonthlyIncome',
       'NumCompaniesWorked',  'PercentSalaryHike', 'TrainingTimesLastYear',
       'YearsAtCompany', 'YearsSinceLastPromotion', 'YearsWithCurrManager']].skew()

print(dataset)

dataset= mydata[['Age',  'DistanceFromHome',
       'Education',  'MonthlyIncome',
       'NumCompaniesWorked',  'PercentSalaryHike', 'TrainingTimesLastYear',
       'YearsAtCompany', 'YearsSinceLastPromotion', 'YearsWithCurrManager']].kurt()

print(dataset)

boxplot1=mydata.Age
plt.boxplot(boxplot1)

boxplot1=mydata.YearsAtCompany
plt.boxplot(boxplot1)

boxplot1=mydata.YearsSinceLastPromotion
plt.boxplot(boxplot1)

boxplot1=mydata.MonthlyIncome
plt.boxplot(boxplot1)

