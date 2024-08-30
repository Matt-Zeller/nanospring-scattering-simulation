# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 19:16:30 2024

@author: Matt E. Zeller
"""

from math import *
import numpy as np
import circleModule
import rayModule
import stack_circles_1 as picture
from matplotlib import pyplot

C = circleModule.perimeter(1., 0., 1000)
R = rayModule.line(0., 0., 1000, 0., 20.)

picture.stack()

rays = pyplot.plot(R[..., 0], R[..., 1], 'b')
pyplot.setp(rays, color='0')

circleModule.perimeter()
