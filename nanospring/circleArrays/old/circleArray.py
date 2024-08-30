# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 04:22:27 2024

@author: mattz
"""

from math import *
import numpy as np

#N is number of subintervals
#r is radius of circle
#h is x position of center of circle (k=0 always)
def circle(r,h,N):
    circ_array = np.zeros(((2*N)+1,2))
    for x in range((2*N)+1):
        y = sqrt((r**2)-(((((x/N)-r)-h)**2)))
        circ_array[x,0]=((x/N)-r)
        circ_array[x,1]=y
    return circ_array

A=circle(1,0,100)

A