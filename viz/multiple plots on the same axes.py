#!/usr/bin/env python3

import os

import matplotlib.pyplot as plt
import pandas as pd

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

os.makedirs('plots/multiple_plot_axes', exist_ok=True)

plt.style.use("ggplot")

fig, axes = plt.subplots(1, 1, figsize=(5, 5))

# This time we plot multiple plots on the same axes, to get some perspective on their comparisons
axes.scatter(df['CRIM'], df['LSTAT'], alpha=0.7, label='LOWEST CRIME')
axes.scatter(df['AGE'], df['TAX'], alpha=0.7, label='AGE COMPARATION')

axes.scatter(df['ZN'], df['INDUS'], alpha=0.7)

axes.scatter(df['DIS'], df['RAD], s=(df['INDUS']) ** 2.5,
             label=f'Alcohol to Malic Acid', color='orange', marker='o', edgecolors='w', alpha=0.7)

axes.set_xlabel('CRIME')
axes.set_ylabel('TotaL')
axes.set_title(f'comparisons')
axes.legend()
plt.savefig(f'plots/multiplot_scatter.png', dpi=300)
plt.close()
