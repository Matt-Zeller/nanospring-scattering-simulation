# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 17:45:07 2024

@author: Matt E. Zeller
"""

import numpy as np
import circle
import ray
from matplotlib import pyplot

circle_xy = circle.perimeter(1., 0., 1000)
size = (6, 6)
a, b = -10., 10.
center = 8
N = 10
num_circles = 100
axes_visible = False

fig = pyplot.figure(figsize=size)
ax = pyplot.axis(xmin=a, xmax=b, ymin=a, ymax=b)
ax = pyplot.axis(axes_visible)
shift = np.ones(np.shape(circle_xy))
x_shift = center * shift[..., 1]
x_values = circle_xy[..., 0] + x_shift
# plot n vertically shifted copies of original circle
for n in range(N):
    copy = 2*n*shift[..., 1]
    top_hemi_y = circle_xy[..., 1] + copy
    bot_hemi_y = np.negative(circle_xy[..., 1]) + copy
    circles = pyplot.plot(x_values, top_hemi_y, x_values, bot_hemi_y)
    pyplot.setp(circles, color='0')

    top_hemi_y = circle_xy[..., 1] - copy
    bot_hemi_y = np.negative(circle_xy[..., 1]) - copy
    circles = pyplot.plot(x_values, top_hemi_y, x_values, bot_hemi_y)
    pyplot.setp(circles, color='0')
