# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:40:49 2024

@author: Matt E. Zeller
"""

import numpy as np
import ray
from matplotlib import pyplot


def space(size, a, b, axes_visible=False):
    """Display the coordinate space before any objects are added."""
    fig = pyplot.figure(figsize=size)
    ax = pyplot.axis(xmin=a, xmax=b, ymin=a, ymax=b)
    ax = pyplot.axis(axes_visible)


def stack(circle_xy, size, a, b, center, N, axes_visible=False):
    """Make copies of a circle and stack them vertically."""
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


def scatter(N, subints, a, b, spread):
    rng = np.random.default_rng()
    randoms = rng.uniform(low=-1., high=1., size=(N, 2))
    ray_set = np.zeros((N, subints, 2))
    for n in range(N):
        slope = randoms[n, 0]
        intercept = spread*randoms[n, 1]
        ray_array = ray.line(slope, intercept, subints, a, b)
        ray_set[n] = ray_array
        ray_draw = pyplot.plot(ray_array[..., 0], ray_array[..., 1], 'b')
        pyplot.setp(ray_draw, color='0')
    return ray_set
