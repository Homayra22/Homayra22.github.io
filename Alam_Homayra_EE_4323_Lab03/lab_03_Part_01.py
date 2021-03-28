#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 20:16:40 2021

@author: homayra
"""

import numpy as np
import cv2
import histogram_plotter
import matplotlib.pyplot as plt

image1=cv2.imread("cell.jpeg",0)
image1=cv2.imread("lowcell.jpeg",0)
image1=cv2.imread("building.jpeg",0)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
