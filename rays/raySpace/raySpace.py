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
        circ_array[x,0] = ((x/N)-r)
        circ_array[x,1] = y
    return circ_array

def ray(m,b,N,x0,xf):
    line_array = np.zeros((N,2))
    for i in range(N):
        s = abs(xf - x0) / N
        xi = x0 + i*s
        y = m*xi + b
        line_array[i,0] = xi
        line_array[i,1] = y
    return line_array

C = circle(1., 0., 1000)
R = ray(0.5, 2.2, 1000, 0., 20.)

fig = pyplot.figure(figsize=(5,5))
min = -5
max = 10
ax = pyplot.axis(xmin=min,xmax=max,ymin=min,ymax=max)
ax = pyplot.axis(False)

shift = np.ones(np.shape(C))
circCenter = 5.
xShift = circCenter*shift[...,1]
topHemi_X = C[...,0] + xShift
botHemi_X = C[...,0] + xShift
#plot n vertically shifted copies of original circle
for n in range(3):
    copy = 2*n*shift[...,1]
    topHemi_Y = C[...,1] + copy
    botHemi_Y = np.negative(C[...,1]) + copy
    circles = pyplot.plot(topHemi_X, topHemi_Y, botHemi_X, botHemi_Y)
    pyplot.setp(circles, color='0')
    
rays = pyplot.plot(R[...,0], R[...,1], 'b')
pyplot.setp(rays, color='0')
