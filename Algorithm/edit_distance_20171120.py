# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 14:11:04 2017

Edit distance using dynamic programming

@author: dyin
"""


import numpy as np

x="abcdefg"
y="aabcefh"


def edit_dist(x,y):
    n=len(x)
    m=len(y)
    D=np.zeros((n+1,m+1))
    for i in range(n+1):
        D[i,0]=i
    for j in range(m+1):
        D[0,j]=j
    for i in range(1,n+1):
        for j in range(1,m+1):
            cost=0 if x[i-1]==y[j-1] else 1  
            D[i,j]=min(D[i-1,j-1]+cost,D[i,j-1]+1,D[i-1,j]+1)                                 
    return D[n,m]  
        
edit_dist(x,y)    

edit_dist(x="ABCDE",y="ABDE") 
