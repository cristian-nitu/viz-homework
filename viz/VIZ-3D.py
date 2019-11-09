import os


import pandas as pd
import warnings
import numpy as np
import matplotlib.pyplot as plt

warnings.simplefilter(action='ignore', category=FutureWarning)
print('x' in np.arange(5))

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

# All the plots in this section use the BOSTON

# Example of creating a Histogram plot
fig, axes = plt.subplots(1, 1, figsize=(5, 5))
axes.hist(df['CHAS'], bins=20, color='b', label='house by the river ')
axes.set_title('Charles River')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.legend()
plt.savefig('plots/simmetry_hist.png', dpi=300)

# # Example of creating a Pie plot
fig, axes = plt.subplots(1, 1, figsize=(8, 8))
axes.pie(df['TAX'].value_counts(), labels=df['TAX'].value_counts().index.tolist())
axes.set_title('Boston Houses value')
#axes.legend()
plt.savefig('plots/pie.png', dpi=300)
#
# # Example of creating a Bar plot
fig, axes = plt.subplots(1, 1, figsize=(10, 10))
axes.bar(np.arange(0, len(df['CRIM'])), df['TAX'], color='r', label='DIS')
axes.set_title(lab_CRIM)
axes.set_xlabel(lab_TAX)
axes.set_ylabel(lab_DIS)
axes.legend()
plt.savefig('plots/simmetry_bar.png', dpi=200)
#
# # Example of creating a Correlation Heatmap plot
fig, axes = plt.subplots(1, 1, figsize=(20, 20))
df['concoded_MEDV'] = df['MEDV'].map({10 : 0, 60 : 1})
correlation = df.corr().round(2)
im = axes.imshow(correlation)
cbar = axes.figure.colorbar(im, ax=axes)
cbar.ax.set_ylabel('Correlation', rotation=-90, va="bottom")
numrows = len(correlation.iloc[0])
numcolumns = len(correlation.columns)
axes.set_xticks(np.arange(numrows))
axes.set_yticks(np.arange(numcolumns))
axes.set_xticklabels(correlation.columns)
axes.set_yticklabels(correlation.columns)
plt.setp(axes.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
for i in range(numrows):
    for j in range(numcolumns):
        text = axes.text(j, i, correlation.iloc[i, j], ha='center', va='center', color='w')
axes.set_title('Heatmap of Correlation of House Value')
fig.tight_layout()
plt.savefig('plots/houses_correlation_heatmap.png')

# # Example of creating a 3D plot
price_min = df[df['MEDV'] >= 10]
price_max = df[df['MEDV'] < 60]
fig = plt.figure()
axes = fig.add_subplot(1, 1, 1, projection='3d')
line1 = axes.scatter(price_min['TAX'], price_min['RM'], price_min['LSTAT'])
line2 = axes.scatter(price_max['TAX'], price_max['RM'], price_max['LSTAT'])
axes.legend((line1, line2), ('Affordable Houses', 'Expensive Houses'))
axes.set_xlabel('Full Value Taxes')
axes.set_ylabel('Number of Room')
axes.set_zlabel('Lowest Ocuppation')
plt.savefig('plots/3d.png', dpi= 500)

plt.close()
