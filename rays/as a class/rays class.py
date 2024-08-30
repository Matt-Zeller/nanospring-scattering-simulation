# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 01:57:01 2024

@author: Matt E. Zeller
"""

class Ray():
    """A single 2-D ray for creating large sets of uncollimated rays."""
    
	def __init__(self, angle, origin, termination):
        """"""
    ray(m,b,N,x0,xf):
		line_array = np.zeros((N,2))
		for i in range(N):
			s = abs(xf - x0) / N
			xi = x0 + i*s
			y = m*xi + b
			line_array[i,0] = xi
			line_array[i,1] = y
		return line_array