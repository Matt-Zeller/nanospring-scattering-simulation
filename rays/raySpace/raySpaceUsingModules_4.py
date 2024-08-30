# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 19:16:30 2024

@author: Matt E. Zeller
"""

from math import *
import numpy as np
import circle
import ray
import picture
from matplotlib import pyplot

circle = circle.perimeter(1., 0., 1000)

center = 8.
num_circles = 3

circle_set = picture.stack(circle, (6, 6), -10., 10., center, num_circles)
ray_set = picture.scatter(1, 1000, 0., center, 0.)
