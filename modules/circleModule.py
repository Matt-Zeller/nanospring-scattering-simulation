# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 04:27:41 2024

@author: Matt E. Zeller
"""

from math import *
import numpy as np

def perimeter(r,h,N):
#r is radius of circle
#h is x position of center of circle (k=0 always)
#N is number of subintervals
    circ_array = np.zeros(((2*N)+1,2))
    for x in range((2*N)+1):
        y = sqrt(abs((r**2)-(((((x/N)-r)-h)**2))))
        circ_array[x,0] = ((x/N)-r)
        circ_array[x,1] = y
    return circ_array