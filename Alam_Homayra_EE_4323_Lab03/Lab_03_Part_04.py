#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 17:48:27 2021

@author: homayra
"""

import numpy as np
import cv2
import histogram_plotter
import matplotlib.pyplot as plt

image1=cv2.imread("cell.jpeg",1)
b,g,r=cv2.split (image1)

clahe=cv2.createCLAHE(clipLimit=3.0,tileGridSize=(8,8))
clahe_b=clahe.apply(b)
clahe_g=clahe.apply(g)
clahe_r=clahe.apply(r)

histogram_plotter.his_img(b)
histogram_plotter.his_img(clahe_b)

histogram_plotter.his_img(g)
histogram_plotter.his_img(clahe_g)

histogram_plotter.his_img(r)
histogram_plotter.his_img(clahe_r)

bgr_clahe=cv2.merge([clahe_b,clahe_g,clahe_r])



cv2.imshow("Original Image",image1)
cv2.imshow("Hist_Equ",bgr_clahe)



cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
