# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 22:51:00 2024

@author: Matt E. Zeller
"""

"""A class for representing 2D cross-sections at the midpoint of a nanospring"""

from math import *
import numpy as np

class Circle():
    """An array of x, y values from the cartesian form of a circle."""
    
    def __init__(self, radius, xcenter, subintervals):
        """Initialize radius, center, and number of subintervals."""
        self.radius = radius
        self.xcenter = xcenter
        self.subintervals = subintervals
    
    def get_perimeter_array(self):
        """Return x, y array defining circle perimeter."""
        perimeter = np.zeros(((2*subintervals)+1,2))
        for x in range((2*subintervals)+1):
            y = sqrt(abs((r**2)-(((((x/subintervals)-r)-h)**2))))
            perimeter[x,0] = ((x/subintervals)-r)
            perimeter[x,1] = y
        return perimeter