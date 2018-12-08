# -*- coding: utf-8 -*-
"""
Created on Wed Nov 01 13:43:54 2017

Applied Plotting, Charting & Data Representation in Python

Week 4
@author: dyin
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.available
plt.style.use('seaborn-colorblind')

np.random.seed(123)

# 1.plot option for pandas DataFrame
df = pd.DataFrame({'A': np.random.randn(365).cumsum(0), 
                   'B': np.random.randn(365).cumsum(0) + 20,
                   'C': np.random.randn(365).cumsum(0) - 20}, 
                  index=pd.date_range('1/1/2017', periods=365))
df.head()
df.plot();
df.plot('A','B', kind = 'scatter'); # or:
ax=df.plot.scatter('A', 'C', c='B', s=df['B'], colormap='viridis')
ax.set_aspect('equal')

df.plot.box(); # boxplot
df.plot.hist(alpha=0.8); # histogram
df.plot.kde(); # kernel density estimation plot


# 2.Seaborn
import seaborn as sns
np.random.seed(1234)
v1=pd.Series(np.random.normal(0,10,1000),name='v1')
v2=pd.Series(2*v1+np.random.normal(60,15,1000),name='v2')

plt.figure()
plt.hist(v1,alpha=0.7,bins=np.arange(-50,150,5),label='v1')
plt.hist(v2,alpha=0.7,bins=np.arange(-50,150,5),label='v2')
plt.legend()

plt.figure()
plt.hist([v1, v2], histtype='barstacked', normed=True);
v3 = np.concatenate((v1,v2))
sns.kdeplot(v3);

plt.figure()
# we can pass keyword arguments for each individual component of the plot
sns.distplot(v3, hist_kws={'color': 'Teal'}, kde_kws={'color': 'Navy'});

# joint plot(marginal plot)
sns.jointplot(v1, v2, alpha=0.4);
grid = sns.jointplot(v1, v2, alpha=0.4);
grid.ax_joint.set_aspect('equal')

sns.jointplot(v1, v2, kind='hex');

sns.set_style('white')

sns.jointplot(v1, v2, kind='kde', space=0);

# pairplot
iris = pd.read_csv('iris.csv')
iris.head()
sns.pairplot(iris, hue='Name', diag_kind='kde', size=2);

plt.figure(figsize=(8,6))
plt.subplot(121)
sns.swarmplot('Name', 'PetalLength', data=iris);
plt.subplot(122)
sns.violinplot('Name', 'PetalLength', data=iris);


