# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 01:15:11 2024

@author: Matt E. Zeller
"""

import numpy as np

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path
from matplotlib.transforms import Bbox

circle_path = Path.circle(center=(0., 0.))
circ = plt.Circle((0., 0.), 1., fill=False, edgecolor='black')

fig, ax = plt.subplots(figsize=(2, 2))
axis = plt.axis(xmin=-2., xmax=2., ymin=-2., ymax=2.)

ax.add_patch(circ)

bcircle = Bbox.null()
Bbox.update_from_path(bcircle, circle_path)

plt.show()
