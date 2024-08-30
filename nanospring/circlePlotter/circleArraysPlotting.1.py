# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 19:16:30 2024

@author: Matt E. Zeller
"""
from math import *
import numpy as np
from matplotlib import pyplot

def circle(r,h,N):
#r is radius of circle
#h is x position of center of circle (k=0 always)
#N is number of subintervals
    circ_array = np.zeros(((2*N)+1,2))
    for x in range((2*N)+1):
        y = sqrt(abs((r**2)-(((((x/N)-r)-h)**2))))
        circ_array[x,0]=((x/N)-r)
        circ_array[x,1]=y
    return circ_array

A = circle(1.,0.,1000)

fig = pyplot.figure(figsize=(10,10))
ax = pyplot.axis(xmin=-10,xmax=10,ymin=-10,ymax=10)
ax = pyplot.axis(False)

# fig, ax = pyplot.subplots(figsize=(5,5))
# fig.add_axes((0.5,0.5,0.5,0.5))
# fig.add_axes((1,1,1,1))
# fig.add_axes((1,1,1,1))
lines = pyplot.plot(A[...,0],A[...,1],A[...,0],np.negative(A[...,1]),'b')
pyplot.setp(lines, color='0')
# pyplot.show()
# ax.autoscale()
