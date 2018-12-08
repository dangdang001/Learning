# -*- coding: utf-8 -*-
"""
Created on Wed Nov 01 10:48:15 2017

Applied Plotting, Charting & Data Representation in Python

Week 3
@author: dyin
"""

# import modules needed
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# 1. Subplot

# linear data on the left, quadratic data on the right
plt.figure()
plt.subplot(1,2,1) # or plt.subplot(121), altenatively
linear_data=np.array([1,2,3,4,5,6,7,8])
plt.plot(linear_data,'-o')
plt.subplot(1,2,2)
quadratic_data=linear_data**2
plt.plot(quadratic_data,'-x')

# plot quadratic on the 1st subplot
plt.subplot(121)
plt.plot(quadratic_data,'-x')


# pass axis using sharey to ensure two subplots share the same y axis
plt.figure()
ax1=plt.subplot(121)
plt.plot(linear_data,'-o')
ax2=plt.subplot(122,sharey=ax1)
plt.plot(quadratic_data,'-x')

# create a 3x3 grid of subplots using "subplots"
'''
Creates just a figure and only one subplot

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Simple plot')

Creates two subplots and unpacks the output array immediately

f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.plot(x, y)
ax1.set_title('Sharing Y axis')
ax2.scatter(x, y)
'''

plt.figure()
fig,((ax1,ax2,ax3),(ax4,ax5,ax6),(ax7,ax8,ax9))=plt.subplots(3,3,sharex=True,sharey=True)
ax5.plot(linear_data,'-')

# set inside tick labels to visible
for ax in plt.gcf().get_axes():
    for label in ax.get_xticklabels()+ax.get_yticklabels():
        label.set_visible(True)

# 2. Histogram

# draw n = 10, 100, 1000, and 10000 samples from the normal distribution and plot corresponding histograms
plt.figure()
fig,((ax1,ax2),(ax3,ax4))=plt.subplots(2,2,sharex=True)
axs=[ax1,ax2,ax3,ax4]
for n in range(len(axs)):
    sample_size=10**n
    sample=np.random.normal(0,1,size=sample_size)
    axs[n].hist(sample,bins=100)
    axs[n].set_title('n={}'.format(sample_size))
    
    
# use gridspec to partition the figure into subplots(marginal distributions of the data)
plt.figure()
x=np.random.normal(0,1,size=1000)
y=np.random.random(size=1000)
plt.scatter(x,y)

import matplotlib.gridspec as gridspec

plt.figure()
gspec=gridspec.GridSpec(3,3)
top_histogram=plt.subplot(gspec[0,1:])
side_histogram=plt.subplot(gspec[1:,0])
lower_right=plt.subplot(gspec[1:,1:])

lower_right.scatter(x,y)
top_histogram.hist(x,bins=100)
side_histogram.hist(y,bins=100,orientation='horizontal',normed=True)
# flip the side histogram's x axis
side_histogram.invert_xaxis()

# change axes limits
for ax in [top_histogram, lower_right]:
    ax.set_xlim(-5, 5)
for ax in [side_histogram, lower_right]:
    ax.set_ylim(0, 1)

# 3. Box plot
normal_sample=np.random.normal(0,1,size=10000)
random_sample=np.random.random(size=10000)
gamma_sample=np.random.gamma(2,size=10000)

df=pd.DataFrame({'normal':normal_sample,'random':random_sample,'gamma':gamma_sample})

df.describe()
plt.clf()
_=plt.boxplot([df['normal'],df['random'],df['gamma']],whis='range')# if `whis` argument isn't passed, boxplot defaults to showing 1.5*interquartile (IQR) whiskers with outliers

# attach another plot on top of the original one
import mpl_toolkits.axes_grid1.inset_locator as mpl_il

plt.figure()
plt.boxplot([ df['normal'], df['random'], df['gamma'] ], whis='range')
# overlay axis on top of another 
ax2 = mpl_il.inset_axes(plt.gca(), width='60%', height='40%', loc=2)
ax2.hist(df['gamma'], bins=100)
ax2.margins(x=0.5)
# switch the y axis ticks for ax2 to the right side
ax2.yaxis.tick_right()



# 4. Heatmap
y=np.random.normal(0,1,size=10000)
x=np.random.random(size=10000)
_=plt.hist2d(x,y,bins=100)
plt.colorbar()

# 5. Animation
import matplotlib.animation as animation
n=100
x=np.random.randn(n)
def update(curr):
    if curr==n:
        a.event_source.stop()
        plt.cla()
        bins=np.arange(-4,4,0.5)
        plt.hist(x[:curr],bins=bins)
        plt.axis([-4,4,0.5])
        plt.gca().set_title('Sampling the Normal Distribution')
        plt.gca().set_ylabel('Frequency')
        plt.gca().set_xlabel('Value')
        plt.annotate('n={}'.format(curr),[3,27])

fig=plt.figure()
a=animation.FuncAnimation(fig, update, interval=100)        
        
# 6.Interactivity
plt.figure()
data = np.random.rand(10)
plt.plot(data)

def onclick(event):
    plt.cla()
    plt.plot(data)
    plt.gca().set_title('Event at pixels {},{} \nand data {},{}'.format(event.x, event.y, event.xdata, event.ydata))

# tell mpl_connect we want to pass a 'button_press_event' into onclick when the event is detected
plt.gcf().canvas.mpl_connect('button_press_event', onclick)
    
from random import shuffle
origins = ['China', 'Brazil', 'India', 'USA', 'Canada', 'UK', 'Germany', 'Iraq', 'Chile', 'Mexico']

shuffle(origins)

df = pd.DataFrame({'height': np.random.rand(10),
                   'weight': np.random.rand(10),
                   'origin': origins})
df
plt.figure()
# picker=5 means the mouse doesn't have to click directly on an event, but can be up to 5 pixels away
plt.scatter(df['height'], df['weight'], picker=5)
plt.gca().set_ylabel('Weight')
plt.gca().set_xlabel('Height')

def onpick(event):
    origin = df.iloc[event.ind[0]]['origin']
    plt.gca().set_title('Selected item came from {}'.format(origin))

# tell mpl_connect we want to pass a 'pick_event' into onpick when the event is detected
plt.gcf().canvas.mpl_connect('pick_event', onpick)
