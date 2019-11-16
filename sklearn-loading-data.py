import os


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

# Loading dataset
df = pd.read_csv('c:/users/cristiann/documents/github/viz-homework/viz/data/boston/housing.data',
             sep='\s+',
              header=None)

# Setting columns to dataset
lab_CRIM = 'Per capita crime rate by town'
lab_ZN = 'Proportion of residential land zoned for lots over 25,000 sq.ft.'
lab_INDUS = 'Proportion of non-retail business acres per town'
lab_CHAS = 'Charles River dummy variable (1 if tract bounds river; 0 otherwise)'
lab_NOX = ' nitric oxides concentration (parts per 10 million)'
lab_RM = 'Average number of rooms per dwelling'
lab_AGE = 'Proportion of owner-occupied units built prior to 1940'
lab_DIS = 'Weighted distances to five Boston employment centres'
lab_RAD = 'Index of accessibility to radial highways'
lab_TAX = 'Full-value property-tax rate per $10,000'
lab_PTRATIO = 'Pupil-teacher ratio by town'
lab_B = '1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town'
lab_LSTAT = ' % lower status of the population'
lab_MEDV = 'Median value of owner-occupied homes in $1000 '


df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

#lab_NOX = ' nitric oxides concentration (parts per 10 million)'
#lab_MEDV = 'Median value of owner-occupied homes in $1000'
# Creating figure

X = df.drop('NOX', axis=1)
y = df['NOX']


print(f'Dataset X shape: {X.shape}')
print(f'Dataset y shape: {y.shape}')






