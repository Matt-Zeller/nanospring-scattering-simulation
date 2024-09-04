# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 02:49:19 2024

@author: Matt E. Zeller
"""

import matplotlib.pyplot as plt
import circle

circle = circle.perimeter(1., 0., 10)

fig = plt.figure(figsize=(1, 1))
ax = fig.subplots()
ax.plot(circle[..., 0], circle[..., 1])
