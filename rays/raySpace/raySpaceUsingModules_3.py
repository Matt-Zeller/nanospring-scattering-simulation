# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 19:16:30 2024

@author: Matt E. Zeller
"""

from math import *
import numpy as np
import circle
import picture
from matplotlib import pyplot

circle = circle.perimeter(1., 0., 1000)

center = 8.
num_circles = 3

picture.stack(circle, (4, 4), -10., 10., center, num_circles)
picture.scatter(1, 1000, 0., center, num_circles)
