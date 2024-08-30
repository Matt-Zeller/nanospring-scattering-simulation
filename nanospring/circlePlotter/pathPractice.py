# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 19:57:45 2024

@author: Matt E. Zeller
"""

from math import *
import numpy as np
from matplotlib import pyplot
from matplotlib import patches
from matplotlib.path import Path

vertices = [
    (0.,0.),
    (1.,1.),
]

codes = [
    Path.MOVETO,
    Path.LINETO,
]

path = Path(vertices, codes)

fig, ax = pyplot.subplots()
patch = patches.PathPatch(path)
ax.add_patch(patch)