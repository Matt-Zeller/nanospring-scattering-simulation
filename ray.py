# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 04:51:50 2024

@author: Matt E. Zeller
"""

from math import *
import numpy as np


def line(m, b, N, x0, xf):
    line_array = np.zeros((N, 2))
    for i in range(N):
        s = abs(xf - x0) / N
        xi = x0 + i*s
        y = m*xi + b
        line_array[i, 0] = xi
        line_array[i, 1] = y
    return line_array
