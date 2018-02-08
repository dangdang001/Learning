# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 11:11:23 2017

Applied Machine Learning, Module 1: A simple classification task

@author: dyin
"""

# check and change current working directory
import os
print os.getcwd()
os.chdir("C:/Users/dyin/Documents")

# 1. Import required modules and load data file

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

fruits=pd.read_table("./fruit_data_with_colors.txt")
fruits.head()

# create a mapping from fruit label value to fruit name to make results easier to interpret
lookup_fruit_name=dict(zip(fruits['fruit_label'].unique(),fruits['fruit_name'].unique()))

# 2. examining the data


# Create train-test split

X=fruits[['mass','width','height','color_score']]
y=fruits['fruit_label']

X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.25,random_state=0) # random_state: seed used

# feature pair scatter plot

from matplotlib import cm
cmap=cm.get_cmap('gnuplot')
scatter=pd.scatter_matrix(X_train, c=y_train,marker='o',s=40,hist_kwds={'bins':15},figsize=(9,9),cmap=cmap)

# 3d scatter plot
from mpl_toolkits.mplot3d import Axes3D
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.scatter(X_train['width'],X_train['height'],X_train['color_score'],c=y_train,marker='o',s=100)
ax.set_xlabel('width')
ax.set_ylabel('height')
ax.set_zlabel('color_score')
plt.show()

# 3. apply KNN to the data
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=5)

# Train the classifier (fit the estimator) using the training data
knn.fit(X_train, y_train)

# Estimate the accuracy of the classifier on future data, using the test data
knn.score(X_test,y_test)

# Use the trained k-NN classifier model to predict new data
fruit_predict=knn.predict([[20,4.3,5.5,0.7]])
lookup_fruit_name[fruit_predict[0]]

# Plot the decision boundaries of the k-NN classifier
from adspy_shared_utilities import plot_fruit_knn
plot_fruit_knn(X_train, y_train, 5, 'uniform')   # we choose 5 nearest neighbors

# How sensitive is k-NN classification accuracy to the choice of the 'k' parameter?
score=[]
for k in range(1,20):
    knn=KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train,y_train)
    score.append(knn.score(X_test,y_test))
plt.figure()
plt.scatter(range(1,20),score)
plt.xlabel('k')
plt.ylabel('accuracy')
plt.xticks([0,5,10,15,20])

# How sensitive is k-NN classification accuracy to the train/test split proportion?
plt.figure()
prop=np.arange(0.1,1.0,0.1)
knn=KNeighborsClassifier(n_neighbors=5)
for i in prop:
    score=[]
    for rep in range(1000):
        X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=i)
        knn.fit(X_train,y_train)
        score.append(knn.score(X_test,y_test))
    plt.plot(i,np.mean(score),'go')
plt.xlabel('Testing set proportion(%)')
plt.ylabel('Acurracy')
plt.title('Testing set proportion vs Acurracy (KNN-example)')
plt.savefig('Testing set proportion vs Acurracy (KNN-example).png')
plt.show()
