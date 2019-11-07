import os

import matplotlib.pyplot as plt
import pandas as pd

# Loading dataset
df = pd.read_csv('c:/users/cristiann/documents/github/viz-homework/viz/data/boston/housing.data',
             sep='\s+',
              header=None)

#df = pd.read_csv('..viz/data/boston/housing.data',
       #          sep='\s+',
        #       header=None)

# Setting columns to dataset
## 1 CRIM - per capita crime rate by town
## 2 ZN - proportion of residential land zoned for lots over 25,000 sq.ft.
## 3 INDUS - proportion of non-retail business acres per town.
## 4 CHAS - Charles River dummy variable (1 if tract bounds river; 0 otherwise)
## 5 NOX - nitric oxides concentration (parts per 10 million)
## 6 RM - average number of rooms per dwelling
## 7 AGE - proportion of owner-occupied units built prior to 1940
## 8 DIS - weighted distances to five Boston employment centres
## 9 RAD - index of accessibility to radial highways
## 10 TAX - full-value property-tax rate per $10,000
## 11 PTRATIO - pupil-teacher ratio by town
## 12 B - 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
## 13 LSTAT - % lower status of the population
## 14 MEDV - Median value of owner-occupied homes in $1000's


df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

lab_NOX = ' nitric oxides concentration (parts per 10 million)'
lab_MEDV = 'Median value of owner-occupied homes in $1000'
# Creating figure
fig, axes = plt.subplots(2, 1, figsize=(8, 8))

axes[0].plot(df['NOX'])
axes[0].set_title('Nitric oxides')
axes[0].set_xlabel('Index')
axes[0].set_ylabel('acid oxides')

axes[1].scatter(df['MEDV'], df['NOX'],
                color='black',
                marker='s',
                alpha=0.3,
                s=df['MEDV'] ** 1.2)
#axes[1].set_title('Nitric Oxides Concentration')

axes[1].set_title(lab_NOX)

plt.tight_layout()
plt.savefig('noxBoston.png')
plt.show()
plt.close()
