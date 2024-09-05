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
from matplotlib import backend_bases

circle_path = Path.circle(center=(0., 0.))
# circ = plt.Circle((0., 0.), 1., fill=False, edgecolor='black')


fig, ax = plt.subplots(figsize=(4, 4))
axis = plt.axis(xmin=-3., xmax=3., ymin=-3., ymax=3.)

circ = patches.PathPatch(circle_path, fill=False, edgecolor='black')
ax.add_patch(circ)

bcircle = Bbox.null()
bbox = Bbox.update_from_path(bcircle, circle_path)

for i in range(25):
    vertices = (np.random.random((2, 2)) - 0.5) * 6.
    path = Path(vertices)
    if path.intersects_path(circle_path):
        color = 'r'
    else:
        color = 'b'
    ax.plot(vertices[:, 0], vertices[:, 1], color=color, lw=0.5)

plt.show()
