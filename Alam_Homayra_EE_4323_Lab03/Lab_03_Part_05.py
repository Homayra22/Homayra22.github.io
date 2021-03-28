#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 18:58:52 2021

@author: homayra
"""

import numpy as np
import cv2
import histogram_plotter
import matplotlib.pyplot as plt

image1=cv2.imread("cell.jpeg",0)

HP=np.array([[1,1,1],[1,1,1],[1,1,1]])/9

Y=histogram_plotter.Conv_Cor(image1,HP,0)

cv2.imshow("Original Image",image1)
cv2.imshow("Filtered",Y)



cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)