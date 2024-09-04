# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:40:49 2024

@author: Matt E. Zeller
"""

import numpy as np
from matplotlib import pyplot


def space(size, a, b, showAxis=False):
    """Display the coordinate space before any objects are added."""
    fig = pyplot.figure(figsize=size)
    ax = pyplot.axis(xmin=a, xmax=b, ymin=a, ymax=b)
    ax = pyplot.axis(showAxis)


def
shift = np.ones(np.shape(C))
circCenter = 5.
xShift = circCenter*shift[..., 1]
Hemi_X = C[..., 0] + xShift
# plot n vertically shifted copies of original circle
for n in range(3):
    copy = 2*n*shift[..., 1]
    topHemi_Y = C[..., 1] + copy
    botHemi_Y = np.negative(C[..., 1]) + copy
    circles = pyplot.plot(Hemi_X, topHemi_Y, Hemi_X, botHemi_Y)
    pyplot.setp(circles, color='0')
