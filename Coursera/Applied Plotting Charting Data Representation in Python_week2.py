# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 13:38:24 2017

Applied Plotting, Charting & Data Representation in Python

Week 2

@author: dyin
"""

import matplotlib as mpl

mpl.get_backend()

import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

plt.plot(3,2,'o')


# 1. scatterplot

x=np.array([1,2,3,4,5,6,7,8])
y=x
plt.figure()
plt.scatter(x,y)

# add color
c=['green']*(len(x)-1)
c.append('red')

plt.figure()
plt.scatter(x,y,color=c)

zip_generator=zip([1,2,3,4,5],[6,7,8,9,10])
print(zip_generator)
print(zip(*zip_generator))

plt.figure()
plt.scatter(x[:2],y[:2],color='red',label='Tall student')
plt.scatter(x[2:],y[2:],color='blue',label='Short student')
plt.title('Relationship between ball kicking and grades')
plt.xlabel('The number of times the student kicks a ball')
plt.ylabel('The grades of the student')
plt.legend()

# 2. line plot

linear_data=np.array([1,2,3,4,5,6,7,8])
quadratic_data=linear_data**2
plt.plot(linear_data,'-o',quadratic_data,'-o')
plt.plot(linear_data,'-o',quadratic_data,'--r')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Title')
plt.legend(['Linear',' Quadratic'],loc='upper right')

# fill the area between the linear data and exponential data (useful in plotting CI)
plt.gca().fill_between(range(len(linear_data)),
        linear_data,quadratic_data,
        facecolor='blue',alpha=0.25)
# alpha: degree of transparent

# adjust(rotate) tick labels
plt.figure()
observation_dates=np.arange('2017-01-01','2017-01-09',dtype='datetime64[D]')
observation_dates=map(pd.to_datetime,list(observation_dates)) # convert the object to a list to get rid of the error when using map function
plt.plot(observation_dates,linear_data,'-o', observation_dates,quadratic_data,'-o')

# rotate the tick labels for the x axis
x = plt.gca().xaxis
for item in x.get_ticklabels():
    item.set_rotation(45)

# adjust the subplot so the text doesn't run off the image
plt.subplots_adjust(bottom=0.25)

# alternative way to set labels and title
ax = plt.gca()
ax.set_xlabel('Date')
ax.set_ylabel('Units')
ax.set_title("Exponential ($x^2$) vs. Linear ($x$) performance")

# 3. bar plot
plt.figure()
xval=range(len(linear_data))
plt.bar(xval,linear_data,width=0.3)

# plot another set of bars, adjusting the new xvals to make up for the first set of bars plotted
new_xval=[]
for item in xval:
    new_xval.append(item+0.3)
plt.bar(new_xval, quadratic_data, width=0.3,color='red')

# add random error(confidence interval to bar plot
from random import randint
linear_err=[randint(0,15) for x in range(len(linear_data))]
plt.bar(xval, linear_data, width=0.3,yerr=linear_err)

# stack bar plot
plt.figure()
plt.bar(xval,linear_data,width=0.3,color='blue')
plt.bar(xval,quadratic_data,width=0.3,color='red',bottom=linear_data)

# horizontal bar charts
plt.figure()
plt.barh(xval,linear_data,height=0.3,color='blue')
plt.barh(xval,quadratic_data,height=0.3,color='red',left=linear_data)
