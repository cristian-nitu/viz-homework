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
fig, axes = plt.subplots(2, 2, figsize=(8, 8))

axes[0, 0].plot(df['NOX'])
axes[0, 0].set_title('Nitric Oxides')
axes[0, 0].set_xlabel('Index')
axes[0, 0].set_ylabel('acid oxides')

axes[1, 0].scatter(df['TAX'], df['NOX'],
                color='black',
                marker='s',
                alpha=0.4,
                s=df['TAX'] ** 0.7)
axes[1, 0].set_title('Nitric Oxides by taxes value')
axes[1, 0].set_xlabel(lab_TAX)
axes[1, 0].set_ylabel(lab_NOX)

axes[0, 1].scatter(df['MEDV'], df['NOX'],
                color='green',
                marker='s',
                alpha=0.3,
                s=df['MEDV'] ** 1.2)
axes[0, 1].set_title('')
axes[1, 0].set_xlabel(lab_MEDV)
axes[1, 0].set_ylabel(lab_NOX)

axes[1, 1].scatter(df['CRIM'], df['TAX'],
                color='RED',
                marker='s',
                alpha=0.8,
                s=df['CRIM'] ** 1.8)
axes[1, 1].set_title(lab_CRIM)
axes[1, 1].set_xlabel(lab_CRIM)
axes[1, 1].set_xlabel(lab_TAX)
plt.tight_layout()
plt.savefig('noxBoston.png')

plt.close()
