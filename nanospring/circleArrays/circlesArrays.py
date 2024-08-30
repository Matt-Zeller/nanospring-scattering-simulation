# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 00:30:16 2024

@author: Matt E. Zeller
"""

from math import *
import numpy as np

def circle(r,h,N):
#r is radius of circle
#h is x coordinate of center of circle (k=0 always)
#N is number of subintervals
    circ_array = np.zeros((N+1,2))
    #calculate y values at left-hand x value for N evenly spaced subintervals 
    #(from h-r to h+r: the diameter)
    for i in range(N+1):
        #xi is the x coordinate where ith point will be plotted
        xi = i*(2*r)/N-r
        y = sqrt(abs((r**2)-(xi**2)))
        circ_array[i,0]=xi+h
        circ_array[i,1]=y
    return circ_array

def vertShift(a,k):
#takes array a, adds k to every y element
    for i in range(np.size(a,0)):
        a[i,1] = a[i,1] + k
    return a

A = circle(1,1,100)
B = circle(1,1,100)
B = vertShift(B,1)