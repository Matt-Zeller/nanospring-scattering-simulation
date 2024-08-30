# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 19:16:30 2024

@author: Matt E. Zeller
"""

from math import *
import numpy as np
import circleModule
import rayModule
from matplotlib import pyplot

C = circleModule.perimeter(1., 0., 1000)
R = rayModule.line(0., 0., 1000, 0., 20.)

fig = pyplot.figure(figsize=(4,4))
min = -5
max = 10
ax = pyplot.axis(xmin=min,xmax=max,ymin=min,ymax=max)
ax = pyplot.axis(False)

shift = np.ones(np.shape(C))
circCenter = 5.
xShift = circCenter*shift[...,1]
Hemi_X = C[...,0] + xShift
#plot n vertically shifted copies of original circle
for n in range(3):
    copy = 2*n*shift[...,1]
    topHemi_Y = C[...,1] + copy
    botHemi_Y = np.negative(C[...,1]) + copy
    circles = pyplot.plot(Hemi_X, topHemi_Y, Hemi_X, botHemi_Y)
    pyplot.setp(circles, color='0')
    
rays = pyplot.plot(R[...,0], R[...,1], 'b')
pyplot.setp(rays, color='0')
