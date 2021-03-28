#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 16:17:27 2021

@author: homayra
"""

import numpy as np
import cv2
import histogram_plotter

image1=cv2.imread("cell.jpeg",0)

histogram_plotter.his_img(image1)

cv2.imshow("Original Image",image1)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

